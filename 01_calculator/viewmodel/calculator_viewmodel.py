from model.calculator_model import CalculatorModel

class CalculatorViewModel:
    def __init__(self):
        self.model = CalculatorModel()
        
    def perform_calculation(self, num1, operator, num2):
        if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
            raise ValueError("Inputs must be numbers")
        
        if operator not in ['+', '-', '*', '/']:
            raise ValueError("Invalid operator")
        
        if operator == '/' and num2 == 0:
            raise ValueError("Cannot divide by zero")
        
        result = self.model.calculate(num1, operator, num2)
        self.model.save_history(f"{num1} {operator} {num2}", result)
        return result
        
    def capture_history(self):
        return self.model.load_history()