class Proce:
    def __init__(self,arrivalTime, timeWeight, running):
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


def BuildingProce(processes):
    arr =[]
    for x in processes:
        print(x)
        w = Proce(x[0],x[1],False)
        arr.append(w)
    return arr

def ArrivalQueue(processes):
    arrival = sorted(processes, key=lambda x: x.arrivalTime)
    return arrival
qr=[[0,1],[100,77],[22,45],[5,2],[110,10]]

l = BuildingProce(qr)

w = ArrivalQueue(l)

for x in w:
    print(x.arrivalTime)
