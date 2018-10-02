# -*- coding: utf-8 -*-
"""
Created on Thu May 24 16:34:58 2018

@author: admin
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.spatial.distance as sc
from scipy.cluster import hierarchy
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn import linear_model
from sklearn.metrics import (confusion_matrix, precision_score, recall_score,f1_score, accuracy_score)
from sklearn.feature_selection import VarianceThreshold
from sklearn import svm
from sklearn.preprocessing import PolynomialFeatures
from datetime import datetime, date, time, timedelta
import calendar
from sklearn.metrics import (confusion_matrix, precision_score, recall_score,f1_score, accuracy_score,precision_recall_fscore_support)
from tkinter import *
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image
from xlwt import Workbook


database_file = "inglaterra.xlsx"
database = pd.read_excel(database_file,
                         sheetname="07-13_06",
                         header=0,
                         index_col=None,
                         parse_dates=False)

minidatabase=database.iloc[:,[0,1,2,5]]

buche=[]
for i in np.arange(np.size(minidatabase["descripcion"])):
    if("BUCHE" in minidatabase.iloc[i,1]):
        buche.append(minidatabase.loc[i])
buche=pd.DataFrame(np.zeros([int(np.size(buche)/4),5]))
cont=0
for i in np.arange(np.size(minidatabase["descripcion"])):
    if("BUCHE" in minidatabase.iloc[i,1]):
        buche.iloc[cont,0]=(minidatabase.iloc[i,1])
        buche.iloc[cont,1]=(minidatabase.iloc[i,3])
        if("POZOLE" in minidatabase.iloc[i,1] ):
            if("CH" in minidatabase.iloc[i,1] ):
                buche.iloc[cont,2]=.114
            elif("MD" in minidatabase.iloc[i,1]):
                buche.iloc[cont,2]=.141
            else:
                buche.iloc[cont,2]=.282
        #elif("PITUFO"in minidatabase.iloc[i,1] or "SUSHIPITUFO"in minidatabase.iloc[i,1])):
         #   buche.iloc[cont,4]=1
        elif("TORTA" in minidatabase.iloc[i,1] or "SUSHITORTA"in minidatabase.iloc[i,1]):
            buche.iloc[cont,4]=1
            if("1/2 BUCHE" in minidatabase.iloc[i,1]):
                buche.iloc[cont,2]=.06
                
            else:
                buche.iloc[cont,2]=.12
        else:
            if("1/2 BUCHE" in minidatabase.iloc[i,1]):
                buche.iloc[cont,2]=.03
            else:
                buche.iloc[cont,2]=.06
        cont+=1
buche[3]=buche[1]*buche[2]
buche[4]=buche[1]*buche[4]

pancita=[]
for i in np.arange(np.size(minidatabase["descripcion"])):
    if("PANCITA" in minidatabase.iloc[i,1]):
        pancita.append(minidatabase.loc[i])
pancita=pd.DataFrame(np.zeros([int(np.size(pancita)/4),5]))
cont=0
for i in np.arange(np.size(minidatabase["descripcion"])):
    if("PANCITA" in minidatabase.iloc[i,1]):
        pancita.iloc[cont,0]=(minidatabase.iloc[i,1])
        pancita.iloc[cont,1]=(minidatabase.iloc[i,3])
        if("POZOLE" in minidatabase.iloc[i,1] ):
            if("CH" in minidatabase.iloc[i,1] ):
                pancita.iloc[cont,2]=.114
            elif("MD" in minidatabase.iloc[i,1]):
                pancita.iloc[cont,2]=.141
            else:
                pancita.iloc[cont,2]=.282
        elif("TORTA" in minidatabase.iloc[i,1] or "SUSHITORTA"in minidatabase.iloc[i,1]):
            pancita.iloc[cont,4]=1
            if("1/2 PANCITA" in minidatabase.iloc[i,1]):
                pancita.iloc[cont,2]=.06
            else:
                pancita.iloc[cont,2]=.12
        else:
            if("1/2 PANCITA" in minidatabase.iloc[i,1]):
                pancita.iloc[cont,2]=.03
            else:
                pancita.iloc[cont,2]=.06
        cont+=1
pancita[3]=pancita[1]*pancita[2]
pancita[4]=pancita[1]*pancita[4]

        
lengua=[]
for i in np.arange(np.size(minidatabase["descripcion"])):
    if("LENGUA" in minidatabase.iloc[i,1]):
        lengua.append(minidatabase.loc[i])
lengua=pd.DataFrame(np.zeros([int(np.size(lengua)/4),5]))
cont=0
for i in np.arange(np.size(minidatabase["descripcion"])):
    if("LENGUA" in minidatabase.iloc[i,1]):
        lengua.iloc[cont,0]=(minidatabase.iloc[i,1])
        lengua.iloc[cont,1]=(minidatabase.iloc[i,3])
        if("POZOLE" in minidatabase.iloc[i,1] ):
            if("CH" in minidatabase.iloc[i,1] ):
                lengua.iloc[cont,2]=.114
            elif("MD" in minidatabase.iloc[i,1]):
                lengua.iloc[cont,2]=.141
            else:
                lengua.iloc[cont,2]=.282
        elif("TORTA" in minidatabase.iloc[i,1] or "SUSHITORTA"in minidatabase.iloc[i,1]):
            lengua.iloc[cont,4]=1
            if("1/2 LENGUA" in minidatabase.iloc[i,1]):
                lengua.iloc[cont,2]=.06
            else:
                lengua.iloc[cont,2]=.12
        else:
            if("1/2 LENGUA" in minidatabase.iloc[i,1]):
                lengua.iloc[cont,2]=.03
            else:
                lengua.iloc[cont,2]=.06
        cont+=1
lengua[3]=lengua[1]*lengua[2]
lengua[4]=lengua[1]*lengua[4]

pierna=[]
for i in np.arange(np.size(minidatabase["descripcion"])):
    if("PIERNA" in minidatabase.iloc[i,1]):
        pierna.append(minidatabase.loc[i])
pierna=pd.DataFrame(np.zeros([int(np.size(pierna)/4),5]))
cont=0
for i in np.arange(np.size(minidatabase["descripcion"])):
    if("PIERNA" in minidatabase.iloc[i,1]):
        pierna.iloc[cont,0]=(minidatabase.iloc[i,1])
        pierna.iloc[cont,1]=(minidatabase.iloc[i,3])
        if("POZOLE" in minidatabase.iloc[i,1] ):
            if("CH" in minidatabase.iloc[i,1] ):
                pierna.iloc[cont,2]=.114
            elif("MD" in minidatabase.iloc[i,1]):
                pierna.iloc[cont,2]=.141
            else:
                pierna.iloc[cont,2]=.282
        elif("TORTA" in minidatabase.iloc[i,1] or "SUSHITORTA"in minidatabase.iloc[i,1]):
            pierna.iloc[cont,4]=1
            if("1/2 PIERNA" in minidatabase.iloc[i,1]):
                pierna.iloc[cont,2]=.06
            else:
                pierna.iloc[cont,2]=.12
        else:
            if("1/2 PIERNA" in minidatabase.iloc[i,1]):
                pierna.iloc[cont,2]=.03
            else:
                pierna.iloc[cont,2]=.06
        cont+=1
pierna[3]=pierna[1]*pierna[2]
pierna[4]=pierna[1]*pierna[4]

asada=[]
for i in np.arange(np.size(minidatabase["descripcion"])):
    if("ASADA" in minidatabase.iloc[i,1]):
        if("DORADITA VERDURAS ASADAS" in minidatabase.iloc[i,1] or "PANELA ASADA" in minidatabase.iloc[i,1] or "VERDURAS ASADAS" in minidatabase.iloc[i,1]):
            1+1
        else:
            asada.append(minidatabase.loc[i])
asada=pd.DataFrame(np.zeros([int(np.size(asada)/4),5]))
cont=0
for i in np.arange(np.size(minidatabase["descripcion"])):
    if("ASADA" in minidatabase.iloc[i,1]):
        if("DORADITA VERDURAS ASADAS" in minidatabase.iloc[i,1] or "PANELA ASADA" in minidatabase.iloc[i,1] or "VERDURAS ASADAS" in minidatabase.iloc[i,1]):
            1+1
        else:
            asada.iloc[cont,0]=(minidatabase.iloc[i,1])
            asada.iloc[cont,1]=(minidatabase.iloc[i,3])
            if("CHORIPAN" in minidatabase.iloc[i,1] or "PAPA" in minidatabase.iloc[i,1]):
                if("CHORIPAN" in minidatabase.iloc[i,1]):
                    asada.iloc[cont,4]=1
                if("1/2" in minidatabase.iloc[i,1] or "PITUFO" in minidatabase.iloc[i,1] ):
                    asada.iloc[cont,2]=.06
                else:
                    asada.iloc[cont,2]=.12
            else:
                if("1/2" in minidatabase.iloc[i,1]):
                    asada.iloc[cont,2]=.03
                else:
                    asada.iloc[cont,2]=.06
        cont+=1
asada[3]=asada[1]*asada[2]
asada[4]=asada[1]*asada[4]

arrachera=[]
for i in np.arange(np.size(minidatabase["descripcion"])):
    if("ARRACHERA" in minidatabase.iloc[i,1]):
        arrachera.append(minidatabase.loc[i])
arrachera=pd.DataFrame(np.zeros([int(np.size(arrachera)/4),5]))
cont=0
for i in np.arange(np.size(minidatabase["descripcion"])):
    if("ARRACHERA" in minidatabase.iloc[i,1]):
        arrachera.iloc[cont,0]=(minidatabase.iloc[i,1])
        arrachera.iloc[cont,1]=(minidatabase.iloc[i,3])
        if("CHORIPAN" in minidatabase.iloc[i,1] or "PAPA" in minidatabase.iloc[i,1]):
            if("CHORIPAN" in minidatabase.iloc[i,1]):
                arrachera.iloc[cont,4]=1
            if("1/2" in minidatabase.iloc[i,1] or "PITUFO" in minidatabase.iloc[i,1] ):
                arrachera.iloc[cont,2]=.06
            else:
                arrachera.iloc[cont,2]=.12
        else:
            if("1/2" in minidatabase.iloc[i,1]):
                arrachera.iloc[cont,2]=.03
            else:
                arrachera.iloc[cont,2]=.06
        cont+=1
arrachera[3]=arrachera[1]*arrachera[2]
arrachera[4]=arrachera[1]*arrachera[4]

chorizo=[]
for i in np.arange(np.size(minidatabase["descripcion"])):
    if("CHORIZO" in minidatabase.iloc[i,1]):
        chorizo.append(minidatabase.loc[i])
chorizo=pd.DataFrame(np.zeros([int(np.size(chorizo)/4),5]))
cont=0
for i in np.arange(np.size(minidatabase["descripcion"])):
    if("CHORIZO" in minidatabase.iloc[i,1]):
        chorizo.iloc[cont,0]=(minidatabase.iloc[i,1])
        chorizo.iloc[cont,1]=(minidatabase.iloc[i,3])
        if("CHORIPAN" in minidatabase.iloc[i,1] or "PAPA" in minidatabase.iloc[i,1]):
            if("CHORIPAN" in minidatabase.iloc[i,1]):
                chorizo.iloc[cont,4]=1
            if("1/2" in minidatabase.iloc[i,1] or "PITUFO" in minidatabase.iloc[i,1] ):
                chorizo.iloc[cont,2]=.06
            else:
                chorizo.iloc[cont,2]=.12
        else:
            if("1/2" in minidatabase.iloc[i,1]):
                chorizo.iloc[cont,2]=.03
            else:
                chorizo.iloc[cont,2]=.06
        cont+=1
chorizo[3]=chorizo[1]*chorizo[2]
chorizo[4]=chorizo[1]*chorizo[4]

marlin=[]
for i in np.arange(np.size(minidatabase["descripcion"])):
    if("MARLIN" in minidatabase.iloc[i,1]):
        marlin.append(minidatabase.loc[i])
marlin=pd.DataFrame(np.zeros([int(np.size(marlin)/4),5]))
cont=0
for i in np.arange(np.size(minidatabase["descripcion"])):
    if("MARLIN" in minidatabase.iloc[i,1]):
        marlin.iloc[cont,0]=(minidatabase.iloc[i,1])
        marlin.iloc[cont,1]=(minidatabase.iloc[i,3])
        if("TORTA" in minidatabase.iloc[i,1] or "PAPA" in minidatabase.iloc[i,1]):
            if("1/2" in minidatabase.iloc[i,1] or "PITUFO" in minidatabase.iloc[i,1] ):
                marlin.iloc[cont,2]=.06
            else:
                marlin.iloc[cont,2]=.12
        else:
            if("1/2" in minidatabase.iloc[i,1] or "GOBERNADOR CH" in minidatabase.iloc[i,1]):
                marlin.iloc[cont,2]=.03
            else:
                marlin.iloc[cont,2]=.06
        cont+=1
marlin[3]=marlin[1]*marlin[2]

camaron=[]
for i in np.arange(np.size(minidatabase["descripcion"])):
    if("CAMARON" in minidatabase.iloc[i,1]):
        camaron.append(minidatabase.loc[i])
camaron=pd.DataFrame(np.zeros([int(np.size(camaron)/4),5]))
cont=0
for i in np.arange(np.size(minidatabase["descripcion"])):
    if("CAMARON" in minidatabase.iloc[i,1]):
        camaron.iloc[cont,0]=(minidatabase.iloc[i,1])
        camaron.iloc[cont,1]=(minidatabase.iloc[i,3])
        if("TORTA" in minidatabase.iloc[i,1] or "PAPA" in minidatabase.iloc[i,1]):
            if("1/2" in minidatabase.iloc[i,1] or "PITUFO" in minidatabase.iloc[i,1] ):
                camaron.iloc[cont,2]=.06
            else:
                camaron.iloc[cont,2]=.12
        else:
            if("1/2" in minidatabase.iloc[i,1] or "GOBERNADOR CH" in minidatabase.iloc[i,1]):
                camaron.iloc[cont,2]=.03
            else:
                camaron.iloc[cont,2]=.06
        cont+=1
camaron[3]=camaron[1]*camaron[2]



#manchego=[]
#for i in np.arange(np.size(minidatabase["descripcion"])):
#    if("CAMARON" in minidatabase.iloc[i,1]):
#        camaron.append(minidatabase.loc[i])
#manchego=pd.DataFrame(np.zeros([int(np.size(manchego)/4),5]))
#cont=0
#for i in np.arange(np.size(minidatabase["descripcion"])):
#    if("CAMARON" in minidatabase.iloc[i,1]):
#        manchego.iloc[cont,0]=(minidatabase.iloc[i,1])
#        manchego.iloc[cont,1]=(minidatabase.iloc[i,3])
#        if("TORTA" in minidatabase.iloc[i,1] or "PAPA" in minidatabase.iloc[i,1]):
#            if("1/2" in minidatabase.iloc[i,1] or "PITUFO" in minidatabase.iloc[i,1] ):
#                manchego.iloc[cont,2]=.06
#            else:
#                manchego.iloc[cont,2]=.12
#        else:
#            if("1/2" in minidatabase.iloc[i,1] or "GOBERNADOR CH" in minidatabase.iloc[i,1]):
#                manchego.iloc[cont,2]=.03
#            else:
#                manchego.iloc[cont,2]=.06
#        cont+=1
#manchego[3]=manchego[1]*manchego[2]

suma_carnes=pd.DataFrame(np.zeros([1,9]))
suma_carnes[0]=np.sum(pierna[3])
suma_carnes[1]=np.sum(buche[3])
suma_carnes[2]=np.sum(pancita[3])
suma_carnes[3]=np.sum(lengua[3])
suma_carnes[4]=np.sum(arrachera[3])
suma_carnes[5]=np.sum(asada[3])
suma_carnes[6]=np.sum(chorizo[3])
suma_carnes[7]=np.sum(marlin[3])
suma_carnes[8]=np.sum(camaron[3])

suma_carnes.columns=["pierna","buche","pancita","lengua","arrachera","asada","chorizo","marlin","camaron"]

#%%
suma_bolillo=pd.DataFrame(np.zeros([1,5]))
bolillo=0
pitufo=0
papa=0
requeson=0
frijol=0
suma_aguas=pd.DataFrame(np.zeros([1,8]))
cebada=0
coco=0
guayaba=0
horchata=0
jamaica=0
limon=0
tamarindo=0
jazmin=0
suma_refrescos=pd.DataFrame(np.zeros([1,13]))
COCA=0
COCALATA=0
COCASINAZUCAR=0
COCALIGHTBOTELLA=0
COCALIGHTLATA=0
FANTA =0
FRESCA=0
MANZANA=0
SPRITE=0
SPRITELATA=0
SPRITEZERO=0
MINERAL=0
NATURAL=0

CORONA=0
CORONALATA=0
CORONALIGHT=0
CORONALIGHTLATA=0
MODELO=0
NEGRA=0
PACIFICO=0
VICTORIA=0


for i in np.arange(np.size(minidatabase["descripcion"])):
    if("TORTA" in minidatabase.iloc[i,1]):
        bolillo+=(minidatabase.iloc[i,3])
    if("PITUFO" in minidatabase.iloc[i,1]):
        pitufo+=(minidatabase.iloc[i,3])
    if("DORADO PAPA" in minidatabase.iloc[i,1]):
        papa+=(minidatabase.iloc[i,3])
    if("DORADO REQUESON" in minidatabase.iloc[i,1]):
        requeson+=(minidatabase.iloc[i,3])
    if("DORADO FRIJOL" in minidatabase.iloc[i,1]):
        frijol+=(minidatabase.iloc[i,3])
    if("CEBADA" in minidatabase.iloc[i,1]):
        cebada+=(minidatabase.iloc[i,3])
    if("COCO" in minidatabase.iloc[i,1]):
        coco+=(minidatabase.iloc[i,3])
    if("AGUA DE GUAYABA" in minidatabase.iloc[i,1]):
        guayaba+=(minidatabase.iloc[i,3])
    if("HORCHATA" in minidatabase.iloc[i,1]):
        horchata+=(minidatabase.iloc[i,3])
    if("JAMAICA" in minidatabase.iloc[i,1]):
        jamaica+=(minidatabase.iloc[i,3])
    if("AGUA DE LIMON" in minidatabase.iloc[i,1]):
        limon+=(minidatabase.iloc[i,3])
    if("TAMARINDO" in minidatabase.iloc[i,1]):
        tamarindo+=(minidatabase.iloc[i,3])
    if("JAZMIN" in minidatabase.iloc[i,1]):
        jazmin+=(minidatabase.iloc[i,3])
    if("COCA COLA BOTELLA" in minidatabase.iloc[i,1] or "CH COCA" in minidatabase.iloc[i,1]):
        COCA+=(minidatabase.iloc[i,3])
    if("GDE COCA" in minidatabase.iloc[i,1]):
        COCA+=2*(minidatabase.iloc[i,3])
    if("COCA COLA LATA" in minidatabase.iloc[i,1]):
        COCALATA+=(minidatabase.iloc[i,3])
    if("COCA COLA SIN AZUCAR" in minidatabase.iloc[i,1]):
        COCASINAZUCAR+=(minidatabase.iloc[i,3])
    if("COCA LIGHT BOTELLA" in minidatabase.iloc[i,1]):
        COCALIGHTBOTELLA+=(minidatabase.iloc[i,3])
    if("COCA LIGHT LATA" in minidatabase.iloc[i,1]):
        COCALIGHTLATA+=(minidatabase.iloc[i,3])
    if("FANTA" in minidatabase.iloc[i,1]):
        FANTA+=(minidatabase.iloc[i,3])
    if("JAZMIN" in minidatabase.iloc[i,1]):
        jazmin+=(minidatabase.iloc[i,3])
    if("FRESCA BOTELLA" in minidatabase.iloc[i,1] or "CH FRESCA" in minidatabase.iloc[i,1]):
        FRESCA+=(minidatabase.iloc[i,3])
    if("GDE FRESCA" in minidatabase.iloc[i,1]):
        FRESCA+=2*(minidatabase.iloc[i,3])
    if("MANZANA" in minidatabase.iloc[i,1]):
        MANZANA+=(minidatabase.iloc[i,3])
    if("SPRITE BOTELLA" in minidatabase.iloc[i,1] or "CH SPRITE" in minidatabase.iloc[i,1]):
        SPRITE+=(minidatabase.iloc[i,3])
    if("GDE SPRITE" in minidatabase.iloc[i,1]):
        SPRITE+=2*(minidatabase.iloc[i,3])
    if("SPRITE LATA" in minidatabase.iloc[i,1]):
        SPRITELATA+=(minidatabase.iloc[i,3])
    if("SPRITE ZERO" in minidatabase.iloc[i,1]):
        SPRITEZERO+=(minidatabase.iloc[i,3])
    if("AGUA NATURAL" in minidatabase.iloc[i,1]):
        NATURAL+=(minidatabase.iloc[i,3])
    if("AGUA MINERAL" in minidatabase.iloc[i,1] or "CH MINERAL" in minidatabase.iloc[i,1]):
        NATURAL+=(minidatabase.iloc[i,3])
    if("GDE MINERAL" in minidatabase.iloc[i,1]):
        MINERAL+=2*(minidatabase.iloc[i,3])
    if("CORONA" == minidatabase.iloc[i,1]):
        CORONA+=(minidatabase.iloc[i,3])
    if("CORONA" == minidatabase.iloc[i,1]):
        CORONA+=(minidatabase.iloc[i,3])

        
suma_bolillo.iloc[0,0]=bolillo
suma_bolillo.iloc[0,1]=pitufo
suma_bolillo.iloc[0,2]=requeson
suma_bolillo.iloc[0,3]=papa
suma_bolillo.iloc[0,4]=frijol

suma_aguas.iloc[0,0]=cebada
suma_aguas.iloc[0,1]=coco
suma_aguas.iloc[0,2]=guayaba
suma_aguas.iloc[0,3]=horchata
suma_aguas.iloc[0,4]=jamaica
suma_aguas.iloc[0,5]=limon
suma_aguas.iloc[0,6]=tamarindo
suma_aguas.iloc[0,7]=jazmin

suma_refrescos.iloc[0,0]=COCA
suma_refrescos.iloc[0,1]=COCALATA
suma_refrescos.iloc[0,2]=COCASINAZUCAR
suma_refrescos.iloc[0,3]=COCALIGHTBOTELLA
suma_refrescos.iloc[0,4]=COCALIGHTLATA
suma_refrescos.iloc[0,5]=FANTA
suma_refrescos.iloc[0,6]=FRESCA
suma_refrescos.iloc[0,7]=MANZANA
suma_refrescos.iloc[0,8]=SPRITE
suma_refrescos.iloc[0,9]=SPRITELATA
suma_refrescos.iloc[0,10]=SPRITEZERO
suma_refrescos.iloc[0,11]=MINERAL
suma_refrescos.iloc[0,12]=NATURAL


#agregar al rastreo manchego, philadelfia, panela, pollo, tortilla harina, vampiro, a mano

#cambiar esta receta tortilla vampiro en doraditas
#agregar a receta vampiro granulado .03
#cambiar receta papas, cambiar el peso de la papa



