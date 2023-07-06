import pyglet
from pyglet.gl import *
import random

#main es la ventana de pyglet que se abre al ejecutar el programa.
main = pyglet.window.Window(caption="Proyecto Naves 2D", resizable=False)
#caption es el título de la ventana.
#No se puede cambiar el tamaño de la ventana (resizable=False)

#Lienzo es un batch, esto permite dibujar varias cosas a la vez.
Lienzo = pyglet.graphics.Batch()

#Se fija el tamaño de la pantalla de la forma (ancho x alto)
main.set_size(480, 640)
#Se fija un color de fondo para los espacios vacíos de la ventana.
#Este color es una tonalidad de azul oscuro similar a (26, 26, 77).
pyglet.gl.glClearColor(0.1,0.1,0.3,1.0)

#Estos grupos de objetos permite dar prioridad a lo que se ve en pantalla.
fondo = pyglet.graphics.Group(0)
naves = pyglet.graphics.Group(1)
#Las figuras que pertenecen a "naves" se dibujan por arriba de "fondo".

#Las siguientes figuras forman a la nave nodriza.
Cuerpo = pyglet.shapes.Polygon((235,220),(235,300),(240,330),(245,300),
                                (245,220),color=(200,200,200),
                                batch=Lienzo,group=naves)
Ala_izq = pyglet.shapes.Polygon((235,300),(195,220),(215,210),
                                (225,220),(235,220),color=(255,255,255),
                                batch=Lienzo,group=naves)
Ala_der = pyglet.shapes.Polygon((245,300),(285,220),(265,210),(255,220),
                                 (245,220),color=(255,255,255),
                                 batch=Lienzo,group=naves)
Prop = pyglet.shapes.Rectangle(225,210,30,10, color=(255,120,30),
                                    batch=Lienzo,group=naves)

#Las siguientes figuras forman la nave del costado izquierdo.
Mini_c_izq = pyglet.shapes.Polygon((100,110),(100,158),(103,182),(106,158)
                                    ,(106,110),color=(200,200,200),
                                    batch=Lienzo,group=naves)
Mini_ai_izq = pyglet.shapes.Polygon((100,158),(100,110),(94,110),(88,104),
                                     (76,110),color=(255,255,255),
                                     batch=Lienzo,group=naves)
Mini_ad_izq = pyglet.shapes.Polygon((106,158),(106,110),(130,110),(118,104),
                                     (112,110),color=(255,255,255),batch=Lienzo,
                                     group=naves)
Mini_p_izq = pyglet.shapes.Rectangle(94,104,18,6, color=(255,120,30),
                                      batch=Lienzo,group=naves)

#Las siguientes figuras forman la nave del costado derecho.
Mini_c_der = pyglet.shapes.Polygon((380,110),(380,158),(383,182),(386,158),
                                   (386,110),color=(200,200,200),
                                     batch=Lienzo,group=naves)
Mini_ai_der = pyglet.shapes.Polygon((380,158),(380,110),(372,110),(366,104),
                                    (354,110),color=(255,255,255),
                                    batch=Lienzo,group=naves)
Mini_ad_der = pyglet.shapes.Polygon((386,158),(386,110),(392,110),(398,104),
                                    (410,110),color=(255,255,255),
                                    batch=Lienzo,group=naves)
Mini_p_der = pyglet.shapes.Rectangle(374,104,18,6, color=(255,120,30),
                                      batch=Lienzo,group=naves)

#La función posiciones entrega una posición aleatoria para el eje x.
def posiciones():
    x_pos = random.randint(0,480)
    return x_pos

#La función generador crea estrellas de fondo, en lotes de 1 a 5 estrellas.
def generador():
    estrellas = []
    for i in range(random.randint(1,5)):
        estrellita = pyglet.shapes.Star(posiciones(),680,10,6,5,
                                        rotation=0,color=(255,225,45),
                                        batch=Lienzo,group=fondo)
        estrellas.append(estrellita)
    return estrellas

#Se define un conjunto de estrellas.
conjunto_estrella=generador()

#La función starter crea 70 estrellas en ubicaciones aleatorias.
#Esto solo se ejecuta al iniciar el programa.
def starter():
    stars = []
    for i in range(0,70):
        Inicial = pyglet.shapes.Star(posiciones(),random.randint(0,670),
                                      10,6,5,rotation=0,color=(255,225,45),
                                        batch=Lienzo,group=fondo)
        stars.append(Inicial)
    conjunto_estrella.extend(stars)

starter()       

#La función movimiento es la que mueve las estrellas.
def movimiento():
    for i in range(0,len(conjunto_estrella)):
        conjunto_estrella[i].y-=5

#La función checker destruye las estrellas que ya no son visibles.
def checker():
    for i in range (0,10):
        if conjunto_estrella[i].y<=0:
            conjunto_estrella.remove(conjunto_estrella[i])

#La función update llama al generador para ir creando nuevas estrellas.
def update(dt):
    conjunto_estrella.extend(generador())

#La función update se ejecuta en cada décima de segundo (10Hz).    
pyglet.clock.schedule_interval(update, 1/10.0)

#A continuación, se actualiza la pantalla.        
@main.event
def on_draw():
    main.clear() #Se limpia la ventana.
    Lienzo.draw() #Se dibujan los objetos del lienzo.
    movimiento() #Se ejecuta el movimiento de las estrellas.
    checker() #Se revisa la visibilidad de las estrellas.

pyglet.app.run() #Se ejecuta la aplicación.
