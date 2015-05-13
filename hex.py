# -*- coding: utf-8 -*-
"""
Created on Thu May  7 11:44:41 2015

Generation du maillage hexagonal

@author: rosaell
"""

from Tkinter import *
import math

rac3 = math.sqrt(3)

a = 15 #Arete de l'hexagone
nH = 20 #Nombre sur une colonne
nW = 20 #Nombre sur une ligne

h=nH*a*rac3
w=(nW/2)*3*a

fen = Tk()
can = Canvas(fen, width=w, height=h, bg='white')


for i in range(nW):
    for j in range(nH):
        if i%2 == 0:
            points=[(1.5*a*i + a/2, j*a*rac3),(1.5*a*i + 3*a/2, j*a*rac3),(1.5*a*i + 2*a, j*a*rac3 + a*rac3/2),(1.5*a*i + 3*a/2, j*a*rac3 + a*rac3),(1.5*a*i + a/2, j*a*rac3 + a*rac3),(1.5*a*i, j*a*rac3 + a*rac3/2)]
        elif i%2 == 1:
            points=[(1.5*a*(i-1) + 2*a, j*a*rac3 + a*rac3/2),(1.5*a*(i-1) + 3*a, j*a*rac3 + a*rac3/2),(1.5*a*(i-1) + 7*a/2, (j+1)*a*rac3),(1.5*a*(i-1) + 3*a, j*a*rac3 + 3*a*rac3/2),(1.5*a*(i-1) + 2*a, j*a*rac3 + 3*a*rac3/2),(1.5*a*(i-1) + 3*a/2, (j+1)*a*rac3)]
        
        can.create_polygon(points, fill='white', outline='black')
        
can.pack(side=TOP, padx=5, pady=5)
fen.mainloop()
