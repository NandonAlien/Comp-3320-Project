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



#The Running of the Pygame
while True:
    keys = pygame.key.getpressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT or pygame.K_SPACE:
            Reset()
