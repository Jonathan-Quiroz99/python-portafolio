import os
from dotenv import load_dotenv
from supabase import create_client

class CalculatorModel:
    def __init__(self):
        load_dotenv()
        url = os.getenv("SUPABASE_URL")
        key = os.getenv("SUPABASE_KEY")
        self.supabase = create_client(url, key)
    
    def calculate(self, num1, operator, num2):
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            if num2 != 0:
                return num1 / num2
            else:                
                raise ValueError("Cannot divide by zero")
    
    def save_history(self, operation, result):
        self.supabase.table("calculator_history").insert({
            "operation": operation, 
            "result": result
            }).execute()
        
    def load_history(self):
        response = self.supabase.table("calculator_history").select("*").execute()
        return response.data
    