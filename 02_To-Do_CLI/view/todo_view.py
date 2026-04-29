from viewmodel.todo_viewmodel import ToDoViewModel

class ToDoView:
    def __init__(self):
        self.viewmodel = ToDoViewModel()
    
    def run(self):
        while True:
            try:
                print("Welcome to the to-do list!")
                print("Please select an option:")
                print("1. create task")
                print("2. View tasks")
                print("3. update task")
                print("4. delete task")
                print("5. Exit")
                choice = input("Enter your choice: ")
                
            
                if choice == '1':
                    task = input("please describe your new task: ")
                    message = self.viewmodel.create_task(task)
                    print(message)
                    
                elif choice == '2':
                    tasks = self.viewmodel.get_tasks()
                    print("list of tasks:")
                    print("-----------------------------------------------------------")
                    for record in tasks:                   
                        print(f"id: {record["id"]} | task: {record["task"]} | status: {"completed" if record["is_completed"]== True else "pending"} |")
                    print("-----------------------------------------------------------")
                    
                elif choice == '3':
                    tasks = self.viewmodel.get_tasks()
                    print("list of tasks:")
                    print("-----------------------------------------------------------")
                    for record in tasks:          
                        print(f"id: {record["id"]} | task: {record["task"]} | status: {"completed" if record["is_completed"]== True else "pending"} |")
                    print("-----------------------------------------------------------")
                        
                    id_task = int(input("please select task you want to update: "))
                    newtask = input("please describe the task: ")
                    newstatus = input("is it pending? [y/n]")
                    if newstatus not in ["y", "n"]:
                        raise ValueError ("please enteer 'y' or 'n'")
                        
                    message = self.viewmodel.update_task(id_task, newtask, True if newstatus == "y" else False)
                    print(message)
                    
                elif choice == '4':
                    tasks = self.viewmodel.get_tasks()
                    print("list of tasks:")
                    print("-----------------------------------------------------------")
                    for record in tasks:                        
                        print(f"id: {record["id"]} | task: {record["task"]} | status: {"completed" if record["is_completed"]== True else "pending"} |")
                    print("-----------------------------------------------------------")
                    id_task = int(input("please select task you want to delete: "))  
                    message = self.viewmodel.delete_task(id_task)
                    print(message)
                    
                elif choice == '5':
                    print("Exiting the To-Do List App. Goodbye!") 
                    break
            except ValueError as e:
                print(" error: ", e)