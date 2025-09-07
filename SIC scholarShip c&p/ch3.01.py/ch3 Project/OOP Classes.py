current_tasks = []
completed_tasks = []
Work_tasks = []
Personal_tasks = []

#this is the main class that manages the tasks(delete, edit, create, 
#mark as completed, show current tasks, show completed tasks)
class Task_manager:
    def __init__ (self):
            self.tasks = current_tasks
            self.completed_tasks = completed_tasks

    #this is the main menu that shows the options to the user
    def main_menu(self):
        try:
            user_choice = int(input(
        "what do you want to do?\n"
        "(0) create\n"
        "(1) edit\n"
        "(2) delete\n"
        "(3) mark as completed\n"
        "(4) show current tasks\n"
        "(5) show completed tasks\n"
        "(6) exit\n"
        " "
    ))

            if user_choice == 0:
                create_new_task = Task_manager().create_task()
            
            if user_choice == 1:
                edit_task = Task_manager().update_task()

            if user_choice == 2:
                delete_task = Task_manager().delete_task()
            
            if user_choice == 3:
                mark_completed_task = Task_manager().mark_as_completed() 

            if user_choice == 4:
                if not current_tasks:
                    print('no current tasks available.')
                else:
                    print('these are the current tasks:')
                    for task in current_tasks:
                        print(f'these are the registered tasks: task title:  {task.title}      task due date {task.due_date}     task is completed ? {task.progress}     task type {task.task_type()}')
                        print('-----------------------------------')

            if user_choice == 5:
                if not completed_tasks:
                    print('no tasks are completed.')
                else:
                    print('these are the completed tasks:')
                    for task in completed_tasks:
                        print(f'these are the completed tasks: task title:  {task.title}      task due date {task.due_date}  task type {task.task_type()}')
                        print('-----------------------------------')
            
            if user_choice == 6:
                print('thank you for using SIC task manager app')
                exit()

            else:
                print('invalid input, please try again')
        except ValueError:
            print('invalid input, please enter a number from 0 to 6')

    #this function creates a new task and adds it to the current tasks list
    def create_task(self):
            while True:
                task_type = input("do you want to create a work task or personal task? (work/personal):  ")
                if task_type == "work":
                    print('enter the task details')
                    title = input("please enter the task title:  ")
                    description = input("please enter the task description:  ")
                    due_date = input("please enter the task due date:  ")
                    priority = input("please enter the task priority (high/medium/low):  ")
                    progress = 'incompleted'
                    added_work_task = Work_task(title, description, due_date, priority, progress)
                    print("work task added successfully!")   
                    self.tasks.append(added_work_task)
                    Work_tasks.append(added_work_task)
                    break

                elif task_type == "personal":
                    print('enter the task details')
                    title = input("please enter the task title:  ")
                    description = input("please enter the task description:  ")
                    due_date = input("please enter the task due date:  ")
                    category = input("please enter the task category (family, sports, study):  ")
                    progress = 'incompleted'
                    added_personal_task = Personal_task(title, description, due_date, category, progress)
                    print("personal task added successfully!")
                    self.tasks.append(added_personal_task)
                    Personal_tasks.append(added_personal_task)
                    break

                else:
                    print("invalid task type")

    #this function updates an existing task in the current tasks list          
    def update_task(self):
        if not self.tasks:
            print('no tasks available to edit.')
            print('please add task first')
            self.create_task()
            return None 
    
        print("these are the registered tasks:")
        for task in self.tasks:
            if isinstance(task, Work_task):
                print(f"task title: {task.title}     due date: {task.due_date}      task is completed? {task.progress}      priority: {task.priority}         progress: {task.progress}")

            elif isinstance(task, Personal_task):
                print(f"task title: {task.title}     due date: {task.due_date}      task is completed? {task.progress}       category: {task.category}       progress: {task.progress}")
            print("-----------------------------------")

        user_task_title = input("which task do you want to edit? (enter the task title):  ")

        for task in self.tasks:
            if user_task_title == task.title:
                if isinstance(task, Work_task):
                    edited_in_task = input("what do you want to edit? (title/due date/priority/progress):  ")
                    if edited_in_task == "title":
                        task.title = input("enter the new title:  ")
                    elif edited_in_task == "due date":
                        task.due_date = input("enter the new due date:  ")
                    elif edited_in_task == "priority":
                        task.priority = input("enter the new priority:  ")
                    elif edited_in_task == "progress":
                        task.progress = input("enter the new progress (completed/incompleted/in progress):  ")
                        if task.progress == "completed":
                            self.completed_tasks.append(task)
                            self.tasks.remove(task)
                    print("work task updated successfully!")

                elif isinstance(task, Personal_task):
                    edited_in_task = input("what do you want to edit? (title/due date/category/progress):  ")
                    if edited_in_task == "title":
                        task.title = input("enter the new title:  ")
                    elif edited_in_task == "due date":
                        task.due_date = input("enter the new due date:  ")
                    elif edited_in_task == "category":
                        task.category = input("enter the new category:  ")
                    elif edited_in_task == "progress":
                        task.progress = input("enter the new progress (completed/incompleted/in progress):  ")
                        if task.progress == "completed":
                            self.completed_tasks.append(task)
                            self.tasks.remove(task)
                    print("personal task updated successfully!")
                break
        else:
            print("task not found")

    #this function deletes an existing task from the current tasks list
    def delete_task(self):
        if not current_tasks:
            print('no tasks available to delete.')
            print('please add task first')
            create_new_task = Task_manager()
            create_new_task.create_task()
        else: 
            print('these are the registered tasks')
            for task in current_tasks:
                print(f'these are the registered tasks: task title:  {task.title}      task due date {task.due_date}     task is completed ? {task.progress}')
                print('-----------------------------------')
            user_task_title = input('which task do you want to delete? (enter the task title):  ')
            for task in current_tasks:
                if user_task_title == task.title:
                    current_tasks.remove(task)
                    print('task deleted successfully!')
                    break
            else:
                print('task not found')

    #this function marks an existing task as completed and moves it to the completed tasks list
    def mark_as_completed(self):
        if not current_tasks:
            print('no tasks available to mark as completed.')
            print('please add task first')
            create_new_task = Task_manager()
            create_new_task.create_task()
            return None
        else:
            print('these are the registered tasks')
            for task in current_tasks:
                print(f'these are the registered tasks: task title:  {task.title}      task due date {task.due_date}     task is completed ? {task.progress}')
                print('-----------------------------------')
            user_task_title = input('which task do you want to mark as completed? (enter the task title):  ')
            for task in current_tasks:
                if user_task_title == task.title:
                    task.progress = 'completed'
                    completed_tasks.append(task)
                    current_tasks.remove(task)
                    print('task marked as completed successfully!')
                    break
            else:
                print('task not found')

#this is the parent class for all tasks    
class Task:
      def __init__ (self, title, description, due_date, progress = 'incompleted'):
            self.title = title
            self.description = description
            self.due_date = due_date
            self.progress = progress

#this is the child class for work tasks
class Work_task(Task):
        def __init__ (self, title, description, due_date, priority, type="work"):
                super().__init__(title, description, due_date)
                self.priority = priority
                self.type = type

        def task_type(self):
            return self.type

#this is the child class for personal tasks
class Personal_task(Task):
        def __init__ (self, title, description, due_date, category, type="personal"):
                super().__init__(title, description, due_date)
                self.category = category
                self.type = type

        def task_type(self):
            return self.type

print("welcome to SIC task manager app")
while True:
    main_menu = Task_manager().main_menu()

    
        
         
            