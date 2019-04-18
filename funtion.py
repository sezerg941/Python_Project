# # function only do one job.
# # functions are like little machines.
# #they can take inputer (argumwents).
# # they run a block of code
# # they give a specific output.
#
#
# #syntax
#  #deqfinition name (argiument):
#     #Block to run
#
# # def making_bread():
# #     print("yummy bread")
# #
# # making_bread()
# #
# #
# def full_name(f_name, l_name):
#      print(f_name, l_name)
# user_f_name = input("enter your first name")
# user_l_name = input("enter your last name")
# full_name(user_f_name, user_l_name)
# #
# # #area of a circle

# def circle_area(radius):
#     print("radius is ", radius)
#     calculation = 3.14 * radius * radius
#     print("area of the circle is ",calculation)
# circle_area(100)
#
# def circle_area(radius, PII = 3.14):
#     return PII * radius * radius
# print(circle_area(10, 3.14159))
#
# def full_name(f_name, l_name, m_name):
#     return f_name, m_name, l_name
# user_f_name = input("enter your first name ")
# user_l_name = input("enter your last name ")
#
# print(full_name(user_f_name, user_l_name))
#

def full_name(f_name = "", l_name = "", m_name = ""):
    return f_name + "" + m_name + "" + l_name + ""
print(full_name("Sezer Garip"))