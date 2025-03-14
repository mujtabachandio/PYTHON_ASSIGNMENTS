# Lesson 05: Control Flow & Loops

# if-elif-else Statement
num = 10
if num > 10:
    print("Number is greater than 10")
elif num == 10:
    print("Number is exactly 10")
else:
    print("Number is less than 10")

# for Loop
for i in range(5):  # Loop from 0 to 4
    print({i})

# while Loop
count = 3
while count > 0:
    print({count})
    count -= 1

# break and continue
for num in range(5):
    if num == 4:
        break  # Exit the loop when num is 3
    print(num)

for num in range(5):
    if num == 4:
        continue  # Skip when num is 3
    print(num)

# Lesson 06: Lists, Tuples & Dictionary

# List Example
fruits = ["apple", "banana", "cherry"]
fruits.append("mango")  # Add an item
fruits.remove("banana")  # Remove an item
print(fruits[0])  # Access first item
print(fruits)

# Tuple Example (Immutable List)
colors = ("red", "green", "blue")
print(colors[1])  # Access second item

# Dictionary Example (Key-Value Pairs)
student = {"name": "Ali", "age": 20, "course": "Python"}
print(student["name"])  # Access value by key
student["age"] = 21  # Update value
student["city"] = "Karachi"  # Add new key-value pair
print(student)

# Lesson 07: The Set & Frozenset

# Set Example (Unique Elements, Unordered)
numbers = {1, 2, 3, 4, 4, 5}  # Duplicates are removed automatically
numbers.add(6)
numbers.remove(2)
print(numbers)

# Set Operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1 | set2)  # Union
print(set1 & set2)  # Intersection
print(set1 - set2)  # Difference

# Frozenset Example (Immutable Set)
immutable_set = frozenset([1, 2, 3, 4])
print(immutable_set)
