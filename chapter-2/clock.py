currenttime = input("What is the current time (in hours)? ")
waitingtime = input("How many hours do you have to wait? ")

currenttimeint = int(currenttime)
waitingtimeint = int(waitingtime)

hours = currenttimeint + waitingtimeint

timeofday = hours % 24

print(timeofday)