def add (a, b):
  return a + b

def subtraction (a, b):
  return a - b

def multiplication (a, b):
  return a * b

def division(a, b):
  if b == 0:
    return "Error: Division by zero is not allowed."
  else:
    return a / b

def get_user_input():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    operation = input("Enter choice (1/2/3/4): ")
    
    if operation not in ['1', '2', '3', '4']:
        print("Invalid input. Please enter a number between 1 and 4.")
        return None, None, None
    
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return None, None, None
    
    return operation, num1, num2

def calculator():
    while True:
        operation, num1, num2 = get_user_input()
        
        if operation is None:
            continue
        
        if operation == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif operation == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif operation == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif operation == '4':
            result = divide(num1, num2)
            if isinstance(result, str):
                print(result)
            else:
                print(f"{num1} / {num2} = {result}")
        
        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break

calculator()