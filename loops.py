movies = ["Avengers", "Spider man", "Thor", "Rick And Morty"]

max_size_list = len(movies)
counter = -1
number = 1

while counter < max_size_list -1:
    counter += 1
    print(number, "-", movies[counter])
    number += 1


while True:
   user = input("Say Something ").strip().lower()
   if user == "exit":
       break
