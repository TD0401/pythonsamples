#write a program to show hello world with pyglet/pygame

#import  sys
#import pygame as pg

#pg.init()

#screen = pg.display.set_caption("Hello World")
#screen = pg.display.set_mode(size=(600,500))
#screen_rect= screen.get_rect()
#msg = "Hello World"
#f = pg.font.SysFont(None,48)
#msg_img = f.render(msg,True,color=(100,100,100), background=None)
#msg_img_rect = msg_img.get_rect()
#msg_img_centr= screen_rect.center
#screen.blit(msg_img, msg_img_rect)


#while True:
#    for event in pg.event.get():
#        if event.type== pg.QUIT:
#            sys.exit()
#        pg.display.flip()

import pyglet

window = pyglet.window.Window()

label = pyglet.text.Label("Hello World",font_name="Times New Roman",font_size=36,
                          x = window.width//2 , y = window.height //2, anchor_x='center' , anchor_y='center')
@window.event
def on_draw():
    window.clear()
    label.draw()

pyglet.app.run()