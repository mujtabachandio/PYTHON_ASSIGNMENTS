"""
Lesson 08: Control Modules & Functions
This lesson covers Python modules and functions with examples.
"""

# Example 1: Basic Function Definition
def greet(name):
    """This function takes a name and returns a greeting"""
    return f"Hello, {name}!"

# Example 2: Function with Multiple Parameters
def calculate_rectangle_area(length, width):
    """Calculate the area of a rectangle"""
    return length * width

# Example 3: Function with Default Parameters
def power(base, exponent=2):
    """Calculate power with default exponent of 2"""
    return base ** exponent

# Example 4: Function with Variable Arguments
def sum_all(*numbers):
    """Sum all numbers passed to the function"""
    return sum(numbers)

# Example 5: Function with Keyword Arguments
def create_person(**details):
    """Create a person dictionary with given details"""
    return details

# Example 6: Lambda Function
square = lambda x: x ** 2

# Example 7: Function with Return Multiple Values
def get_dimensions(length, width):
    """Return multiple values from a function"""
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

# Testing the functions
if __name__ == "__main__":
    # Test Example 1
    print("Example 1:", greet("Alice"))
    
    # Test Example 2
    print("Example 2:", calculate_rectangle_area(5, 3))
    
    # Test Example 3
    print("Example 3:", power(3))  # Uses default exponent
    print("Example 3:", power(3, 3))  # Uses provided exponent
    
    # Test Example 4
    print("Example 4:", sum_all(1, 2, 3, 4, 5))
    
    # Test Example 5
    person = create_person(name="John", age=30, city="New York")
    print("Example 5:", person)
    
    # Test Example 6
    print("Example 6:", square(4))
    
    # Test Example 7
    area, perimeter = get_dimensions(4, 6)
    print("Example 7:", f"Area: {area}, Perimeter: {perimeter}") 