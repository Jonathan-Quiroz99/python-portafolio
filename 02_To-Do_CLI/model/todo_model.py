import os
from dotenv import load_dotenv
from supabase import create_client

class ToDoModel:
    def __init__(self):
        load_dotenv()
        url = os.getenv("SUPABASE_URL")
        key = os.getenv("SUPABASE_KEY")
        self.supabase = create_client(url, key)
        
    def create_task(self, task):
        self.supabase.table("todo_items").insert({
            "task": task,           
        }).execute()
        
    def load_tasks(self):
        response = self.supabase.table("todo_items").select("*").execute()
        return response.data
    
    def update_task(self, id_task, task, status):
        self.supabase.table("todo_items").update({
            "task": task, "is_completed": status
            }).eq("id", id_task).execute()
        
    
    def delete_task(self, id_task):
        self.supabase.table("todo_items").delete().eq("id", id_task).execute()