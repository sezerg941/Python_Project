# movies = ["Avengers", "Spider man", "Thor", "Rick And Morty"]
# counter = 0
#
# for id in movies:
#     print(counter +1, "-", id)
#     counter += 1
#
#
#
# embedded_data = [[1, 2, 3], [7, 12, 1], ["Skoda Feceilia Fun", "Panda 4*4"]]
#
# for data_list in embedded_data:
#     print(data_list)
#     for data in data_list:
#         print(data)


#Loops for dictionaries#

accounts = {

             2: {"names": "Bob", "money": "$10000"},
             3: {"names": "John", "money": "$1000000"}
}

# for account_dictionary in accounts.values():
#         print(account_dictionary)
#         for embedded_value in account_dictionary:
#             print (embedded_value)

for key in accounts:
    print(accounts[key])
    for embedded_key in accounts[key]:
        print([embedded_key])
