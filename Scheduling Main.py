import pygame
from sys import exit
pygame.init()

screen=pygame.display.set_mode((1280,720))
pygame.display.set_caption('Process Scheduling')
clock = pygame.time.Clock()

Font = pygame.font.Font(None, 30)

textsurf1=Font.render('FCS 1', False, 'white')
textsurf2=Font.render('RR 2', False, 'white')
textsurf3=Font.render('SPN 3', False, 'white')
textsurf4=Font.render('SRT 4', False, 'white')
running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill("gray")    
    screen.blit(textsurf1,(0,0))
    screen.blit(textsurf2,(0,600))
    screen.blit(textsurf3,(100,0))
    screen.blit(textsurf4,(100,600))
    #insert Switch Case(if else)
    #Future endeaveor, Set the text and dis surf to change 
    pygame.display.update()
    clock.tick(60)

#select the scheduling method
#Switch case
#1
#   First Come First Serve
#2
#   Round Robin
#3
#   Shortest Process Next
#4
#   Shortest Remaining Time
#
#For all of them: this function 
#   Select the number of Processes
#
#While Loop for each Scheduling State is a function each containing
#   An event that sends you back to the main function when the you complete the simulation
#
# FCFS
#   
#  Set their Entry time as the arrival time
#
#During each time
#Add new process when their Entry time = 0
#Dequeue process from that array and queue into the Ready
#Check Arrival Times
#	Set Highest if none are running
#Decrement Running Time 
#		Decrement Entry Time
#
#RR

#Set their Entry time as the arrival time

#During each time
#Add new process when their Entry time = 0
#Dequeue process from that array and Enqueue into the Ready
#Check Counter
#	If Runtime = 0
#		Dequeue from array and set the next process in tht array to the running
#		Reset Counter
#	If Counter = 0
#		Set Next process in the array to Running
#		Reset Counter
#Decrement Counter
#Decrement Running Time
#		Decrement Entry Time
#SPN
#During each time
#Add new process when their Entry time = 0
#Dequeue process from that array and Enqueue into the Ready
#Check Process Times
#	If Process Time=0
#Set Running to the process time with the minimum process
#			Decrement Running Time
#Decrement Entry Time
#SRT
#During each time
#Add new process when their Entry time = 0
#Dequeue process from that array and Enqueue into the Ready
#Check Process Times
#	Set Running to the process time with the minimum process
#			Decrement Running Time
#Decrement Entry Time
	

