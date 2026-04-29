from model.todo_model import ToDoModel

class ToDoViewModel:
    def __init__(self):
        self.model = ToDoModel()
    
    def create_task(self, task):
        if task != "":
            self.model.create_task(task)
            return "task created"
        else:
            raise ValueError("task can't be empty")
    
    def get_tasks(self):
        return self.model.load_tasks()
    
    def update_task(self, id_task, task, status):
        tasks = self.model.load_tasks()
        if not any(t["id"]== id_task for t in tasks):
            raise ValueError("no task found")
        if task == "":
            raise ValueError("task can't be empty")
        
        self.model.update_task(id_task, task, status)
        return "task updated"
    
    def delete_task(self, id_task):
        tasks = self.model.load_tasks()
        if not any(task["id"]== id_task for task in tasks):
            raise ValueError("no task found")
        
        self.model.delete_task(id_task)
        return "task deleted"