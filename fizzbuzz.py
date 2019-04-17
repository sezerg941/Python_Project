print("Welcome To FizzBuzz")

number_1 = (int(input("Enter A Starting Number ")))
number_2 = (int(input("Enter A Ending Number ")))

for num in range (number_1, number_2):

    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
        continue
    elif num % 3 == 0:
        print("Fizz")
        continue
    elif num % 5 == 0:
        print("Buzz")
        continue
    print(num)

# the continue statement rejects all interations of the look#
# and returns control to the top of the loop.#

# the % sign is used to find numbers that are divisible by 3 and 5#
#when this sign is used and uquate to 0.
# the program finds numbers that are divisible by 3 and 5.
# if those numbers have no remainders, then that number will be #
#replaced with fizzbuzz.#


