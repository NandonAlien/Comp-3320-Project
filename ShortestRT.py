import pygame
from sys import exit


pygame.init()

screen=pygame.display.set_mode((1240,720))

pygame.display.set_caption('Shortest Process Next')

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
Storage =[[0,1,5,False],[0,1,6,False],[1,2,3,False]]
Ready = []
Runs = False
SimRun = True
Det = 1
SNext= 0
Read=0
Supe=[]
Assign = 0

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

def SRT(Entry):
    global Runs,Storage,Supe,Read,Ready,Assign
    i=0
    if len(Entry) > 0:
        while i < 1 and i < len(Entry):
            if Entry[i][1] > 0:
                i=1
            elif Entry[i][1]<=0:
                Ready.append(Entry[i])
                Supe.append(Entry[i])
                Entry.remove(Entry[i])
                Read+=1
            
    if len(Ready)==0 and len(Entry) == 0:
        return 0
    if Runs == False and len(Ready) > 0:
        Ready = sorted(Ready, key=lambda x: x[2])
        print(Ready)
        Supe = sorted(Supe, key=lambda x: x[2])
        Ready[0][3]=True
        Wil=Storage.index(Supe[0])
        Storage[Wil][3]=True
        Runs = True
        EBlock[Read-1].Colour = "red"
        
    elif Runs == True and len(Ready)>0:
        if Ready[0][2] <1:
            Ready[0][3] =False
            Wil=Storage.index(Supe[0])
            Storage[Wil][3]=False
            EBlock[Read-1].Colour = "gray"
            Ready.pop(0)
            Supe.pop(0)
            Runs = False
        elif Ready[0][2]>Ready[len(Ready)-1][2]:
            Wil=Storage.index(Supe[0])
            EBlock[Wil].Colour = "white"
            Runs=False
        else:
            Ready[0][2]-=1
            Wil=Storage.index(Supe[0])
            EBlock[Wil].H+=1
            EBlock[Wil].setincr()        
    for x in Entry:
        x[1]-=1
    return 1



def run(SchedulQ):
    global Storage, Entry, Ready
    Storage=developEntry(SchedulQ)
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
            Det = SRT(Entry)
            ProcessPrints()
        if Det == 0:
            ProcessPrints()
            SimRun=False 
                
        for x in range(len(Storage)):
            screen.blit(IDStr,(0,50*(x+1)))
            screen.blit(Font.render(str(x),False,"White"),(100,50*(x+1)))
        pygame.display.update()
    
        clock.tick(1)
        
run(Storage)