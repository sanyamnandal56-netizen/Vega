# goals = ["get fit", "learn coding", "save money", "sleep better"]
# for goal in goals:
#     print("My goal",goal)
# goals.append("drink water")
# print(goals)
# goals.remove(goals[0])
# print(goals)
# if "get fit" in goals:
#     print("yes")
# else:
#     print("no")
# modules = ["fitness","diet","career","finance"]
# for i in range(2):
#     print(modules[i])
# sleep = [7, 6.5, 8, 5, 7.5, 6, 8]
# bad=0
# for i in sleep:
#     if i<7:
#         bad+=1
# print(bad)    
workout_log = []
count=0
wait=0

for i in range(7):
    entry = input("Enter workout " + str(i + 1) + ": ")
    workout_log.append(entry)
    

print("--- This Week's Workouts ---")
for i, entry in enumerate(workout_log, 1):
    print(str(i) + ".", entry)
    if entry == "rest":
        count+=1

    else:
        wait+=1
print("rest days:",count)
print("Active Days",wait)
    



