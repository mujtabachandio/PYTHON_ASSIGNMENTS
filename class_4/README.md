# 🐍 Python Programming Lessons

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

*A comprehensive collection of Python programming lessons with practical examples and hands-on exercises*

</div>

## 📚 Table of Contents
- [Project Overview](#-project-overview)
- [Lesson Structure](#-lesson-structure)
- [Getting Started](#-getting-started)
- [Interactive Examples](#-interactive-examples)
- [Requirements](#-requirements)
- [Best Practices](#-best-practices)
- [Contributing](#-contributing)
- [License](#-license)

## 🎯 Project Overview

This repository contains a collection of Python programming lessons covering various fundamental concepts. Each lesson is contained in its own Python file with practical examples and explanations. The lessons are designed to be interactive and hands-on, allowing you to learn by doing.

## 📁 Lesson Structure

| Lesson | File | Description |
|--------|------|-------------|
| 📘 08 | `lesson_08.py` | Control Modules & Functions |
| 📘 09 | `lesson_09.py` | Exception Handling |
| 📘 10 | `lesson_10.py` | File Handling |
| 📘 11 | `lesson_11.py` | Math & Date Time Calendar |

## 🚀 Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/
   cd python-lessons
   ```

2. **Run the lessons**
   ```bash
   # Run individual lessons
   python lesson_08.py
   python lesson_09.py
   python lesson_10.py
   python lesson_11.py
   ```

## 📝 Interactive Examples

### 📘 Lesson 08: Control Modules & Functions
```python
# Example: Function with multiple parameters
def calculate_rectangle_area(length, width):
    return length * width

# Try it yourself!
area = calculate_rectangle_area(5, 3)
print(f"Area: {area}")  # Output: Area: 15
```

### 📘 Lesson 09: Exception Handling
```python
# Example: Basic try-except block
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

### 📘 Lesson 10: File Handling
```python
# Example: Writing to a file
with open("test.txt", "w") as file:
    file.write("Hello, World!")
```

### 📘 Lesson 11: Math & Date Time Calendar
```python
# Example: Date operations
from datetime import datetime
now = datetime.now()
print(f"Current date and time: {now}")
```

## 🛠️ Requirements

- Python 3.x
- No external dependencies required

## 💡 Best Practices

1. **Read the Documentation**
   - Study the comments and docstrings in each file
   - Understand the concepts before running the code

2. **Experiment with Code**
   - Modify the examples to try different scenarios
   - Add your own test cases
   - Break and fix the code to learn

3. **Follow Python Standards**
   - Use meaningful variable names
   - Write clear docstrings
   - Follow PEP 8 style guide

4. **Debug Effectively**
   - Use print statements for debugging
   - Try different input values
   - Handle exceptions properly

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">

### ⭐ Star this repository if you find it helpful!

</div> 