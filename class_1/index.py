# 1. Integer and Float Data Types
age = 25  # This is an integer (whole number)
height = 5.9  # This is a float (decimal number)
print("Section 1: Integer and Float Data Types")
print("Age:", age)
print("Height:", height)
print()

# 2. String Data Type
greeting = "Hello, world!"  # This is a string (a sentence)
print("Section 2: String Data Type")
print("Greeting:", greeting)
print()

# 3. Boolean Data Type
is_sunny = True  # This is a boolean, True or False
is_raining = False  # Another boolean, False means it's not raining
print("Section 3: Boolean Data Type")
print("Is it sunny?", is_sunny)
print("Is it raining?", is_raining)
print()

# 4. List Data Type
fruits = ["apple", "banana", "cherry"]  # A list of fruits
fruits.append("orange")  # Add "orange" to the list
fruits[0] = "grape"  # Change the first fruit in the list to "grape"
print("Section 4: List Data Type")
print("Fruits:", fruits)
print()

# 5. Tuple Data Type
coordinates = (10, 20)  # A tuple (an ordered, unchangeable collection)
print("Section 5: Tuple Data Type")
print("Coordinates:", coordinates)
print()

# 6. Dictionary Data Type
person = {"name": "John", "age": 30, "city": "New York"}  # A dictionary with key-value pairs
person["age"] = 31  # Change the age in the dictionary
print("Section 6: Dictionary Data Type")
print("Person:", person)
print()

# 7. Set Data Type
colors = {"red", "green", "blue"}  # A set of unique colors
colors.add("yellow")  # Add a new color to the set
print("Section 7: Set Data Type")
print("Colors:", colors)
print()

# 8. None Data Type
unknown = None  # None means nothing or no value
print("Section 8: None Data Type")
print("Unknown value:", unknown)
print()

# Operators (for performing calculations or comparisons)

# 1. Arithmetic Operators (for basic math)
sum_result = age + height  # Adding age and height (int + float)
difference = age - 5  # Subtracting 5 from age
product = age * 2  # Multiplying age by 2
division = height / 2  # Dividing height by 2
remainder = age % 4  # Remainder when age is divided by 4
print("Section 9: Arithmetic Operators")
print("Sum of age and height:", sum_result)
print("Difference of age and 5:", difference)
print("Product of age and 2:", product)
print("Division of height by 2:", division)
print("Remainder when age is divided by 4:", remainder)
print()

# 2. Comparison Operators (to compare values)
is_equal = age == 25  # Is age equal to 25?
is_greater = age > height  # Is age greater than height?
print("Section 10: Comparison Operators")
print("Is age equal to 25?", is_equal)
print("Is age greater than height?", is_greater)
print()

# 3. Logical Operators (to combine conditions)
both_true = (age > 20 and height > 5)  # True if both conditions are true
either_true = (age > 20 or height < 5)  # True if at least one condition is true
not_true = not (age > 20)  # True if age is not greater than 20
print("Section 11: Logical Operators")
print("Are both conditions true?", both_true)
print("Is at least one condition true?", either_true)
print("Is age not greater than 20?", not_true)
