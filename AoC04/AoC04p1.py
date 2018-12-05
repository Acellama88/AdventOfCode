with open('./schedule.txt') as f:
	lines = f.read().splitlines()
#ID, 00, 01, 02, 03, 04, ..., 59
ID = 0
start = 0
stop = 0
compute = 0
Guards = list()
for timestamp in lines:
    tokens = timestamp.split()
    if "Guard" in timestamp:
        ID = tokens[3]
    elif "falls" in timestamp:
        start = tokens[1].replace("]","").split(":")[1]
    elif "wakes" in timestamp:
        stop = tokens[1].replace("]","").split(":")[1]
        compute = 1
    if compute > 0:
        Guard = {}
        found = 0
        for person in Guards:
            if person["ID"] == ID:
                Guard = person
                found = 1
                break
        if found == 0:
            Guard["ID"] = ID
            Guards.append(Guard)
        time = int(start)
        end = int(stop)
        while time < end:
            if str(time) in Guard:
                Guard[str(time)] += 1
            else:
                Guard[str(time)] = 1
            time += 1
        compute = 0

finalTime = 0
finalMinute = 0
finalID = 0
finalTime = 0
for Guard in Guards:
    time = 0
    Time = 0
    Minute = 0
    totalTime = 0
    ID = 0
    while time < 60:
        if str(time) in Guard:
            totalTime += Guard[str(time)]
            if Guard[str(time)] > Time:
                Time = Guard[str(time)]
                Minute = str(time)
                ID = Guard["ID"]
        time += 1
    if totalTime > finalTime:
        finalTime = totalTime
        finalMinute = Minute
        finalID = ID
    print(ID + " " + Minute + " " + str(Time) + " " + str(totalTime))
print("End: " + finalID + " " + finalMinute + " " + str(finalTime))
