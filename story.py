character = input("what is your  characters name? ")
gender = input("Is your character male of female? ")
gender_type_female = "she"
gender_type_male = "he"

if gender != "male":
    print(f"There was a person named {character} that lived in an oak. Everyday {gender_type_female} saw incidents happening around the area. ")

else:
    print(f"There was a person named {character} that lived in an oak. Everyday {gender_type_male} saw incidents happening around the area. ")



print(f"{character} saw an old man crossing the street")

decision_1 = input("Do You Help Him? ")

print(decision_1)
if decision_1 == "yes":
    print(f"the old man gave {character} a chocolate.")


else:
    print("the old man and the child took too long crossing the street and got hit by a car")



print(f"Today {character} saw a girl shouting at her mother.")

decision_2 = input("Did You Stop Her? ")

if decision_2 != "no":
    print(f"the girl stopped shouting and hugged mom.")
else:
    decision_2 != "no"
    print(f"the mom slapped her daughter made things worse.")

print(f"the moral of this story is, look around you and  try help others. not doing so can make things worse")