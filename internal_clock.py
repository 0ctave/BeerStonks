from datetime import datetime
import random as random
from tkinter import ttk
import time
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from pandas import DataFrame
import pandas as pd

from matplotlib import pyplot as plt

pullData = open("history", "r").read()
dataList = pullData.split('\n')
xList = []
yList = []
for eachLine in dataList:
    if len(eachLine) > 1:
        x, y = eachLine.split(',')
        xList.append(int(x))
        yList.append(int(y))

data = {'Beer_Value': xList,
        'Time': yList
        }

global df1
df1 = DataFrame(data, columns=['Beer_Value', 'Time'])


def get_time():
    date = datetime.utcnow() - datetime(1970, 1, 1)
    seconds = (date.total_seconds())
    return round(seconds * 1000)


class InternalClock(tk.Tk):

    def __init__(self):
        global df1
        super().__init__()

        self.base_time = 1 * 1000

        # configure the root window

        # change the background color to black
        # self.style = ttk.Style(self)
        # self.style.configure(
        #     'TLabel',
        #     background='black',
        #     foreground='red')

        canvas = tk.Canvas(self, height=700, width=700)
        canvas.pack()
        frame = tk.Frame(self, bg="white")
        label = tk.Label(frame, text=50)
        label.pack()
        figure = plt.Figure(figsize=(5, 4), dpi=100)
        self.ax = figure.add_subplot(111)

        df = df1[['Beer_Value', 'Time']].groupby('Time').sum()
        print(df)
        df.plot(kind='line', legend=True, ax=self.ax, color='b', fontsize=10)

        line2 = FigureCanvasTkAgg(figure, self)
        line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)

        # schedule an update every 1 second
        self.start_time = get_time()
        self.time_elapsed = 0

        self.after(self.base_time, self.update)

    def update(self):
        global df1
        print(get_time() - self.start_time)

        """ update the label every 1 second """
        rand = random.randint(0, 1000) / 1000
        print(rand)
        time.sleep(rand)

        self.ax.clear()

        data = {'Beer_Value': [rand],
                'Time': [get_time()]
                }
        df2 = DataFrame(data, columns=['Beer_Value', 'Time'])

        df1 = pd.concat([df1, df2])
        df = df1[['Beer_Value', 'Time']].groupby('Time').sum()
        df.plot(kind='line', legend=True, ax=self.ax, color='b', fontsize=10)
        print(df1)
        # schedule another timer
        self.time_elapsed = self.time_elapsed + 1
        self.after(self.base_time + (self.start_time + self.time_elapsed * self.base_time) - get_time(), self.update)
