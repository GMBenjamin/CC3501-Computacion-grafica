import pyglet
from pyglet.gl import *
import random

main = pyglet.window.Window(caption="Proyecto Naves 2D", resizable=False)

Lienzo = pyglet.graphics.Batch()

main.set_size(480, 640)
pyglet.gl.glClearColor(0.1,0.1,0.3,1.0)

fondo = pyglet.graphics.Group(0)
naves = pyglet.graphics.Group(1)

Cuerpo = pyglet.shapes.Rectangle(235,220,10,80, color=(200,200,200),
                                 batch=Lienzo, group=naves)
Punta = pyglet.shapes.Triangle(235,300,245,300,240,330,
                               color=(200,200,200),batch=Lienzo,group=naves)
Ala_izq = pyglet.shapes.Triangle(235,300,195,220,235,220,
                                 color=(255,255,255), batch=Lienzo,group=naves)
Ala_der = pyglet.shapes.Triangle(245,300,285,220,245,220,
                                 color=(255,255,255), batch=Lienzo,group=naves)
Prop_izq = pyglet.shapes.Triangle(195,220,215,210,225,220,
                                 color=(255,255,255), batch=Lienzo,group=naves)
Prop_der = pyglet.shapes.Triangle(285,220,265,210,255,220,
                                  color=(255,255,255), batch=Lienzo,group=naves)
Prop_c = pyglet.shapes.Rectangle(225,210,30,10, color=(255,120,30),
                                    batch=Lienzo,group=naves)

Mini_c_izq = pyglet.shapes.Rectangle(100,110,6,48,color=(200,200,200),
                                     batch=Lienzo,group=naves)
Mini_p_izq = pyglet.shapes.Triangle(100,158,106,158,103,182,
                                    color=(200,200,200),batch=Lienzo,group=naves)
Mini_ai_izq = pyglet.shapes.Triangle(100,158,100,110,76,110,
                                     color=(255,255,255),batch=Lienzo,group=naves)
Mini_ad_izq = pyglet.shapes.Triangle(106,158,106,110,130,110,
                                     color=(255,255,255),batch=Lienzo,group=naves)
Mini_pi_izq = pyglet.shapes.Triangle(76,110,88,104,94,110,
                                     color=(255,255,255),batch=Lienzo,group=naves)
Mini_pd_izq = pyglet.shapes.Triangle(130,110,118,104,112,110,
                                     color=(255,255,255),batch=Lienzo,group=naves)
Mini_mp_izq = pyglet.shapes.Rectangle(94,104,18,6, color=(255,120,30),
                                      batch=Lienzo,group=naves)

Mini_c_der = pyglet.shapes.Rectangle(380,110,6,48,color=(200,200,200),
                                     batch=Lienzo,group=naves)
Mini_p_der = pyglet.shapes.Triangle(380,158,386,158,383,182,
                                    color=(200,200,200),batch=Lienzo,group=naves)
Mini_ai_der = pyglet.shapes.Triangle(380,158,380,110,354,110,
                                     color=(255,255,255),batch=Lienzo,group=naves)
Mini_ad_der = pyglet.shapes.Triangle(386,158,386,110,410,110,
                                     color=(255,255,255),batch=Lienzo,group=naves)
Mini_pi_der = pyglet.shapes.Triangle(354,110,366,104,372,110,
                                     color=(255,255,255),batch=Lienzo,group=naves)
Mini_pd_der = pyglet.shapes.Triangle(410,110,398,104,392,110,
                                     color=(255,255,255),batch=Lienzo,group=naves)
Mini_mp_der = pyglet.shapes.Rectangle(374,104,18,6, color=(255,120,30),
                                      batch=Lienzo,group=naves)

def posiciones():
    x_pos = random.randint(0,480)
    return x_pos

def generador():
    estrellas = []
    for i in range(random.randint(1,5)):
        estrellita = pyglet.shapes.Star(posiciones(),680,10,6,5,
                                        rotation=0,color=(255,225,45),
                                        batch=Lienzo,group=fondo)
        estrellas.append(estrellita)
    return estrellas

conjunto_estrella=generador()

def starter():
    stars = []
    for i in range(0,70):
        Inicial = pyglet.shapes.Star(posiciones(),random.randint(0,670),
                                      10,6,5,rotation=0,color=(255,225,45),
                                        batch=Lienzo,group=fondo)
        stars.append(Inicial)
    conjunto_estrella.extend(stars)

starter()       

def movimiento():
    for i in range(0,len(conjunto_estrella)):
        conjunto_estrella[i].y-=5

def checker():
    for i in range (0,10):
        if conjunto_estrella[i].y<=0:
            conjunto_estrella.remove(conjunto_estrella[i])

def update(dt):
    conjunto_estrella.extend(generador())
    
pyglet.clock.schedule_interval(update, 1/10.0)
        
@main.event
def on_draw():
    main.clear()
    Lienzo.draw()
    movimiento()
    checker()

pyglet.app.run()
