
def dough (water, wheat):
    # print(f"mixing {water} and {wheat} together")
    if water == water and wheat == wheat:
        return ("dough")

    else:
        return "blob"

def bake(substance):
    if substance == "dough":
        return("bread")
    else:
        return ("not bread")

def bread_factory(substance1, substance2):
    output_dough = dough(substance1, substance2)
    bake(output_dough)


print(bake("dough")== "bread")
print(bake("brick")== "not bread")


#TEST#

# For our bread factory
# we should be able to put water and dough and get bread.
#if we do not add water and doe we should not get bread.

print("testing to see is this would print out bread")
print(bread_factory("water", "wheat")== "bread")
print(bread_factory("water", "wheat"))

print("testing to see is this would not print out bread")
print(bread_factory("water", "wheat")== "bread")
print(bread_factory("water", "cement"))