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