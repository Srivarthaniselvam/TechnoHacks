# task 7

from datetime import datetime
import datetime
class Task:
    def __init__(self, title, description, completed=False):
        self.title = title
        self.description = description
        self.completed = completed

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task.title} - {task.description}")

    def complete_task(self, index):
        if 1 <= index <= len(self.tasks):
            completed_task = self.tasks.pop(index - 1)
            print(f"Task '{completed_task}' completed!")
        else:
            print("Invalid task index.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            print("Task deleted successfully.")
        else:
            print("Invalid index.")
def run_todo_list():
    todo_list = ToDoList()

    while True:
        print("\n To-Do List Application")
        print("1. Add Task\n2. View Tasks\n3. Completed Task\n4. Deleted Task\nType 'exit' to Exit")

        choice = input("Enter your choice: ").lower()

        if choice == "1":
            todo_list.add_task(Task(input("Task Title: "), input("Task Description: ")))
            print("Task added successfully!")

        elif choice == "2":
            todo_list.view_tasks()

        elif choice == '3':
            todo_list.view_tasks()
            index = input("Enter the index of the task to complete: ")
            if index.isdigit():
                todo_list.complete_task(int(index))
            else:
                print("Invalid input. Please enter a valid index.")
        elif choice == "4":
            todo_list.view_tasks()
            try:
                index = int(input("Enter index of the task to delete: ")) - 1
                todo_list.delete_task(index)
                print("Task deleted successfully!")
            except (ValueError, IndexError):
                print("Invalid input or index.")

        elif choice == "exit":
            print(".............Closing To-Do List Application............")
            break

        else:
            print("Invalid choice. Please enter a valid option.")


run_todo_list()
