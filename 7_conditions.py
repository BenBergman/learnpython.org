x = 2
print(x == 2)
print(x == 3)
print(x < 3)

name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")

if x == 3:
    print("three")
else:
    print("not three")

x = [2]
y = [2]
if x is y:
    print("x is y")

y = x
if y is x:
    print("y is x")

print()
print()
print()


# Exercise

# change this code
number = 20
second_number = 0
first_array = [1,3,3]
second_array = [2,3]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")
