"""
Lesson 10: File Handling
This lesson covers Python file handling operations with examples.
"""

import os

# Example 1: Writing to a file
def write_to_file(filename, content):
    """Write content to a file"""
    try:
        with open(filename, 'w') as file:
            file.write(content)
        return f"Successfully wrote to {filename}"
    except IOError as e:
        return f"Error writing to file: {str(e)}"

# Example 2: Reading from a file
def read_from_file(filename):
    """Read content from a file"""
    try:
        with open(filename, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return f"Error: File {filename} not found"
    except IOError as e:
        return f"Error reading file: {str(e)}"

# Example 3: Appending to a file
def append_to_file(filename, content):
    """Append content to a file"""
    try:
        with open(filename, 'a') as file:
            file.write(content)
        return f"Successfully appended to {filename}"
    except IOError as e:
        return f"Error appending to file: {str(e)}"

# Example 4: Reading file line by line
def read_lines(filename):
    """Read file line by line"""
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        return lines
    except FileNotFoundError:
        return f"Error: File {filename} not found"
    except IOError as e:
        return f"Error reading file: {str(e)}"

# Example 5: Working with binary files
def write_binary_file(filename, data):
    """Write binary data to a file"""
    try:
        with open(filename, 'wb') as file:
            file.write(data)
        return f"Successfully wrote binary data to {filename}"
    except IOError as e:
        return f"Error writing binary file: {str(e)}"

# Example 6: File operations (exists, size, etc.)
def get_file_info(filename):
    """Get information about a file"""
    try:
        if os.path.exists(filename):
            size = os.path.getsize(filename)
            return {
                "exists": True,
                "size": f"{size} bytes",
                "is_file": os.path.isfile(filename),
                "is_dir": os.path.isdir(filename)
            }
        return {"exists": False}
    except Exception as e:
        return f"Error getting file info: {str(e)}"

# Example 7: Working with directories
def list_directory(path="."):
    """List contents of a directory"""
    try:
        return os.listdir(path)
    except Exception as e:
        return f"Error listing directory: {str(e)}"

# Testing the functions
if __name__ == "__main__":
    # Test Example 1
    print("Example 1:", write_to_file("test.txt", "Hello, World!\n"))
    
    # Test Example 2
    print("Example 2:", read_from_file("test.txt"))
    
    # Test Example 3
    print("Example 3:", append_to_file("test.txt", "This is appended text.\n"))
    
    # Test Example 4
    print("Example 4:", read_lines("test.txt"))
    
    # Test Example 5
    binary_data = b"Hello, Binary World!"
    print("Example 5:", write_binary_file("binary.bin", binary_data))
    
    # Test Example 6
    print("Example 6:", get_file_info("test.txt"))
    
    # Test Example 7
    print("Example 7:", list_directory()) 