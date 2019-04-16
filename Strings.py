#-------------------------------------------------------------------------------------------------#

#strings~
#string are characters inside quotes.#

print("hello")
type("hello")
print(type("56765765765"))

#concatinatenation is adding two strings together#
object_sezer = "Car"
variable_sezer ="Bike"
print("Sezer" + " " + f"Garip {object_sezer} {variable_sezer}")

name = "World"
program = "Python"
print(f"Hello {name}! This Is {program}")

#-------------------------------------------------------------------------------------------------#

#Calcukalting the length#
#len()

example_text = "here is some text with lots of text     "
print(len(example_text))

# Strip Of White Space#
#strip()
strip_variable = example_text.strip()
print(len(strip_variable))

#-------------------------------------------------------------------------------------------------#


#.lower()
print (example_text.lower())
#.upper()
print(example_text.upper())
#.capitalize()
print(example_text.capitalize())

#white spaces(split)
print(example_text.split())
