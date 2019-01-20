################################
## Open Graph - CornHacks 2019
################################
import serial
import time
import math


class Data:
    def __init__ (self, ExecTime):
        self.X = [0]
        self.Y = []
        self.SortY = []
        self.ExecTime = ExecTime
        self.ser = serial.Serial('COM6', baudrate = 9600, timeout = 1)
        self.Median = 0.0
        self.Mean = 0.0
        self.Mode = 0.0
        self.Range = 0.0
        
    ###############
    ## Get rid of the extra X in the list
    ##############


    def DefineData(self):
        i = 0
        while i < self.ExecTime: #figure this out
            t0 = time.time()
            arduinoData = self.ser.readline().decode('ascii')
            try:
                self.Y.append(float(arduinoData))
            except:
                pass
            self.X.append((time.time() - t0)+self.X[len(self.X)-1]) 
            self.X.pop() #Get rid of extra X element
            i += 1

    def FnSortY(self):
        self.SortY = self.Y.copy()
        self.SortY.sort()

    def DefineStats(self):
        # Guard in case there is no data
        if len(self.Y) == 0:
            return 1
        self.FnSortY()

        # Median: #
        if len(self.SortY)%2 != 0: #Odd
            self.Median = self.SortY[(len(self.SortY)+1)/2]
        else:
            self.Median = (self.SortY[len(self.SortY)/2] + self.SortY[(len(self.SortY)/2)+1])/2
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
        self.Range = self.SortY[len(self.SortY) - 1] - self.SortY[0]
        ###########


    # Get Functions
    def getX(self):
        return self.X
    def getY(self):
        return self.Y
    def getMedian(self):
        return self.Median
    def getMean(self):
        return self.Mean
    def getMode(self):
        return self.Mode
    def getRange(self):
        return self.Range
