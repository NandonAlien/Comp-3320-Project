import pygame
from sys import exit


pygame.init()

screen=pygame.display.set_mode((1240,720))

pygame.display.set_caption('First Come First Serve')

clock = pygame.time.Clock()

Font = pygame.font.Font(None, 20)


#The Font Renders
IDStr=  Font.render("ID :",False,"White")
ResetDescr =  Font.render("To End the Simulation, Press press Space",False,"White")
#Surface
#General 
Stick = []
EBlock =[]
Entry = []
Storage =[[0,1,2,False],[1,2,3,False]]
Ready = []
Runs = False
SimRun = True
Det = 1
SNext= 0
Read=0


class BlockS:
    def __init__(self, Colour):
        self.Block = pygame.Surface((1,10))
        self.Colour=Colour
        self.H = 1
    def setincr(self):
        self.Block = pygame.Surface((self.H*10,10))
    def setColour(self):
        self.Block.fill(self.Colour)

def developEntry(Storage):
    global Entry
    Entry =sorted(Storage, key=lambda x:x[1])
    for x in range(len(Entry)):
        w=BlockS("white")
        EBlock.append(w)
    return sorted(Storage, key=lambda x:x[1])

def Reset():
    pygame.quit()
    exit()

def ProcessPrints():
    for x in range(Read):
        EBlock[x].setColour()
        screen.blit(EBlock[x].Block,(200,50*(x+1)))
        


#Process Scheduling Specific

def FCFS(Entry, Ready):
    global Runs,Storage,SNext,Read
    i=0
    print(Entry)
    print(i)
    if len(Entry) > 0:
        while i < 1 and i < len(Entry):
            if Entry[i][1] > 0:
                i=1
            elif Entry[i][1]<=0:
                Ready.append(Entry[i])
                Entry.remove(Entry[i])
            
    if len(Ready)==0 and len(Entry) == 0:
        return 0
    if Runs == False and len(Ready) > 0:
        Ready[0][3]=True
        Storage[SNext][3]=True
        Runs = True
        Read+=1
        EBlock[Read-1].Colour = "red"
        
    elif Runs == True and len(Ready)>0:
        if Ready[0][2] <1:
            Ready[0][3] =False
            Storage[SNext][3]=False
            SNext+=1
            Ready.pop(0)
            Runs = False
            EBlock[Read-1].Colour = "gray"
        else:
            Ready[0][2]-=1
            EBlock[Read-1].H+=1
            EBlock[Read-1].setincr()
    print(Ready)         
    for x in Entry:
        x[1]-=1
    return 1


def run():
    print("--------------------------------------------------")
    print("The amount of Processes Done")
    print("--------------------------------------------------")
    print("--------------------------------------------------")
    Total = int(input())
    Processes = []
    for x in range(Total):
        print("For Process")
        print(x)
        print("")
        print("Input the Arrival Time")
        print("")
        ArrTime = int(input())
        print("")
        print("Input the Running Time")
        print("")
        RunTime = int(input())
        print("")
        print("--------------------------------------------------")
        Processes.append([x,ArrTime,RunTime,False])
    global Storage, Entry, Ready
    Storage=developEntry(Processes)
    RI90s(Entry,Ready,Storage)
    return

Running = True
def RI90s(Entry,Ready,Storage):    
    global SimRun,Move,screen,EBlock,Det

    while Running:
        screen.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Reset()
        if SimRun == True:
            Det = FCFS(Entry,Ready)
            ProcessPrints()
        if Det == 0:
            ProcessPrints()
            SimRun=False 
                
        for x in range(len(Storage)):
            screen.blit(IDStr,(0,50*(x+1)))
            screen.blit(Font.render(str(x),False,"White"),(100,50*(x+1)))
        pygame.display.update()
    
        clock.tick(2)
        
run()