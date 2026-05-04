while True:
    num1 = input("\nEnter first number (or 'quit' to exit): ")
    
    if num1.lower() == "quit":
        print("Goodbye!")
        break
    
    operator = input("Enter operator (+, -, *, /): ")
    num2 = input("Enter second number: ")
    
    try:
        num1 = float(num1)
        num2 = float(num2)
        
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                print("Error: Cannot divide by zero!")
                continue
            else:
                result = num1 / num2
        else:
            print("Invalid operator! Please use +, -, *, /")
            continue
        
        print(f"Result: {num1} {operator} {num2} = {result}")
    
    except ValueError:
        print("Invalid input! Please enter a valid number.")
          

