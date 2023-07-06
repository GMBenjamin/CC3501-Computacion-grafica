import numpy as np

class Spaceship:
    def __init__(self,x_pos,y_pos,escala,vloc,vang_y):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.sz = escala
        self.vAY = 0
        self.rotY = 0
        self.vel_loc = vloc
        self.xv = -self.vel_loc*np.sin(self.rotY)
        self.yv = self.vel_loc*np.cos(self.rotY)
        self.gpos = (self.x_pos,self.y_pos)
        self.orientacion = [-np.sin(self.rotY),np.cos(self.rotY)]
        self.ub_vertex = (self.x_pos-0.1*self.sz,self.y_pos-0.1*self.sz,0, self.x_pos-0.2*self.sz,self.y_pos,0, self.x_pos-0.1*self.sz,self.y_pos,0,
                          self.x_pos+0.1*self.sz,self.y_pos-0.1*self.sz,0, self.x_pos+0.2*self.sz,self.y_pos,0, self.x_pos+0.1*self.sz,self.y_pos,0,
                          self.x_pos,self.y_pos+0.5*self.sz,0)
        self.col_vertex = (255, 0, 0, 255,  255, 255, 255, 255,  255, 255, 255, 255,
                           0, 255, 0, 255,  255, 255, 255, 255,  255, 255, 255, 255,
                           255,255,255,255)

        self.graph = None
    
    def Actualizar(self):
        self.rotY += self.vAY
        self.xv = -self.vel_loc*np.sin(self.rotY)
        self.yv = self.vel_loc*np.cos(self.rotY)
        self.x_pos += self.xv
        self.y_pos += self.yv
        self.gpos = (self.x_pos,self.y_pos)
        self.orientacion = [-np.sin(self.rotY),np.cos(self.rotY)]
        self.ub_vertex=(self.x_pos-0.1*(self.sz)*np.sqrt(2)*np.cos(self.rotY+np.pi/4),self.y_pos-0.1*(self.sz)*np.sqrt(2)*np.sin(self.rotY+np.pi/4),0,
                        self.x_pos-0.2*(self.sz)*np.cos(self.rotY),self.y_pos-0.2*(self.sz)*np.sin(self.rotY),0,
                        self.x_pos-0.1*(self.sz)*np.cos(self.rotY),self.y_pos-0.1*(self.sz)*np.sin(self.rotY),0,
                        self.x_pos+0.1*(self.sz)*np.sqrt(2)*np.sin(self.rotY+np.pi/4),self.y_pos-0.1*(self.sz)*np.sqrt(2)*np.cos(self.rotY+np.pi/4),0,
                        self.x_pos+0.2*(self.sz)*np.cos(self.rotY),self.y_pos+0.2*(self.sz)*np.sin(self.rotY),0,
                        self.x_pos+0.1*(self.sz)*np.cos(self.rotY),self.y_pos+0.1*(self.sz)*np.sin(self.rotY),0,
                        self.x_pos-0.5*(self.sz)*np.sin(self.rotY),self.y_pos+0.5*(self.sz)*np.cos(self.rotY),0)
        
class Obstacle:
    def __init__(self,X,Y,Z,escala):
        self.X = X
        self.Y = Y
        self.Z = Z
        self.S = escala
        self.ub_vertex =(self.X-0.5*self.S,self.Y+0.5*self.S,self.Z-0.5*self.S, self.X-0.5*self.S,self.Y+0.5*self.S,self.Z+0.5*self.S,
                                                                 self.X+0.5*self.S,self.Y+0.5*self.S,self.Z+0.5*self.S, self.X+0.5*self.S,self.Y+0.5*self.S,self.Z-0.5*self.S,
                                                                 self.X-0.5*self.S,self.Y-0.5*self.S,self.Z-0.5*self.S, self.X-0.5*self.S,self.Y-0.5*self.S,self.Z+0.5*self.S,
                                                                 self.X+0.5*self.S,self.Y-0.5*self.S,self.Z+0.5*self.S, self.X+0.5*self.S,self.Y-0.5*self.S,self.Z-0.5*self.S)
        self.col_vertex =(255,250,140,255, 255,250,140,255, 255,250,140,255, 255,250,140,255,
                                                                255,250,140,255, 255,250,140,255, 255,250,140,255, 255,250,140,255)
        self.graph = None
