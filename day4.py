
vega_profile={
    "name": input("enter your name: "),
    "age": input("enter your age: "),
    "goal": input("enter your goal: "),
    "sleep_hours": input("enter your sleep_hours: "),
    "fitness_level": input("enter your fitness_level: ")
}
vega_profile["modules"] = ["fitness", "diet", "career", "finance", "grooming", "routine"]
vega_profile["streak"] = 0
vega_profile["days_completed"] = 0
print("--Vega Profile--")
for key,value in vega_profile.items():
    if key=="modules":
        continue
    print(key,"-->",value)

print("Vega modules Activated - ")
for i in vega_profile["modules"]:
    print("-",i)
    