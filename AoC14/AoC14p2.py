def checkScore(scores, goal):
    endpoint = len(scores) - 1
    goalend = len(goal)-1
    penalties = 3 #Required as we sometimes add 2 numbers!
    while goalend >= 0 and penalties > 0:
        if scores[endpoint] != goal[goalend]:
            goalend = len(goal)-1
            penalties -= 1
        #If the last number is added twice (11), pass first, fail second, need to recheck second for pass
        if scores[endpoint] == goal[goalend]:
            goalend -= 1
        endpoint -= 1
    if goalend < 0:
        #return the answer (+1 to offset 0 count)
        return endpoint + 1
    else:
        return 0
        
#Initialization    
scoreboard = [3, 7]
elf1 = 0
elf2 = 1
#Goal Sequence
Goal = [5,4,0,5,6,1]
stop = 0
total = 0
#Keep Going we need to Stop (Break is Redundant)
while stop == 0:
    #Get Score
    score1 = scoreboard[elf1]
    score2 = scoreboard[elf2]
    total = score1+score2
    #Add Score, will never be >18
    if total >= 10:
        scoreboard.append(1)
        scoreboard.append(total%10)
    else:
        scoreboard.append(total)
    #See if the Goal was found
    total = checkScore(scoreboard, Goal)
    #End if it is Non-Zero
    if total > 0:
        stop == 1
        break #Not needed but added anyways
    #Update Elf Positioning - Don't Overflow the Modulo!
    elf1 = (elf1 + (score1 + 1)) % len(scoreboard)
    elf2 = (elf2 + (score2 + 1)) % len(scoreboard)
print(str(total)) #Win
      
