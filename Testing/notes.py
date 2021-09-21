# for loops - when you know how many times to loop
# while loop - loop intill condition

#for loop
repetitions = int(input("how many times"))
def print_about_gum(repetitions):
    for i in range(repetitions):
        print("I will not chew gum in class")


print("But I can drink water")

def main():
    print_about_gum(repetitions)

main()

for j in range(10,-1,-1):
    print(j)

print("blank line")


for k in range(3):
    print("a")
    for l in range(3):
        print("b")

# running total

total = 0
# total has to be outside the loop
for i in range(5):
    new_number = int(input("enter a number: "))
    total += new_number

# print("the total is", total):

# total2 = 0

''' for m in range (1,100)
    total2 +=1

print("total2 ", total2)'''


for n in range (5):
    print("hello")

print("there")

a = 0
for i in range(10):
    a = a + 1
for j in range(10):
    a = a + 1
print(a)

#prints 110

a = 0
for i in range(10):
    a = a + 1
    for j in range(10):
        a = a + 1
print(a)

#prints 100

#while loop

o = 0
while o < 10:
    print(o)
    o += 1

# does the same thing as

for p in range(10):
    print(p)

q = 10
while q > -1:
    print(q)
    q -= 1

