#!/usr/bin/python

#######################################
#                                     #
#   Making the UI for the OpenGraph   #
#    Man, Guis suck, so does this     #
#                                     #
#######################################


import matplotlib.pyplot as plt
from tkinter import *

import serial
import time
import math

from GraphMath import *

top = Tk()
top.title("OpenGraph")

class Grapher():
    def __init__(self, xArray, yArray, xAxisLabel, yAxisLabel):
        self.xArray = xArray
        self.yArray = yArray
        self.xAxisLabel = xAxisLabel
        self.yAxisLabel = yAxisLabel

    def plotData(self):
        plt.plot(self.xArray, self.yArray)
        plt.xlabel(self.xAxisLabel)
        plt.ylabel(self.yAxisLabel)
        plt.title(self.xAxisLabel + " vs. " + self.yAxisLabel)
        plt.show()
        self.xArray = dataObject.getX()
        self.yArray = dataObject.getY()

    def reset(self):
        self.xArray = []
        self.yArray = []

##Pthis object places all the items in the page

class MainWindow():
    def __init__(self, datObject, graphObject, widgetArray):
        self.status = 1
        self.datObject = datObject
        self.graphObject = graphObject
        self.startStopButton = Button(top, text="Start", command=self.changeStatus)
        self.calculations = Button(top, text="Caclulate Statistics", command=self.updateStatistics)
        self.plotData = Button(top, text="Plot Test", command = self.graphObject.plotData)
        self.startStopButton.grid( column = 0, row = 0)
        self.calculations.grid( row=1, column=0)
        self.plotData.grid(row= 0, column= 1)

        self.objectsArray = widgetArray

    def updateStatistics(self):

        print(self.datObject.getMean())

        for ob in self.objectsArray:
            if ob.name == "Mean":
                ob.update(self.datObject.getMean())
            elif ob.name == "Median":
                ob.update(self.datObject.getMedian())
            elif ob.name == "Mode":
                ob.update(self.datObject.getMode())
            elif ob.name == "Range":
                ob.update(self.datObject.getRange())
            elif ob.name == "Standard Deviation":
                ob.update(self.datObject.getStDev())

        for ob in self.objectsArray:
            ob.placeWidget()

    def changeStatus(self):
        if self.status == 1:
            self.datObject.DefineData(self.status)
            self.status = 0
        else:
            self.datObject.DefineData(self.status)
            self.status = 1


class Stats():
    def __init__(self, name, row, column):
        self.name = name
        self.value = ""
        self.rowPos = row
        self.columnPos = column
        self.labelWidget = Label(top, text= self.name + ": ")
        self.valueWidget = Label(top, text = self.value)

    def update(self, value):
        self.value= value
        self.valueWidget.config(text = self.value)
        #self.valueWidget.insert(END, value)

    def placeWidget(self):
        self.labelWidget.grid( row=self.rowPos, column=self.columnPos)
        self.valueWidget.grid( row=self.rowPos, column=self.columnPos + 1)


objectArray = [Stats("Mean", 2, 0),\
                Stats("Median", 3, 0),\
                Stats("Mode", 4, 0), \
                Stats("Range", 5, 0), \
                Stats("Standard Deviation", 6, 0)]
#graph1 = Graph([1,2,3,6,5], [5,13,5,1,1] , "testX", "testY")
#graph1.plotData()
dataObject = Data()
graphy =  Grapher(dataObject.getX(),dataObject.getY(), "test y", "Time")
wandow = MainWindow(dataObject, graphy, objectArray)




top.mainloop()
