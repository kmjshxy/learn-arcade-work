print("most exciting class ever!!")
print("2nd line of \t text")
print(""""" wow 
test
a""")



# class sept 10
temperature = 5
print(temperature)

m = 294 / 10.5

print(m)

m = 294
g = 10.5
m2= m / g

print(m2)

miles_driven = 294
gallons_used = 10.5
mpg = miles_driven / gallons_used
print(mpg)

# x = 15 + 10
# x = 15 - 10
# x = 15 * 10
# x = 15 / 10
# x = 15 // 10 gives you division with no rounding
# x = 15 % 10  gives u the remainder of division

x = 3
y = 2 * x
z = 2 * (3 + y)
print(z)


x = 4
print(x)
x = x + 1
x = x + 1
print(x)
print(x + 1)
print(x + 1)


x += 1
# ^^ = 6

# orders of operations still exist
average = 90 + 71 + 100 + 98 / 5
print(average)
average = (90 + 71 + 100 + 98) / 5
print(average)

answer = "bananas"
print(answer)

print("the answer is", answer, "which are great")
print("the answer is" + answer + "which are great")

# answer = 42
# print("the answer is" + answer)
# this will give error

# this is a way u can do ^^
answer = 42
print(f"the answer is {answer}")


# sept 13
def print_hello():
    """ this function prints hello.
    """
    print("Hello!")


def goodbye():
    print("Goodbye!")


def main():
    print_hello()
    goodbye()


# if __name__=="__main__":
# ^ makes it so if u import it, it wont run


print_hello()
print_hello()
goodbye()




main()

def print_number(my_number):
    print(my_number)

print_number(5)
print_number(6)
print_number(11)

def add_numbers (a, b):
    print(a+b)

add_numbers(11, 7)

def sum_two_numbers (a, b):
    result= a + b
    return result

my_result =sum_two_numbers(5, 6)
print(my_result)

def volume_cylinder(radius, height):
    pi = 3.141592
    volume = pi * radius ** 2 * height
    return volume

my_volume=volume_cylinder(2.5, 5) * 6
print(my_volume)

# def cant change variables that already exist

# Example 4
def a():
    print("A start")
    b()
    print("A end")


def b():
    print("B start")
    c()
    print("B end")


def c():
    print("C start and end")


a()

def average_of_3(x, y, z):
    average = (x + y + z) / 3
    return average

my_result= average_of_3(10, 20, 30)
print(my_result)

# or

n1= 10
n2= 20
n3= 30

my2_result= average_of_3(n1, n2, n3)
print(my2_result)


# if statemant
#  also called conditional logic

a = 4
b = 5
c = 6

# <= less that or equal to
if a <= b:
    print("a is smaller than b")
# >= grater than or equal to
if a >= b:
    print(" b is smaller than a")
# == a & b are equal NOT =
if a == b:
    print(" a is equal to be ")

if a < b and a < c:
    print("a is less than b and c")

# != not equal

if a != b:
    print("a is not equal to b")

t  = True
it = True
nt = False
#this works but is not proper
if t == True:
    print("t is true!!")
# do this insted
if t:
    print("t is true")

if not it:
    print("t is false")
if t and it:
    print("both are true")

d = 3
f = 4
c = d == f

print(c)

if 1:
    print("1")
if "A":
    print("A")
# if 0:
#    print ("0")
# ^ doesnt work

volume = input ("what is the volume in ml ")
volume= int(volume)
print(f"you said the volume was {volume}.")

if volume > 110
    print("wow")
elif volume > 90:
    print("the volume is big")
elif volume < 30
    print("volume is small")
else:
    print("the volume is not big")
print("done")




