"""
Lesson 09: Exception Handling
This lesson covers Python exception handling with examples.
"""

# Example 1: Basic try-except block
def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero!"

# Example 2: Multiple exception handling
def process_number(number):
    try:
        result = 100 / number
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero!"
    except TypeError:
        return "Error: Please provide a number!"
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"

# Example 3: try-except-else block
def check_number(number):
    try:
        result = 100 / number
    except ZeroDivisionError:
        return "Error: Cannot divide by zero!"
    else:
        return f"Division successful: {result}"

# Example 4: try-except-finally block
def file_operation():
    try:
        file = open("test.txt", "r")
        content = file.read()
        return content
    except FileNotFoundError:
        return "Error: File not found!"
    finally:
        print("This block always executes")

# Example 5: Raising custom exceptions
class CustomError(Exception):
    pass

def validate_age(age):
    if age < 0:
        raise CustomError("Age cannot be negative!")
    if age > 150:
        raise CustomError("Age seems invalid!")
    return "Age is valid"

# Example 6: Using with statement (context manager)
def safe_file_operation():
    try:
        with open("test.txt", "w") as file:
            file.write("Hello, World!")
        return "File written successfully"
    except IOError as e:
        return f"Error writing to file: {str(e)}"

# Testing the functions
if __name__ == "__main__":
    # Test Example 1
    print("Example 1:", divide_numbers(10, 2))
    print("Example 1:", divide_numbers(10, 0))
    
    # Test Example 2
    print("Example 2:", process_number(5))
    print("Example 2:", process_number(0))
    print("Example 2:", process_number("abc"))
    
    # Test Example 3
    print("Example 3:", check_number(5))
    print("Example 3:", check_number(0))
    
    # Test Example 4
    print("Example 4:", file_operation())
    
    # Test Example 5
    try:
        print("Example 5:", validate_age(25))
        print("Example 5:", validate_age(-5))
    except CustomError as e:
        print("Example 5:", str(e))
    
    # Test Example 6
    print("Example 6:", safe_file_operation()) 