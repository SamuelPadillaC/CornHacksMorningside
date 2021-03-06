################################
## Open Graph - CornHacks 2019
################################
import serial
import time
import math


class Data:
    def __init__ (self):
        self.X = [0]
        self.Y = []
        self.backX = []
        self.backY = []
        self.SortY = []
        self.ExecTime = 0
        self.ser = serial.Serial('COM6', baudrate = 9600, timeout = 1)
        self.Median = 0.0
        self.Mean = 0.0
        self.Mode = 0.0
        self.Range = 0.0
        self.StDev = 0.0
        self.status = 0
    ####################

    ## Reset ##
    def Reset(self):
        self.backX = self.X.copy()
        self.backY = self.Y.copy()
        self.X = [0]
        self.Y = []
        self.SortY = []
    ####################

    ## Deine Data ##
    def DefineData(self, status):
        self.status = status #Status is time
        while self.X[int(len(self.X) - 1)] < int(self.status): #Last elmt of X < total time
            t0 = time.time()
            arduinoData = self.ser.readline().decode('ascii')
            try:
                self.Y.append(float(arduinoData))
            except:
                pass
            self.X.append((time.time() - t0)+self.X[len(self.X)-1])

        # Make sure arrays have same size
        if len(self.Y) > len(self.X):
            while len(self.Y) > len(self.X):
                self.Y.pop()
        elif len(self.Y) < len(self.X):
            while len(self.Y) < len(self.X):
                self.X.pop()

        self.DefineStats() #Define Stats right away
    ####################

    ## Sort ##
    def FnSortY(self):
        self.SortY = self.Y.copy()
        self.SortY.sort()
    ####################

    ## Define Stats ##
    def DefineStats(self):
        # Guard in case there is no data
        if len(self.Y) == 0:
            return 1
        self.FnSortY()

        # Median: #
        if len(self.SortY)%2 != 0: #Odd
            self.Median = self.SortY[int((len(self.SortY)+1)/2)]
        else:
            self.Median = (self.SortY[int(len(self.SortY)/2)] + self.SortY[(int(len(self.SortY)/2)+1)])/2
        ###########
        # Mean #
        self.Mean = sum(self.SortY)/ len(self.SortY)
        ###########
        # Mode #
        reps = 0
        GreaterRep = 0
        for i in range(1, len(self.SortY)):
            if self.SortY[i] == self.SortY[i-1]:
                reps += 1
            elif (reps != 0 and self.SortY[i] != self.SortY[i-1] and reps >= GreaterRep):
                self.Mode = self.SortY[i-1]
                GreaterRep = reps
                reps = 0
        if GreaterRep == 0:
            self.Mode = 'NaN'
        ###########
        # Range: #
        self.Range = self.SortY[int(len(self.SortY) - 1)] - self.SortY[0]
        ###########
        # Standard Deviation #
        top = 0
        for i in self.SortY:
            top += math.pow((i - self.Mean), 2)
        self.StDev = math.sqrt(top/len(self.SortY))

        # Reset arrays after done calculations
        self.Reset()
    ####################

    ## Get Functions ##
    def getX(self):
        return self.X
    def getbackX(self):
        return self.backX  
    def getY(self):
        return self.Y
    def getbackY(self):
        return self.backY
    def getMedian(self):
        return self.Median
    def getMean(self):
        return self.Mean
    def getMode(self):
        return self.Mode
    def getRange(self):
        return self.Range
    def getStDev(self):
        return self.StDev
    ####################
