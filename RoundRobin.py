import pygame
from sys import exit


pygame.init()

screen=pygame.display.set_mode((1280,720))

pygame.display.set_caption('First Come First Serve')

clock = pygame.time.Clock()

Font = pygame.font.Font(None, 20)

#Surface Renderers
Blocker = pygame.Surface((1280,720))
Blocker.fill("Black")
#The Font Renders
ArrivTimeString= Font.render("Arrival Time",False,"White")
TimeString =  Font.render("Time",False,"White")
IDString =  Font.render("ID",False,"White")
ResetDescr =  Font.render("To End the Simulation, Press press Space",False,"White")


#General 
Entry = []
Storage =[[0,1,2,False],[1,2,3,False]]
Ready = []
Size = 0


    


def ProcessPrints(Batch):
    size = 100
    
    for x in Batch:
       
       ATime= Font.render(str(x.arrivalTime),False,"White")
       Time = Font.render(str(x.timeWeight),False,"White")
       ProcID=Font.render(str(x.IDs), False,"White")
       screen.blit(ProcID,(size,100))
       screen.blit(ATime,(size,200))
       screen.blit(Time,(size,300))
        #Adjust for the Rest
       size+=50

def Reset():
    pygame.quit()
    exit()

#Process Scheduling Specific
SlicNum =0
MaxTimer = 0
Timer=0

def RR(Entry, Ready):
    global SliceNum
    global Runs
    global MaxTimer
    global Timer
    i = 0
    while i == 0 and len(Entry) > 0:
        if Entry[i].arrivalTime > 0:
            i+=1
        if Entry[i].arrivalTime == 0:
            Ready.append(x)
            Entry.pop(0)
    if len(Ready)==0 and len(Entry) == 0:
        return 0
    if Runs == False and len(Ready) > 0:
        Ready[SliceNum].switchRun()
        Runs = True
    else:
        if Ready[SliceNum].timeWeight ==0:
            Ready[SliceNum].switchRun()
            Ready.pop(SlicNum)
            Runs = False
        elif Timer == 0:
            SliceNum = (SliceNum+1)%len(Ready)
            Timer = MaxTimer
        else:
            Ready[SliceNum].DecrTimer()
            Timer-=1
    return 1


#The Running of the Pygame
while True:
    keys = pygame.key.getpressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT or pygame.K_SPACE:
            Reset()
