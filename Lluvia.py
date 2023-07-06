import Lluvia_Shader as Sh
import pyglet
import random
from pyglet.gl import *

main = pyglet.window.Window(caption="Simulador de lluvia", resizable=False)

lienzo = pyglet.graphics.Batch()

main.set_size(520, 520)
pyglet.gl.glClearColor(0.6,0.6,0.6,1.0)
pyglet.gl.glEnable(GL_DEPTH_TEST)
pyglet.gl.glEnable(GL_PROGRAM_POINT_SIZE)

P = pyglet.math.Vec3(0,0,2)
T = pyglet.math.Vec3(0,0,-1)
U = pyglet.math.Vec3(0,1,0)
Camara = pyglet.math.Mat4.look_at(P,T,U) @ \
         pyglet.math.Mat4.perspective_projection(1,-1,1,100)
Sh.program["projection"] = Camara
Sh.program["dropsize"] = 5.0

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

Nubada = []
for i in range(0,500):
    Nubada.append(Gota(random.uniform(-1,1),\
                       random.uniform(-1,1),random.uniform(-1,1)))

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
        for k in range(0,len(Nubada)):
            if Nubada[k].color == (0.2, 0.9, 1, 1):
                Nubada[k].color = (1, 1, 1, 1)
                Nubada[k].v = -0.01
            else:
                Nubada[k].color = (0.2, 0.9, 1, 1)
                Nubada[k].v = -0.02
    if symbol == pyglet.window.key.L:
        Sh.program["dropsize"] = 3.0
    if symbol == pyglet.window.key.H:
        Sh.program["dropsize"] = 7.0
    if symbol == pyglet.window.key.N:
        Sh.program["dropsize"] = 5.0

@main.event
def on_draw():
    main.clear()
    lienzo.draw()
    for j in range(0,len(Nubada)):
        Nubada[j].actualizar()

pyglet.app.run()
