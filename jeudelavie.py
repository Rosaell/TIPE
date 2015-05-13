# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 16:10:37 2015

@author: rosaell
"""
#import random
from Tkinter import *

#Definition des evenements clics droit et gauche

def clic_gauche(event):
    x = event.x -(event.x%c)
    y = event.y -(event.y%c)
    can.create_rectangle(x, y, x+c, y+c, fill='black')
    dico_c[x,y]=1

def clic_droit(event):
    x = event.x -(event.x%c)
    y = event.y -(event.y%c)
    can.create_rectangle(x, y, x+c, y+c, fill='white')
    dico_c[x,y]=0

#generation de la grille:

def grilleGen():
    x = 0
    y = 0
    
    while x < LAR:
        can.create_line(x, 0, x, LAR, width=1, fill="black")
        x+=c
    while y < LON:
        can.create_line(0, y, LON, y, width=1, fill="black")
        y+=c
        

#Commandes des boutons :

def go():
    global bPause
    if bPause == 1:
        bPause = 0
        play()

def pause():
    global bPause
    bPause = 1

#Le jeu : on compte les cs autour et on redessine

def play():
    global bPause, vitesse
    
    for i in range(LAR/c):
        for j in range(LON/c):
            x = i*c
            y = j*c
            nbViv = 0
            
            #Cas des coins
            if x==0 and y==0: 
                if dico_c[x+c, y] == 1:
                    nbViv+=1
                if dico_c[x, y+c] == 1:
                    nbViv+=1
                if dico_c[x+c, y+c]==1:
                    nbViv+=1
            
            elif x==0 and y==LON-c:
                if dico_c[x, y-c] == 1:
                    nbViv+=1
                if dico_c[x+c, y] == 1:
                    nbViv+=1
                if dico_c[x+c, y-c] == 1:
                    nbViv+=1
            
            elif x==LAR-c and y==0:
                if dico_c[x-c, y] == 1:
                    nbViv+=1
                if dico_c[x, y+c] == 1:
                    nbViv+=1
                if dico_c[x-c, y+c] == 1:
                    nbViv+=1
            
            elif x==LAR-c and y==LON-c:
                if dico_c[x-c, y] == 1:
                    nbViv+=1
                if dico_c[x, y-c] == 1:
                    nbViv+=1
                if dico_c[x-c, y-c] == 1:
                    nbViv+=1
            
            #Cas des bords
            elif x==0 and 0<y<int(LON-c): 
                if dico_c[x, y-c]==1:
                    nbViv+=1
                if dico_c[x, y+c]==1:
                    nbViv+=1
                if dico_c[x+c, y-c]==1:
                    nbViv+=1
                if dico_c[x+c, y]==1:
                    nbViv+=1
                if dico_c[x+c, y+c]==1:
                    nbViv+=1
                
            elif x==int(LAR-c) and 0<y<int(LON-c):
                if dico_c[x-c, y-c]==1:
                    nbViv+=1
                if dico_c[x-c, y]==1:
                    nbViv+=1
                if dico_c[x-c, y+c]==1:
                    nbViv+=1
                if dico_c[x, y-c]==1:
                    nbViv+=1
                if dico_c[x, y+c]==1:
                    nbViv+=1

            elif 0<x<int(LAR-c) and y==0:
                if dico_c[x-c, y]==1:
                    nbViv+=1
                if dico_c[x-c, y+c]==1:
                    nbViv+=1
                if dico_c[x, y+c]==1:
                    nbViv+=1
                if dico_c[x+c, y]==1:
                    nbViv+=1
                if dico_c[x+c, y+c]==1:
                    nbViv+=1

            elif 0<x<int(LAR-c) and y==int(LON-c):
                if dico_c[x-c, y-c]==1:
                    nbViv+=1
                if dico_c[x-c, y]==1:
                    nbViv+=1
                if dico_c[x, y-c]==1:
                    nbViv+=1
                if dico_c[x+c, y-c]==1:
                    nbViv+=1
                if dico_c[x+c, y]==1:
                    nbViv+=1
            
            #le reste
            else:
                if dico_c[x-c, y-c]==1:
                    nbViv+=1
                if dico_c[x-c, y]==1:
                    nbViv+=1
                if dico_c[x-c, y+c]==1:
                    nbViv+=1
                if dico_c[x, y-c]==1:
                    nbViv+=1
                if dico_c[x, y+c]==1:
                    nbViv+=1
                if dico_c[x+c, y-c]==1:
                    nbViv+=1
                if dico_c[x+c, y]==1:
                    nbViv+=1
                if dico_c[x+c, y+c]==1:
                    nbViv+=1
            
            dico_etat[x, y] = nbViv
    redessiner()
    
    if bPause == 0:
        fen.after(vitesse, play) #on relance play apres 'vitesse' ms

def redessiner():
    can.delete(ALL)
    grilleGen()
    
    for i in range(LAR/c):
        for j in range(LON/c):
            x = i*c
            y = j*c
            
            if dico_etat[x, y] == 3:
                dico_c[x, y] = 1
                can.create_rectangle(x, y, x+c, y+c, fill='black');
            elif dico_etat[x, y] == 2 and dico_c[x, y] == 1:
                can.create_rectangle(x, y, x+c, y+x, fill='black');
            else:
                dico_c[x, y] = 0
                can.create_rectangle(x, y, x+c, y+c, fill='white')
c = 10
LAR = 500
LON = 500

bPause = 1
vitesse = 50

dico_c = {}
dico_etat = {}

for i in range(LAR/c):
    for j in range(LON/c):
        x = i*c
        y = j*c
        
        dico_c[x, y] = 0


fen = Tk()
can = Canvas(fen, width=LAR, height=LON, bg='white')
can.bind("<Button-1>", clic_gauche)
can.bind("<Button-2>", clic_droit)
can.pack(side=TOP, padx=5, pady=5)

b1 = Button(fen, text="Go", command=go)
b2 = Button(fen, text="Pause", command=pause)
b1.pack(side=LEFT, padx=3, pady=3)
b2.pack(side=LEFT, padx=3, pady=3)

grilleGen()

fen.mainloop()
