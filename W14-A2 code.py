import functools
import time
import logging

# Configure logging to both a file and the console
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("W14-A2.log"),
        logging.StreamHandler()
    ]
)
def log_decorator(func):
    """
    A decorator that logs function calls, execution time, 
    results, and handles exceptions.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            
            # Log the start of execution with input details
            args_repr = [repr(a) for a in args]
            kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
            signature = ", ".join(args_repr + kwargs_repr)
            
            logging.info(f"Executing: {func.__name__}({signature})")
            
            try:
                # Execute the original function
                result = func(*args, **kwargs)
                
                end_time = time.perf_counter()
                duration = end_time - start_time
                
                # Log success, result, and execution time
                logging.info(f"Result: {result} | Time: {duration:.6f}s")
                return result
                
            except Exception as e:
                # Handle and log any errors that occur during execution
                end_time = time.perf_counter()
                duration = end_time - start_time
                logging.error(f"Error in {func.__name__}: {str(e)} | Failed after {duration:.6f}s")
                return None # Or re-raise with 'raise' depending on desired behavior
                
    return wrapper

@log_decorator
def add(a, b):
    return a + b

@log_decorator
def multiply(a, b):
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
            logging.warning("Invalid input: Please enter numerical values.")
    else:
        print("Invalid option!")
    
    return True

if __name__ == "__main__":
    running = True
    while running:
        running = menu()