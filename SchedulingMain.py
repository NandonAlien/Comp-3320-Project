import RoundRobin
import ShortestRT
import ShortestPNext
import FirstCFirstS


print("Please input the type of Scheduling You are doing")
print("--------------------------------------------------")
print("1    First Come First Serve")
print("2    Round Robin Slicing")
print("3    Shortest Process Next")
print("4    Shortest Remaining Time")
print("--------------------------------------------------")
print("--------------------------------------------------")
Schedulingtype= input()
print("--------------------------------------------------")
print("--------------------------------------------------")
print("Please the amount of Processes Done")
print("--------------------------------------------------")
print("--------------------------------------------------")
Total = input()
Processes = []
for x in range(Total):
    print("For Process")
    print(x)
    print("")
    print("Input the Arrival Time")
    print("")
    ArrTime = input()
    print("")
    print("Input the Running Time")
    print("")
    RunTime = input()
    print("")
    print("--------------------------------------------------")
    Processes.append([x,ArrTime,RunTime,False])


if Schedulingtype == 1:
    FirstCFirstS.run(Processes)

elif Schedulingtype == 2:
    print("How much time for each Process")
    Times = input()
    RoundRobin.run(Processes,Times)
    
elif Schedulingtype == 3:
    ShortestPNext.run(Processes)

elif Schedulingtype == 4:
    ShortestRT.run(Processes)


#Process Below to be integrated Later
