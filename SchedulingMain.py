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
    ShortestPNext

elif Schedulingtype == 4:
    ShortestRT


#Process Below to be integrated Later

def SRT(Entry, Ready):
    global Runs

    i = 0
    while i == 0 and len(Entry) > 0:
        if Entry[i].arrivalTime > 0:
            i+=1
        if Entry[i].arrivalTime == 0:
            Ready.append(x)
            Ready = sorted(Ready, key=lambda x: x.arrivalTime)
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

def SRT(Entry, Ready):
    global Runs

    i = 0
    while i == 0 and len(Entry) > 0:
        if Entry[i].arrivalTime > 0:
            i+=1
        if Entry[i].arrivalTime == 0:
            Ready.append(x)
            Ready = sorted(Ready, key=lambda x: x.arrivalTime)
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