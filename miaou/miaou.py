# commandes :
# p : entrer/sortir de pause
# t : déplacements avec/sans trainées
# + / r (sur pad) : augmenter la vitesse
# - / l (sur pad) : diminuer la vitesse
# n : fond d'écran noir
# b : fond d'écran blanc
# esc : sortir du programme
# s (uniquement si le programme est en pause) : sauvegarde de l'image affichée sous le format image_%Y_%m_%d_%H_%M_%S.bmp

import pygame
import sys
import random
import datetime

pygame.init()

infoObject = pygame.display.Info()

winHeight = infoObject.current_h
winWidth = infoObject.current_w
continuer = True
enPause = False
cas = 1
vit = 50
chaos = False
nb_img_sauv_max = 5
nb_img_sauv = 0
avecTrainee = False

chats = [pygame.image.load("img/chat1.bmp"), pygame.image.load("img/chat2.bmp"), pygame.image.load("img/chat3.bmp"),
         pygame.image.load("img/chat4.bmp"), pygame.image.load("img/chat5.bmp"), pygame.image.load("img/chat6.bmp")]


def changer_chat(tab):
    idx = random.randint(0, 5)

    img_chat = tab[idx]

    transparent_color = pygame.Color(255, 0, 0)
    img_chat.set_colorkey(transparent_color)

    return img_chat


img = changer_chat(chats)

width = img.get_width()
height = img.get_height()

# x = winWidth / 2 - width / 2
# y = winHeight / 2 - height / 2
x = random.randint(0, winWidth - width)
y = random.randint(0, winHeight - height)

win = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

pygame.display.set_caption("Miaow")

win.fill((0, 0, 0))

while continuer:
    pygame.time.delay(vit)

    if avecTrainee:
        win.fill((0,0,0))
    win.blit(img, (x, y))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = False
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                enPause = not enPause
            if event.key == pygame.K_ESCAPE:
                continuer = False
                break
            if event.key == pygame.K_n:
                win.fill((0, 0, 0))
                pygame.display.update()
            if event.key == pygame.K_b:
                win.fill((255, 255, 255))
                pygame.display.update()
            if event.key == pygame.K_s and enPause and (nb_img_sauv <= nb_img_sauv_max):
                pygame.image.save(win, "image_" + str(datetime.datetime.today().strftime('%Y_%m_%d_%H_%M_%S')) + ".bmp")
                nb_img_sauv += 1
            if event.key == pygame.K_t:
                avecTrainee = not avecTrainee
                

    keys = pygame.key.get_pressed()
    if (keys[pygame.K_KP_PLUS] or keys[pygame.K_r])and vit > -50:
        vit -= 1
    if (keys[pygame.K_KP_MINUS] or keys[pygame.K_l]) and vit <= 200:
        vit += 1
    if keys[pygame.K_DOWN] and y <= (winHeight - height + 2) and enPause:
        y += 2
    if keys[pygame.K_UP] and y >= 2 and enPause:
        y -= 2
    if keys[pygame.K_RIGHT] and x <= (winHeight - height + 2) and enPause:
        x += 2
    if keys[pygame.K_LEFT] and x >= 2 and enPause:
        x -= 2

    if not enPause:
        match cas:
            case 1:  # x+ y+
                if x >= (winWidth - width):
                    if chaos:
                        cas = random.choice([3, 4])
                    else:
                        cas = 4
                    img = changer_chat(chats)

                elif y >= (winHeight - height):
                    if chaos:
                        cas = random.choice([2, 3])
                    else:
                        cas = 2
                    img = changer_chat(chats)

                else:
                    x += 2
                    y += 2

            case 2:  # x+ y-
                if x >= (winWidth - width):
                    if chaos:
                        cas = random.choice([3, 4])
                    else:
                        cas = 3
                    img = changer_chat(chats)

                elif y <= 0:
                    if chaos:
                        cas = random.choice([1, 4])
                    else:
                        cas = 1
                    img = changer_chat(chats)

                else:
                    x += 2
                    y -= 2

            case 3:  # x- y-
                if x <= 0:
                    if chaos:
                        cas = random.choice([1, 2])
                    else:
                        cas = 2
                    img = changer_chat(chats)

                elif y <= 0:
                    if chaos:
                        cas = random.choice([1, 4])
                    else:
                        cas = 4
                    img = changer_chat(chats)

                else:
                    x -= 2
                    y -= 2

            case 4:  # x- y+
                if x <= 0:
                    if chaos:
                        cas = random.choice([1, 2])
                    else:
                        cas = 1
                    img = changer_chat(chats)

                elif y >= (winHeight - height):
                    if chaos:
                        cas = random.choice([2, 3])
                    else:
                        cas = 3
                    img = changer_chat(chats)

                else:
                    x -= 2
                    y += 2

pygame.quit()
sys.exit()

