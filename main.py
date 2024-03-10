class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({'task': task, 'completed': False})
        print(f'Task "{task}" added successfully.')

    def display_tasks(self):
        if not self.tasks:
            print('No tasks available.')
        else:
            print('Tasks:')
            for idx, task in enumerate(self.tasks, 1):
                status = 'Completed' if task['completed'] else 'Not Completed'
                print(f"{idx}. {task['task']} - {status}")

    def mark_completed(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1]['completed'] = True
            print(f'Task marked as completed: "{self.tasks[task_index - 1]["task"]}"')
        else:
            print('Invalid task index.')

    def remove_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            removed_task = self.tasks.pop(task_index - 1)
            print(f'Task removed: "{removed_task["task"]}"')
        else:
            print('Invalid task index.')

# Main program
todo_list = ToDoList()

while True:
    print('\nMenu:')
    print('1. Add a task')
    print('2. Display tasks')
    print('3. Mark a task as completed')
    print('4. Remove a task')
    print('5. Exit')

    choice = input('Enter your choice: ')

    if choice == '1':
        task = input('Enter the task: ')
        todo_list.add_task(task)
    elif choice == '2':
        todo_list.display_tasks()
    elif choice == '3':
        task_index = int(input('Enter the task index to mark as completed: '))
        todo_list.mark_completed(task_index)
    elif choice == '4':
        task_index = int(input('Enter the task index to remove: '))
        todo_list.remove_task(task_index)
    elif choice == '5':
        print('Exiting the to-do list application. Goodbye!')
        break
    else:
        print('Invalid choice. Please enter a number between 1 and 5.')
