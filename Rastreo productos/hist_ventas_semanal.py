# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 16:39:59 2018

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
import string
import scipy.stats as st 


xls = pd.ExcelFile('tepeyac.xlsx')
xls.sheet_names
sheet_to_df_map = {}

for sheet_name in xls.sheet_names:
    sheet_to_df_map[sheet_name] = xls.parse(sheet_name)


dates=(["17-24_05","24-30_05","31-06_06"])
for fecha in dates:
    sheet_to_df_map[fecha]=sheet_to_df_map[fecha].set_index("descripcion")
for producto in productos["descripcion"]:
    temp=[]
    for fecha in dates:
        if(producto in sheet_to_df_map[fecha].index):
            temp.append(sheet_to_df_map[fecha].loc[producto]["cantidad"])
        else:
            temp.append(0)
    plt.title(producto)
    plt.plot(dates,temp)
    plt.show()
            