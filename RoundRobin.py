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
SliceNum=0
Assign=0
MaxTimer = 0
Timer=0
Supe= []

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
    for x in range(SliceNum):
        EBlock[x].setColour()
        screen.blit(EBlock[x].Block,(200,50*(x+1)))
        


#Process Scheduling Specific

def RR(Entry, Ready):
    global Runs,Storage,MaxTimer, Timer,SliceNum,Assign,Supe

    i=0  
    if len(Entry) > 0:
        while i < 1 and i < len(Entry):
            if Entry[i][1] > 0:
                i=1
            elif Entry[i][1]<=0:
                Ready.append(Entry[i])
                Supe.append(Entry[i])
                Entry.remove(Entry[i])
                SliceNum+=1

    if len(Ready)==0 and len(Entry) == 0:
        return 0
    if Runs == False and len(Ready) > 0:
        Ready[0][3]=True
        Wil=Storage.index(Supe[Assign])
        Storage[Wil][3]=True
        Runs = True
        EBlock[Wil].Colour = "red"
        
    elif Runs == True and len(Ready)>0:
        if Ready[Assign][2] <1:
            Ready[Assign][3] =False
            Wil=Storage.index(Supe[Assign])
            Storage[Wil][3]=False
            EBlock[Wil].Colour = "gray"
            Ready.pop(Assign)
            Supe.pop(Assign)
            Runs = False
            Timer=MaxTimer
            
        elif Timer ==0:
            EBlock[Assign].Colour = "white"
            Assign=(Assign+1)%len(Ready)
            Timer=MaxTimer
            Runs=False   
        else:
            Ready[Assign][2]-=1
            Timer-=1
            Lens=Storage.index(Supe[Assign])
            EBlock[Lens].H+=1
            EBlock[Lens].setincr()
    print(Ready)         
    for x in Entry:
        x[1]-=1
    return 1


def run(SchedulQ,Times):
    global Storage, Entry, Ready,MaxTimer,Timer
    MaxTimer=Times
    Timer=Times
    Storage=developEntry(SchedulQ)
    RI90s(Entry,Ready,Storage)
    return


def RI90s(Entry,Ready,Storage):    
    global SimRun,Move,screen,EBlock,Det

    while True:
        screen.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Reset()
        if SimRun == True:
            Det = RR(Entry,Ready)
            ProcessPrints()
        if Det == 0:
            ProcessPrints()
            SimRun=False 
                
        for x in range(len(Storage)):
            screen.blit(IDStr,(0,50*(x+1)))
            screen.blit(Font.render(str(x),False,"White"),(100,50*(x+1)))
        pygame.display.update()
    
        clock.tick(2)
        

run(Storage, 3)