class Calculation:

    if act == 0:
        def fibonacci_recursive(n):
        
            if n <= 0:
                return 0  # The 0th Fibonacci number
            elif n == 1:
                return 1  # The 1st Fibonacci number
            else:
                # The nth Fibonacci number is the sum of the (n-1)th and (n-2)th
                return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

    else:
        def factorial_recursive(n):
            
            if n == 0: # factorial of 0 is 1
                return 1
        
            else:
                return n * factorial_recursive(n - 1)


def main():

    N = int(input("Enter N: ")) #input for the number to be calculated
    act = int(input("Enter 0 for Fibonacci or 1 for Factorial: ")) #input for action

    if N <= 0:
        print("Please enter a positive integer.") #error message for non-positive integers

    if act ==0:
        print (f"The {N}th element of the Fibonacci series is: {Calculation(N),0}")
    
    elif act ==1:    
            print (f"The {N}th element of the Fibonacci series is: {Calculation(N),0}")
               
    else:
        print("Please enter a valid option for calculation.")


if __name__ == "__main__":

    main()