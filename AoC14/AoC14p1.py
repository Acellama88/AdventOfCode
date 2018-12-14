scoreboard = [3, 7]
elf1 = 0
elf2 = 1
Goal = 540561
while len(scoreboard) < Goal + 10:
    score1 = scoreboard[elf1]
    score2 = scoreboard[elf2]
    total = score1+score2
    if total >= 10:
        scoreboard.append(1)
        scoreboard.append(total%10)
    else:
        scoreboard.append(total)
    #print(str(score1),str(score2),str(elf1),str(elf2),str(total),sep=" ")
    elf1 = (elf1 + (score1 + 1)) % len(scoreboard)
    elf2 = (elf2 + (score2 + 1)) % len(scoreboard)
i = Goal
while i < Goal + 10:
    print(scoreboard[i],end="")
    i += 1
