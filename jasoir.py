# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 11:00:23 2022

@author: rania
"""

import tkinter as tk
import os 
import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pandas import DataFrame
import math as m
import matplotlib.animation as animation

import internal_clock

####datamini

initial_price = 5 
min_price = 3
global beers_bought_delta
beers_bought_delta = 5


# ###dataarrays
# global prices_array
# prices_array=np.zeros(150)
# prices_array[0]=initial_price
#
# for i in range(1,len(prices_array)):
#     prices_array[i]=prices_array[0]-m.log(i)/5
#
# time = np.array([0, 18000], dtype='datetime64[s]')
#
# time2=np.linspace(0,300,300,dtype='datetime64[m]')
# time3 = []
# for i in range(0,len(time2)//2):
#     time3.append(time2[2*i])
# print(len(time3))
#
# print(time2)
# data2 = {'Temps': time3,
#          'Prix': prices_array,
#         }
# global df2
# df2 = DataFrame(data2,columns=['Temps','Prix'])




# def add():
#     global beers_bought_delta
#     beers_bought_delta +=1
#     print(beers_bought_delta)
#     update(frame,df2)
#
#
# def reset():
#     global beers_bought_delta
#     frame.destroy()
#     beers_bought_delta=0
#     print(beers_bought_delta)
#     frame2 = tk.Frame(root,bg="white")
#     frame2.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)
#     label=tk.Label(frame2,text=beers_bought_delta)
#     label.pack()
#
#
# def update(frame,df2):
#     frame = tk.Frame(root,bg="red")
#     frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)
#     label=tk.Label(frame,text=beers_bought_delta)
#     label.pack()
#     figure2 = plt.Figure(figsize=(5,4), dpi=100)
#     ax2 = figure2.add_subplot(111)
#     line2 = FigureCanvasTkAgg(figure2, frame)
#     line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
#     print(df2)
#     df2=reindex(df2)
#     df2 = df2[['Temps','Prix']].groupby('Temps').sum()
#     df2.plot(kind='line', legend=True, ax=ax2, color='r',marker='o', fontsize=10)
#
#
# ###initialize
# root = tk.Tk()
# canvas = tk.Canvas(root,height=700,width=700,bg="#345D41")
#
# canvas.pack()
# frame = tk.Frame(root,bg="white")
# frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)
# label=tk.Label(frame,text=beers_bought_delta)
# label.pack()
# figure2 = plt.Figure(figsize=(5,4), dpi=100)
# ax2 = figure2.add_subplot(111)
# line2 = FigureCanvasTkAgg(figure2, frame)
# line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
# df2 = df2[['Temps','Prix']].groupby('Temps').sum()
# df2.plot(kind='line', legend=True, ax=ax2, color='b',fontsize=10)
# butt = tk.Button(root,text="open file",padx=1,pady=5,fg="white",bg="#263D42",command=add)
# butt.pack()

#
# def animate(i):
#     pullData = open("history","r").read()
#     dataList = pullData.split('\n')
#     xList = []
#     yList = []
#     for eachLine in dataList:
#         if len(eachLine) > 1:
#             x, y = eachLine.split(',')
#             xList.append(int(x))
#             yList.append(int(y))
#
#     ax2.clear()
#     ax2.plot(xList, yList)
#
#
# ani = animation.FuncAnimation(figure2, animate, interval=1000)

beerstonks = internal_clock.InternalClock()

ani = animation.FuncAnimation(f,animate, interval=1000)


beerstonks.mainloop()
######Blabla

