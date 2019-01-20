################################
## Open Graph - CornHacks 2019
################################
import serial
import time


class Data:
    def __init__ (self, ExecTime):
        self.X = [0]
        self.Y = []
        self.SortY = []
        self.ExecTime = ExecTime
        self.ser = serial.Serial('COM6', baudrate = 9600, timeout = 1)
        self.Median = int(0)
        self.Mean = 0.0
        self.Mode = 0.0
        self.Range = 0.0
        self.StDeb = 0.0

    
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
            i += 1

    def DefineStats(self):
        # Guard in case there is no data
        if len(self.Y) == 0:
            return 1

        # Median: #
        if len(self.Y)%2 != 0: #Odd
            self.Median = self.Y[(len(self.Y)+1)/2]
        else
            self.Median = 
        ###########
        


    # Get Functions
    def getX(self):
        return self.X
    def getY(self):
        return self.Y
