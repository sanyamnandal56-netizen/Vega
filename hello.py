name=input("Enter you name- ")
age=int(input("Enter your age- "))
goal=input("Enter your goal-" )
sleep=float(input("Enter you sleep - "))
gap=8-sleep
weight=float(input("enter your weight - "))
height=float(input("enter your height - "))
BMI=weight/((height/100)**2)
print("BMI:", round(BMI, 2))
print("--your Vega Profile--")
print("Name: ",name)
print("Age: ",age)
print("Goal: ",goal)
print("Sleep: ",sleep)
if sleep>=8:
    print("you are doing well")
elif sleep>=6:
    print("you are doing good but you can improve by",gap,"hour")
else:
    print("you seriously lack sleep you need ",gap,"hours of sleep more")

if age<18:
    print("go to school Vega will help you build your habits early")
elif age<=25:
    print("this is your golden period lets build the skills together")
else:
    print("experience is your key use it .")
if BMI<18.5:
    print("Underweight — Vega will focus on healthy gain")
elif BMI<=24.9:
    print("Healthy range — let's maintain and build")
else:
    print("Vega will focus on gradual, sustainable loss")

