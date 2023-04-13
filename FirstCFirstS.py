import pygame
from sys import exit


pygame.init()

screen=pygame.display.set_mode((1920,1080))

pygame.display.set_caption('First Come First Serve')

clock = pygame.time.Clock()

Font = pygame.font.Font(None, 20)


#The Font Renders
ArrivTimeString= Font.render("Arrival Time",False,"White")
TimeString =  Font.render("Time",False,"White")
IDString =  Font.render("ID",False,"White")
ResetDescr =  Font.render("To End the Simulation, Press press Space",False,"White")
#Surface
BlockS = pygame.Surface((10,10))

#General 
EBlock =[]
Entry = []
Storage =[[0,1,2,False],[1,2,3,False]]
Ready = []
Size = 0
Runs = False
SimRun = True
Det = 1
Move=0


def developEntry(Storage):
    global Entry
    
    Entry =sorted(Storage, key=lambda x:x[1])
    return 

def Reset():
    pygame.quit()
    exit()

def ProcessPrints(Batch):
    size = 100
    
    for x in Batch:
       


#Process Scheduling Specific
def FCFS(Entry, Ready):
    global Runs

    i = 0
    while i == 0 and len(Entry) > 0:
        if Entry[i].arrivalTime > 0:
            i+=1
        if Entry[i].arrivalTime == 0:
            Ready.append(Entry[i])
            Entry.pop(0)
    if len(Ready)==0 and len(Entry) == 0:
        return 0
    if Runs == False and len(Ready) > 0:
        Ready[0].switchRun()
        Runs = True
    else:
        if Ready[0].timeWeight ==0:
            Ready[0].switchRun()
            Ready.pop(0)
            Runs = False
        else:
            Ready[0].DecrTimer()
    return 1



def run(SchedulQ):
    global Storage, Entry, Ready
    developEntry(Storage)
    RI90s(Entry,Ready,Storage)
    return


def RI90s(Entry,Ready,Storage):    
    global SimRun

    while True:
        keys = pygame.key.getpressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.K_SPACE:
                Reset()
        ProcessPrints(Storage)
        if SimRun == True:
            Det = FCFS(Entry,Ready)
        if Det ==0:
            SimRun=False
        pygame.display.update()
        if keys[pygame.K_s]:
            clock.tick(60)
        else:
            clock.tick(10)