#   lists

#   decimals = floating points

#STR = STRING = text
"""x = 2, 3, 4
x = (2, 3, 4)
# tuple list ^^
# or
x = [2, 3, 4]
# just a list ^^"""

# lots of types of lists


x = [10, 20]
print(x)
    # prints whole list

    # print(x(1) )   will print error

    # lists use [] no matter what () are used for functions

    # fist integer is a 0 not 1

y = [3, 8, 7, 0, 5, 5, 2, 1]

print(y[1])

    # index = position in the list

    # if u put it x[ -1] will count from the back of the index so -1 would print one on ^^ and - 5 would print 0



z = [3, 8, 7, 0, 5, 5, 2, 1]

z[2] = 22
    # changes the 3rd number to 22

z = 18

    # resets integer and replaces the list

w = []
    # blank list good for writing list as u go

size = len(w)

    # ^^ will print how many element are in the list

# loop through the list
my_list = ["knife", "spoon", "fork"]

for item in my_list:
    print(item)
# anything can be in a list

the_list = [2, 3, 5]

for i in range (len(my_list)):
    print(the_list[i])
# doses the same thing


# OR you can don this

for index, value in enumerate(the_list):
    print("item", index, "is", value)



a_list = [2, 3, 4, 5, 2]
print(a_list)

a_list.append(100)

print(a_list)

# how to make a list from scratch

blist = []

for i in range(5):
    user_input = int(input("enter 5 numbers: "))
    blist.append(user_input)

print(blist)

clist = [3, 4, 5, 2, 8]

sum(clist)

#OR

list_total = 0

for item in clist:
    list_total += item

print(list_total)

# difference between [] and ()
"""
 tuples () cant change items in the list 
 but they are faster 
 use text for these mostly """

dlist = [2, 3, 4, 5, 4]

for item in dlist:
    item = item * 2 # makes a copy of the items in the list

# if u want to modify

for i in range(len(dlist)):
    dlist[i] *= 2

print(dlist)

x = "012345"

print("x=", x)
print("x=[0]", x[0])

print("x[:5]=", x[:5])

#for i in range("test stuff"):
#    print(i)

month_list = ["jan", "feb", "mar", "apr", "may", "jun", "jly", "aug", "sep", "oct", "nov", "dec"]

m = int(input("enter a month number"))

print(month_list[m - 1])


# letters = number

#75 65 84 69 - kate
# utf8 - the code called



plain_text = "This is a test. ABC abc"

for c in plain_text:
    x = ord(c)
    x += 1
    ch = chr(x)
    print(ch, end=" ")

# ord(c) is get the numbers into the numbers the computer stores

# chr() makes the number into a characture

elist = [4, 2, 56, 2, 0]
biggest_number = elist[0]
for item in elist:
    if item > biggest_number:
        biggest_number = item

print(biggest_number)


''' object packaging 
'''
#calss names get capitalized
class address:
    """
    This is a video game character
    """
    def __init__(self):
        """ create my character"""
        self.line1= ""
        self.name = ""
        self.line2 = 0
        self.city = 0
        # self. keeps the variable
    # method is a function in a class



def main():
    # you NEED the parentheses after address
    home_address = address()
    home_address.name = "josh smith"
    home_address.line2 = "lol"

    vacation_home_address = address()
    vacation_home_address.name = "john smith"
    vacation_home_address.line2 = "no"

    


main()
