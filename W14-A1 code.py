import functools

def log_decorator(func):
    """A decorator that logs function calls, arguments, and results."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Capture input arguments
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        
        print(f"Function name: {func.__name__}")
        print(f"Input arguments: ({signature})")
        
        # Execute the original function
        result = func(*args, **kwargs)
        
        print(f"Result: {result}")
        return result
    return wrapper

@log_decorator
def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

@log_decorator
def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b

def menu():
    # Dictionary for dynamic function calls
    operations = {
        "1": add,
        "2": multiply
    }

    print("Choose an operation:")
    print("1 - Add")
    print("2 - Multiply")
    
    choice = input("Enter the number of the option (or 'q' to quit): ")
    
    if choice.lower() == 'q':
        return False

    if choice in operations:
        try:
            val1 = float(input("Enter the first value: "))
            val2 = float(input("Enter the second value: "))
            
            # Calls the chosen function
            operations[choice](val1, val2)
        except ValueError:
            print("Error: Please enter numbers only.")
    else:
        print("Invalid option!")
    
    return True

if __name__ == "__main__":
    running = True
    while running:
        running = menu()