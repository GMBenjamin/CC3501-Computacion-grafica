import pyglet
import numpy as np
from pyglet.gl import *
import random
import shader as bs
import resources as fig

main = pyglet.window.Window(caption="Naves en 2D \
dibujando curvas de Bèzier", resizable=False)

lienzo = pyglet.graphics.Batch()

main.set_size(480, 480)
pyglet.gl.glClearColor(0.1,0.1,0.3,1.0)
pyglet.gl.glEnable(GL_DEPTH_TEST)

VIEW=pyglet.math.Mat4() @ pyglet.math.Mat4.orthogonal_projection(-1.5,1.5,-1.5,1.5,1.5,-2)
bs.program["projection"]=VIEW 

def fdrawO(obj):
    obj.graph = bs.program.vertex_list_indexed(8,pyglet.gl.GL_TRIANGLES,[0,1,3, 3,1,2, 0,4,1, 1,4,5, 0,4,3, 3,4,7, 4,5,7, 7,5,6, 2,3,7, 2,6,7, 1,2,6, 1,5,6],
                                               position=("f",obj.ub_vertex), colors=("Bn",obj.col_vertex),batch=lienzo)
def fdrawN(obj):
    obj.graph = bs.program.vertex_list_indexed(7,pyglet.gl.GL_TRIANGLES,[0,1,2, 3,4,5, 1,4,6],
                                               position=("f",obj.ub_vertex), colors=("Bn",obj.col_vertex),batch=lienzo)
def redraw(obj):
    obj.graph.delete()
    obj.graph = bs.program.vertex_list_indexed(7,pyglet.gl.GL_TRIANGLES,[0,1,2, 3,4,5, 1,4,6],
                                               position=("f",obj.ub_vertex), colors=("Bn",obj.col_vertex),batch=lienzo)
def scene_generator():
    for j in range(0,75):
        fdrawO(fig.Obstacle(random.uniform(-1.6,1.6),random.uniform(-1.6,1.6),1.5,0.04))
    Player = [fig.Spaceship(0,0,1,0,0), fig.Spaceship(0.4,-0.4,0.5,0,0), fig.Spaceship(-0.4,-0.4,0.5,0,0)]
    for k in range(0,len(Player)):
        fdrawN(Player[k])
    return Player

Squad=scene_generator()

class Puntos_de_control:
    def __init__(self):
        self.p1 = []
        self.p2 = []
        self.p3 = []

C_points = Puntos_de_control()

class Bezier:
    def __init__(self):
        self.dibujado = False
        self.CG = None
        self.CD = None
        self.CI = None

    def dibujar(self,puntos):
        if self.dibujado == False:
            self.CG = pyglet.shapes.BezierCurve(*puntos.p1,t=1, segments=100, color=(70,255,250,255), batch=lienzo)
            self.CD = pyglet.shapes.BezierCurve(*puntos.p2,t=1, segments=100, color=(70,255,250,255), batch=lienzo)
            self.CI = pyglet.shapes.BezierCurve(*puntos.p3,t=1, segments=100, color=(70,255,250,255), batch=lienzo)
            self.dibujado = True
        else:
            self.CG.delete()
            self.CD.delete()
            self.CI.delete()
            self.CG = None
            self.CD = None
            self.CI = None
            self.dibujado = False

Curvas = Bezier()

@main.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.W:
        for i in range(0,len(Squad)):
            Squad[i].vel_loc = 0.02
    if symbol == pyglet.window.key.S:
        for i in range(0,len(Squad)):
            Squad[i].vel_loc = -0.02
    if symbol == pyglet.window.key.A:
        for i in range(0,len(Squad)):
            Squad[i].vAY = np.pi/45
    if symbol == pyglet.window.key.D:
        for i in range(0,len(Squad)):
            Squad[i].vAY = -np.pi/45
    if symbol == pyglet.window.key.R:
        C_points.p1.append((main.width//2 + Squad[0].gpos[0]*main.width//2,main.height//2 + Squad[0].gpos[1]*main.height//2))
        C_points.p2.append((main.width//2 + Squad[1].gpos[0]*main.width//2,main.height//2 + Squad[1].gpos[1]*main.height//2))
        C_points.p3.append((main.width//2 + Squad[2].gpos[0]*main.width//2,main.height//2 + Squad[2].gpos[1]*main.height//2))
    if symbol == pyglet.window.key.V:
        Curvas.dibujar(C_points)

@main.event
def on_key_release(symbol, modifiers):
    if symbol == pyglet.window.key.W:
        for i in range(0,len(Squad)):
            Squad[i].vel_loc = 0
    if symbol == pyglet.window.key.S:
        for i in range(0,len(Squad)):
            Squad[i].vel_loc = 0
    if symbol == pyglet.window.key.A:
        for i in range(0,len(Squad)):
            Squad[i].vAY = 0
    if symbol == pyglet.window.key.D:
        for i in range(0,len(Squad)):
            Squad[i].vAY = 0

@main.event
def on_draw():
    main.clear()
    lienzo.draw()
    for i in range(0,len(Squad)):
            Squad[i].Actualizar()
            redraw(Squad[i])

pyglet.app.run()
