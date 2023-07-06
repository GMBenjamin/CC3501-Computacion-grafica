import Lluvia_Shader as Sh #Es necesario tener Lluvia_Shader.py en la misma carpeta.
import pyglet
import random
from pyglet.gl import *

#Se crea la ventana con tamaño fijo.
main = pyglet.window.Window(caption="Simulador de lluvia", resizable=False)

#Se crea un batch.
lienzo = pyglet.graphics.Batch()

#Se fija el tamaño de la pantalla en (520x520)
main.set_size(520, 520)
pyglet.gl.glClearColor(0.6,0.6,0.6,1.0) #Se fija el color de fondo como un tono de gris.
pyglet.gl.glEnable(GL_DEPTH_TEST) #Se habilita el test de profundidad.
pyglet.gl.glEnable(GL_PROGRAM_POINT_SIZE) #Se habilita el uso del point_size.

P = pyglet.math.Vec3(0,0,2) #Vector position.
T = pyglet.math.Vec3(0,0,-1) #Vector target.
U = pyglet.math.Vec3(0,1,0) #Vector up.

#Se le entrega al shader una matriz de proyección en perspectiva.
Camara = pyglet.math.Mat4.look_at(P,T,U) @ \
         pyglet.math.Mat4.perspective_projection(1,-1,1,100)
Sh.program["projection"] = Camara
Sh.program["dropsize"] = 5.0 #El tamaño de las partículas es 5.

#La clase Gota son las partículas y su función de actualización.
class Gota:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        self.v = -0.02
        self.position = (self.x,self.y,self.z)
        self.color = (0.2, 0.9, 1, 1)
        self.objeto = Sh.program.vertex_list(1,pyglet.gl.GL_POINTS,\
                                             position=("f",self.position),\
                                             colors=("f",self.color),\
                                             batch=lienzo)

    def actualizar(self):
        self.y += self.v
        self.position = (self.x,self.y,self.z)
        if self.y <= -1:
            self.x = random.uniform(-1,1)
            self.z = random.uniform(-1,1)
            self.y = 1
            self.position = (self.x,self.y,self.z)
        self.objeto.delete()
        self.objeto = Sh.program.vertex_list(1,pyglet.gl.GL_POINTS,\
                                             position=("f",self.position),\
                                             colors=("f",self.color),\
                                             batch=lienzo)

#Se crea un conjunto de gotas (Nubada)
Nubada = []
#Se usan 500 partículas.
for i in range(0,500):
    Nubada.append(Gota(random.uniform(-1,1),\
                       random.uniform(-1,1),random.uniform(-1,1)))

#Se crea un suelo y un árbol (tronco y copa).
Suelo_vertex = (-2,-1,-2, -2,-1,2, 2,-1,2, 2,-1,-2)
Suelo_color = (0.1,0.5,0,1, 0.1,0.5,0,1, 0.1,0.5,0,1, 0.1,0.5,0,1)
Suelo = Sh.program.vertex_list_indexed(4,\
                                       pyglet.gl.GL_TRIANGLES,\
                                       [0,1,2, 0,2,3],\
                                       position=("f",Suelo_vertex),\
                                       colors=("f",Suelo_color), batch=lienzo)

Tronco_vertex = (-0.4,-0.6,-0.8, -0.4,-1,-0.8, -0.3,-1,-0.8, -0.3,-0.6,-0.8)
Tronco_color = (0.4,0.3,0,1, 0.4,0.3,0,1, 0.4,0.3,0,1, 0.4,0.3,0,1)
Tronco = Sh.program.vertex_list_indexed(4,\
                                       pyglet.gl.GL_TRIANGLES,\
                                       [0,1,2, 0,2,3],\
                                       position=("f",Tronco_vertex),\
                                       colors=("f",Tronco_color), batch=lienzo)

Copa_vertex = (-0.6,0,-0.8, -0.6,-0.6,-0.8, -0.1,-0.6,-0.8, -0.1,0,-0.8)
Copa_color = (0.1,0.5,0,1, 0.1,0.5,0,1, 0.1,0.5,0,1, 0.1,0.5,0,1)
Copa = Sh.program.vertex_list_indexed(4,\
                                       pyglet.gl.GL_TRIANGLES,\
                                       [0,1,2, 0,2,3],\
                                       position=("f",Copa_vertex),\
                                       colors=("f",Copa_color), batch=lienzo)

@main.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.S:
         #presionar S transforma la lluvia en nieve y viceversa.
        for k in range(0,len(Nubada)):
            if Nubada[k].color == (0.2, 0.9, 1, 1):
                Nubada[k].color = (1, 1, 1, 1)
                Nubada[k].v = -0.01
            else:
                Nubada[k].color = (0.2, 0.9, 1, 1)
                Nubada[k].v = -0.02
    if symbol == pyglet.window.key.L:
         #La L encoge las partículas.
        Sh.program["dropsize"] = 3.0
    if symbol == pyglet.window.key.H:
         #La C agranda las partículas.
        Sh.program["dropsize"] = 7.0
    if symbol == pyglet.window.key.N:
         #La N devuelve las partículas al tamaño inicial.
        Sh.program["dropsize"] = 5.0

@main.event
def on_draw():
    main.clear() #Limpia la ventana.
    lienzo.draw() #Dibuja el batch.
    for j in range(0,len(Nubada)):
        Nubada[j].actualizar() #Actualiza las posiciones de las gotas.

pyglet.app.run() #Se ejecuta la aplicación.
