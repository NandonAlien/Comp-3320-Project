
class Proce:
    def __int__(self,arrivalTime, timeWeight, running):
        self.arrivalTime = arrivalTime
        self.timeWeight = timeWeight
        self.running = running
    def switchRun(self):
        if self.running == True:
            self.running=False
        else:
            self.running==True
    def DecrTimer(self):
        self.timeWeight-=1

