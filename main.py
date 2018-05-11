import pygame
import sys
import random as rnd

#----------------------------------------------------#
# simple RGB displaying program----------------------#
# You need pygame to run it--------------------------#
# ---------------------------------------------------#
# -------------------[HOW TO USE]--------------------#
# [Q], [R] increasing, decreasing RED color value----#
# [W], [S] increasing, decreasing GREEN color value--#
# [E], [D] increasing, decreasing BLUE color value---#
# ---------------------------------------------------#
__author__      = "github:didyoueatmybanana / sololearn:eterxoz"
__copyright__   = "Feel free to use, just mention me and leave + ^^"


def main():

    # initialize all pygame modules
    pygame.init()
    # -----------------------------

    # window size --
    size = 1000, 800
    # --------------

    # 1.creating window, 
    # 2.define clock, 
    # 3.define fps value, 
    # 4.define ticker(for printing text once per x frames (line 93))
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    fps = 30
    ticker = 0
    # --------------------------------------------------------------

    # color vars --------------
    r_col = rnd.randint(0, 255)
    g_col = rnd.randint(0, 255)
    b_col = rnd.randint(0, 255)
    # -------------------------

    

    while True:

        rgb_color = r_col, g_col, b_col  # assigning (r, g, b) values
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # close button
                pygame.quit()
                sys.exit()

        # red color control // [q] to increase, [a] to decrease
        if keys[pygame.K_q]:
            r_col += 1
            if r_col > 255:
                r_col = 255

        if keys[pygame.K_a]:
            r_col -= 1
            if r_col < 0:
                r_col = 0
        # ----------------------------------------------------

        # green color control // [w] to increase, [s] to decrease
        if keys[pygame.K_w]:
            g_col += 1
            if g_col > 255:
                g_col = 255

        if keys[pygame.K_s]:
            g_col -= 1
            if g_col < 0:
                g_col = 0
        # ----------------------------------------------------

        # blue color control // [k] to increase, [d] to decrease
        if keys[pygame.K_e]:
            b_col += 1
            if b_col > 255:
                b_col = 255

        if keys[pygame.K_d]:
            b_col -= 1
            if b_col < 0:
                b_col = 0
        # ----------------------------------------------------

        # printing rgb value once per 10frames ---------------
        if ticker == 0:
            ticker = 10
            print("Current rgb value is {}".format(rgb_color))
        if ticker > 0:
            ticker -= 1
        # -----------------------------------------------------

        screen.fill(rgb_color)  # filling the screen with current color
        pygame.display.flip()  # refreshing display
        clock.tick(fps)


main()
