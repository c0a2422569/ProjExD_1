import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img_trans = pg.transform.flip(bg_img, True, False)
    img3 = pg.image.load("fig/3.png")
    img3 = pg.transform.flip(img3,True,False)
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [-tmr, 0])
        screen.blit(bg_img_trans, [1600-tmr, 0])
        screen.blit(bg_img, [3200-tmr, 0])
        screen.blit(img3, [300, 200])


        pg.display.update()
        tmr += 1
        if tmr >= 3200:tmr = 0
        clock.tick(200)

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()