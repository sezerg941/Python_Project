age = int(input("how old are you"))
test = input("have you passed your driving test?")
driver_1 = False

if age >= 18 and driver_1 == ("true"):

    print("you can drive.")
    print("..."("Sorry You Can Not Drive"))
elif age < 18:
    print("you can not drive, you are too young")
elif age > 18:
    print("you can drive")
else:
    print("sorry you cannot drive")

