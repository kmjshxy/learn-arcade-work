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



