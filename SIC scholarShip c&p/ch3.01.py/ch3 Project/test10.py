import json

current_tasks = []
completed_tasks = []
Work_tasks = []
Personal_tasks = []

CURRENT_TASKS_FILE = "current_tasks.json"
COMPLETED_TASKS_FILE = "completed_tasks.json"
WORK_TASKS_FILE = "work_tasks.json"
PERSONAL_TASKS_FILE = "personal_tasks.json"

def load_tasks_from_json():
    global current_tasks, completed_tasks, Work_tasks, Personal_tasks

    try:
        with open(CURRENT_TASKS_FILE, 'r') as f:# r stands for Read - Default value. Opens a file for reading, error if the file does not exist
            current_tasks_data = json.load(f)
            for task_data in current_tasks_data:
                if task_data['type'] == 'work':
                    task = Work_task(
                        task_data['title'],
                        task_data['description'],
                        task_data['priority'],
                        task_data['progress']
                    )
                else:
                    task = Personal_task(
                        task_data['title'],
                        task_data['description'],
                        task_data['category'],
                        task_data['progress']
                    )
                current_tasks.append(task)
    except FileNotFoundError:
        pass  #عشان لو الفايل مش موجود

    try:
        with open(COMPLETED_TASKS_FILE, 'r') as f:
            completed_tasks_data = json.load(f)
            for task_data in completed_tasks_data:
                if task_data['type'] == 'work':
                    task = Work_task(
                        task_data['title'],
                        task_data['description'],
                        task_data['priority'],
                        'completed'
                    )
                else:
                    task = Personal_task(
                        task_data['title'],
                        task_data['description'],
                        task_data['category'],
                        'completed'
                    )
                completed_tasks.append(task)
    except FileNotFoundError:
        pass

    try:
        with open(WORK_TASKS_FILE, 'r') as f:
            work_tasks_data = json.load(f)
            for task_data in work_tasks_data:
                task = Work_task(
                    task_data['title'],
                    task_data['description'],
                    task_data['priority'],
                    task_data['progress']
                )
                Work_tasks.append(task)
    except FileNotFoundError:
        pass

    try:
        with open(PERSONAL_TASKS_FILE, 'r') as f:
            personal_tasks_data = json.load(f)
            for task_data in personal_tasks_data:
                task = Personal_task(
                    task_data['title'],
                    task_data['description'],
                    task_data['category'],
                    task_data['progress']
                )
                Personal_tasks.append(task)
    except FileNotFoundError:
        pass

def save_tasks_to_json():
    current_tasks_data = []
    for task in current_tasks:
        task_data = {
            'title': task.title,
            'description': task.description,
            'progress': task.progress,
            'type': task.task_type()
        }
        if isinstance(task, Work_task): #isinstance بتخلي البروجيكت يتعامل مع الداتا حسب نوعها
            task_data['priority'] = task.priority
        else:
            task_data['category'] = task.category
        current_tasks_data.append(task_data)
#عايز اشوف ازاي بتشتغل عايزا اعرف ازاي
    with open(CURRENT_TASKS_FILE, 'w') as f:
        json.dump(current_tasks_data, f, indent=4) #indent عشان يحافظ علي شكل الداتا المتخزنه مترتههه

    completed_tasks_data = []
    for task in completed_tasks:
        task_data = {
            'title': task.title,
            'description': task.description,
            'type': task.task_type()
        }
        if isinstance(task, Work_task):
            task_data['priority'] = task.priority
        else:
            task_data['category'] = task.category
        completed_tasks_data.append(task_data)

    with open(COMPLETED_TASKS_FILE, 'w') as f:
        json.dump(completed_tasks_data, f, indent=4)

    work_tasks_data = []
    for task in Work_tasks:
        task_data = {
            'title': task.title,
            'description': task.description,
            'priority': task.priority,
            'progress': task.progress,
            'type': task.task_type()
        }
        work_tasks_data.append(task_data)

    with open(WORK_TASKS_FILE, 'w') as f:
        json.dump(work_tasks_data, f, indent=4)
    personal_tasks_data = []
    for task in Personal_tasks:
        task_data = {
            'title': task.title,
            'description': task.description,
            'category': task.category,
            'progress': task.progress,
            'type': task.task_type()
        }
        personal_tasks_data.append(task_data)

    with open(PERSONAL_TASKS_FILE, 'w') as f:
        json.dump(personal_tasks_data, f, indent=4)

class Task_manager:
    def __init__(self):
        self.tasks = current_tasks
        self.completed_tasks = completed_tasks
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
                "ur choice: "
            ))

            if user_choice == 0:
                self.create_task()
                save_tasks_to_json()  #عشان نعمل save للفايل

            elif user_choice == 1:
                self.update_task()
                save_tasks_to_json()

            elif user_choice == 2:
                self.delete_task()
                save_tasks_to_json()

            elif user_choice == 3:
                self.mark_as_completed()
                save_tasks_to_json()

            elif user_choice == 4:
                if not current_tasks:
                    print('no current tasks available.')
                else:
                    print('these are the current tasks:')
                    for task in current_tasks:
                        print(
                            f'task title: {task.title}     task is completed? {task.progress}     task type: {task.task_type()}')
                        if isinstance(task, Work_task):
                            print(f'priority: {task.priority}')
                        else:
                            print(f'category: {task.category}')
                        print('description:', task.description)
                        print('-----------------------------------')

            elif user_choice == 5:
                if not completed_tasks:
                    print('no tasks are completed.')
                else:
                    print('these are the completed tasks:')
                    for task in completed_tasks:
                        print(f'task title: {task.title}     task type: {task.task_type()}')
                        if isinstance(task, Work_task):
                            print(f'priority: {task.priority}')
                        else:
                            print(f'category: {task.category}')
                        print('description:', task.description)
                        print('-----------------------------------')

            elif user_choice == 6:
                print('thank you for using SIC task manager app')
                save_tasks_to_json()
                exit() # عشان يطلع برا البروجيكت

            else:
                print('invalid input, please try again')
        except ValueError:
            print('invalid input, please enter a number from 0 to 6')

    def create_task(self):
        while True:
            task_type = input("do you want to create a work task or personal task? (work/personal):  ")
            if task_type == "work":
                print('enter the task details')
                title = input("please enter the task title:  ")
                description = input("please enter the task description:  ")
                priority = input("please enter the task priority (high/medium/low):  ")
                progress = 'incompleted'
                added_work_task = Work_task(title, description, priority, progress)
                print("work task added successfully!")
                self.tasks.append(added_work_task)
                Work_tasks.append(added_work_task)
                break

            elif task_type == "personal":
                print('enter the task details')
                title = input("please enter the task title:  ")
                description = input("please enter the task description:  ")
                category = input("please enter the task category (family, sports, study):  ")
                progress = 'incompleted'
                added_personal_task = Personal_task(title, description, category, progress)
                print("personal task added successfully!")
                self.tasks.append(added_personal_task)
                Personal_tasks.append(added_personal_task)
                break

            else:
                print("invalid task type")

    def update_task(self):
        if not self.tasks:
            print('no tasks available to edit.')
            print('please add task first')
            self.create_task()
            return None

        print("these are the registered tasks:")
        for task in self.tasks:
            if isinstance(task, Work_task):
                print(f"task title: {task.title}     task is completed? {task.progress}      priority: {task.priority}")

            elif isinstance(task, Personal_task):
                print(
                    f"task title: {task.title}     task is completed? {task.progress}       category: {task.category}")
            print("-----------------------------------")

        user_task_title = input("which task do you want to edit? (enter the task title):  ")

        for task in self.tasks:
            if user_task_title == task.title:
                if isinstance(task, Work_task):
                    edited_in_task = input("what do you want to edit? (title/description/priority/progress):  ")
                    if edited_in_task == "title":
                        task.title = input("enter the new title:  ")
                    elif edited_in_task == "description":
                        task.description = input("enter the new description:  ")
                    elif edited_in_task == "priority":
                        task.priority = input("enter the new priority:  ")
                    elif edited_in_task == "progress":
                        task.progress = input("enter the new progress (completed/incompleted/in progress):  ")
                        if task.progress == "completed":
                            self.completed_tasks.append(task)
                            self.tasks.remove(task)
                    print("work task updated successfully!")

                elif isinstance(task, Personal_task):
                    edited_in_task = input("what do you want to edit? (title/description/category/progress):  ")
                    if edited_in_task == "title":
                        task.title = input("enter the new title:  ")
                    elif edited_in_task == "description":
                        task.description = input("enter the new description:  ")
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

    def delete_task(self):
        if not current_tasks:
            print('no tasks available to delete.')
            print('please add task first')
            self.create_task()
        else:
            print('these are the registered tasks')
            for task in current_tasks:
                print(f'task title: {task.title}     task is completed? {task.progress}')
                print('-----------------------------------')
            user_task_title = input('which task do you want to delete? (enter the task title):  ')
            for task in current_tasks:
                if user_task_title == task.title:
                    current_tasks.remove(task)
                    if task in Work_tasks:
                        Work_tasks.remove(task)
                    if task in Personal_tasks:
                        Personal_tasks.remove(task)
                    print('task deleted successfully!')
                    break
            else:
                print('task not found')
    def mark_as_completed(self):
        if not current_tasks:
            print('no tasks available to mark as completed.')
            print('please add task first')
            self.create_task()
            return None
        else:
            print('these are the registered tasks')
            for task in current_tasks:
                print(f'task title: {task.title}     task is completed? {task.progress}')
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

class Task:
    def __init__(self, title, description, progress='incompleted'):
        self.title = title
        self.description = description
        self.progress = progress

class Work_task(Task):
    def __init__(self, title, description, priority, progress='incompleted'):
        super().__init__(title, description, progress)
        self.priority = priority
    def task_type(self):
        return "work"

class Personal_task(Task):
    def __init__(self, title, description, category, progress='incompleted'):
        super().__init__(title, description, progress)
        self.category = category

    def task_type(self):
        return "personal"

# load_tasks_from_json()

print("welcome to SIC task manager app")
while True:
    main_menu = Task_manager().main_menu()