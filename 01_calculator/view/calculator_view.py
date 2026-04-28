from viewmodel.calculator_viewmodel import CalculatorViewModel

class CalculatorView:
    def __init__(self):
        self.viewmodel = CalculatorViewModel()
    
    def display_menu(self):
        while True:
            print("\t Welcome to the Calculator App!")
            print("Please select an option:")
            print("1. Perform a calculation")
            print("2. View calculation history")
            print("3. Exit")
            choice = input("Enter your choice: ")
            
            if choice == '1':
                num1 = float(input("Enter the first number: "))
                operator = input("Enter the operator (+, -, *, /): ")
                num2 = float(input("Enter the second number:"))
                try:
                    result = self.viewmodel.perform_calculation(num1, operator, num2)
                    print(f"The result of {num1} {operator} {num2} is: {result}")
                except ValueError as e:
                    print(f"error: {e}")
            elif choice == '2':
                history = self.viewmodel.capture_history()
                print("Calculation History:")
                for record in history:
                    print(f"{record['operation']} = {record['result']}")
            elif choice == '3':
                print("Exiting the Calculator App. Goodbye!")
                break