
# Replace Item#

my_list = ["Eggs", "Bread", "Milk", "Butter", "Biscuits", "Apples", "Jam", 18, "Chocolate", "Crisps"]
print(f"my old list is {my_list}")

# Add Item#
my_list.append("Grapes")
print(f"inserted list {my_list}")
#----------------------------------------------------------------------------->#
my_list[5] = "Banana"
print(f"new list is {my_list}")

#----------------------------------------------------------------------------->#

# Length Of List#
my_list = len(my_list)
print(f"my the length of my list is {my_list}")
#----------------------------------------------------------------------------->#
#ranges are defines by colom (:)
print(my_list[1:4])
#----------------------------------------------------------------------------->#
# with :: you can jumo objects to the relavant index. for example.. print every 3rd object.#
print(my_list[::4])

