from datetime import datetime
from typing import List, Optional

class Task:
    def __init__(self, title: str, description: str, due_date: Optional[str] = None):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False
        self.created_at = datetime.now()

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "✓" if self.completed else " "
        return f"[{status}] {self.title} - {self.description} (Due: {self.due_date or 'No due date'})"

class TaskList:
    def __init__(self, name: str):
        self.name = name
        self.tasks: List[Task] = []

    def add_task(self, task: Task):
        self.tasks.append(task)

    def remove_task(self, index: int) -> bool:
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            return True
        return False

    def get_tasks(self) -> List[Task]:
        return self.tasks

    def __str__(self):
        return f"\n{self.name}:\n" + "\n".join(f"{i+1}. {task}" for i, task in enumerate(self.tasks))

class TaskManager:
    def __init__(self):
        self.task_lists: List[TaskList] = []

    def create_list(self, name: str) -> TaskList:
        task_list = TaskList(name)
        self.task_lists.append(task_list)
        return task_list

    def get_list(self, index: int) -> Optional[TaskList]:
        if 0 <= index < len(self.task_lists):
            return self.task_lists[index]
        return None

    def list_all_lists(self):
        for i, task_list in enumerate(self.task_lists):
            print(f"{i+1}. {task_list.name}")

def main():
    manager = TaskManager()
    
    while True:
        print("\n=== Task Manager ===")
        print("1. Create new task list")
        print("2. View all task lists")
        print("3. Select a task list")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == "1":
            name = input("Enter task list name: ")
            manager.create_list(name)
            print(f"Task list '{name}' created successfully!")
            
        elif choice == "2":
            if not manager.task_lists:
                print("No task lists available.")
            else:
                print("\nAvailable Task Lists:")
                manager.list_all_lists()
                
        elif choice == "3":
            if not manager.task_lists:
                print("No task lists available. Create one first!")
                continue
                
            manager.list_all_lists()
            list_index = int(input("Enter list number: ")) - 1
            task_list = manager.get_list(list_index)
            
            if task_list:
                while True:
                    print(f"\n=== {task_list.name} ===")
                    print("1. Add task")
                    print("2. View tasks")
                    print("3. Mark task as completed")
                    print("4. Remove task")
                    print("5. Back to main menu")
                    
                    sub_choice = input("\nEnter your choice (1-5): ")
                    
                    if sub_choice == "1":
                        title = input("Enter task title: ")
                        description = input("Enter task description: ")
                        due_date = input("Enter due date (optional, press Enter to skip): ")
                        task = Task(title, description, due_date if due_date else None)
                        task_list.add_task(task)
                        print("Task added successfully!")
                        
                    elif sub_choice == "2":
                        print(task_list)
                        
                    elif sub_choice == "3":
                        print(task_list)
                        task_index = int(input("Enter task number to mark as completed: ")) - 1
                        if 0 <= task_index < len(task_list.tasks):
                            task_list.tasks[task_index].mark_completed()
                            print("Task marked as completed!")
                        else:
                            print("Invalid task number!")
                            
                    elif sub_choice == "4":
                        print(task_list)
                        task_index = int(input("Enter task number to remove: ")) - 1
                        if task_list.remove_task(task_index):
                            print("Task removed successfully!")
                        else:
                            print("Invalid task number!")
                            
                    elif sub_choice == "5":
                        break
                        
                    else:
                        print("Invalid choice!")
            else:
                print("Invalid list number!")
                
        elif choice == "4":
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main() 