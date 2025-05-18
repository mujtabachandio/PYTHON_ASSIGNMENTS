# Task Management System

A simple command-line task management system built using Python and Object-Oriented Programming principles. This application allows users to create and manage multiple task lists, add tasks, mark them as completed, and remove tasks.

## Features

- Create multiple task lists
- Add tasks with titles, descriptions, and optional due dates
- Mark tasks as completed
- Remove tasks
- View all tasks in a list
- Navigate between different task lists
- Simple and intuitive command-line interface

## Requirements

- Python 3.6 or higher
- No external dependencies required

## Installation

1. Clone or download this repository
2. Navigate to the project directory
3. Install the requirements (if any):
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```bash
   python task_manager.py
   ```

2. Follow the on-screen menu options:
   - Create new task list
   - View all task lists
   - Select a task list to manage tasks
   - Exit the application

3. When managing a task list, you can:
   - Add new tasks
   - View all tasks
   - Mark tasks as completed
   - Remove tasks
   - Return to the main menu

## Project Structure

- `task_manager.py`: Main application file containing all the classes and logic
- `requirements.txt`: List of Python package dependencies
- `README.md`: This documentation file

## OOP Principles Used

1. **Classes and Objects**
   - Task class for individual tasks
   - TaskList class for managing collections of tasks
   - TaskManager class for managing multiple task lists

2. **Encapsulation**
   - Each class encapsulates its own data and methods
   - Properties are accessed through methods
   - Internal state is protected

3. **Type Hints**
   - Modern Python type hints for better code clarity
   - Improved IDE support and code maintainability

## Contributing

Feel free to fork this project and submit pull requests for any improvements or additional features.

## License

This project is open source and available under the MIT License. 