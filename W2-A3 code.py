def fibonacci_recursive(n):
   
    if n <= 0:
        return 0  # The 0th Fibonacci number
    elif n == 1:
        return 1  # The 1st Fibonacci number
    else:
        # The nth Fibonacci number is the sum of the (n-1)th and (n-2)th
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def factorial_recursive(n):
    
    if n == 0: # factorial of 0 is 1
        return 1
   
    else:
        return n * factorial_recursive(n - 1)
    

def main():

    N = int(input("Enter N: ")) #input from the user

    if N <= 0:
        print("Please enter a positive integer.")
    else:
        print (f"The {N}th element of the Fibonacci series is: {fibonacci_recursive(N)}")
        print (f"The factorial of {N} is: {factorial_recursive(N)}")

if __name__ == "__main__":

    main()
    