age = int(input("what your age"))
if (age >= 18):
    print("can enter")
elif(age - 18):
    print("can't enter")

temperature = 38.2
if(temperature > 37.5):
    print("high")
else:
    print("normal temperature")

your_number = int(input("what is your number"))
if your_number % 2 == 0:
    print("Even number")
else:
    print("odd number")

battery = 15
is_charging = True
if battery < 20 and is_charging:
    print("low battery, charging now")
elif battery < 20 and not is_charging:
    print("low battery; connect charger")
else:
    print("battery ok")

password = input("enter password")
if password == "python123":
    print("access approved")
else:
    print("access denied")

score = 72 
if score >= 90:
    print("Excellent")
elif score >= 75:
    print("good")
elif score >= 60:
    print("pass")
else:
    print("Fail")

first = int(input("first number"))
second = int(input("second number"))

if first > second:
    print("first is bigger")
elif second > first:
    print("second is bigger")
else:
    print("Equal")

fuel = 40
distance = 30
if fuel - distance >= 10:
    print("Enough fuel with resserve")
elif fuel >= distance:
    print("Enough fuel, low resserv")
else:
    print("not Enough fuel")

username = input("Enter username")
if username == "":
    print("Guest user")
else:
    print("Hello", username)

hour = 21 
if hour < 0 or hour > 23:
    print("Invalid hour")
elif hour < 12:
    print("morning")
elif hour < 18:
    print("afternoon")
else:
    print("evening")
    