class Calculation:

    def __init__(self, N, act):
        self.N = N
        self.act = act


    def fibonacci_recursive(self, n):
        
            if n <= 0:
                return 0  # The 0th Fibonacci number
            elif n == 1:
                return 1  # The 1st Fibonacci number
            else:
                # The nth Fibonacci number is the sum of the (n-1)th and (n-2)th
                return self.fibonacci_recursive(n - 1) + self.fibonacci_recursive(n - 2)

    def factorial_recursive(self, n):
            
            if n == 0: # factorial of 0 is 1
                return 1
        
            else:
                return n * self.factorial_recursive(n - 1)

    def calculate(self):
        if self.act == 0:
            return self.fibonacci_recursive(self.N)
        elif self.act == 1:
            return self.factorial_recursive(self.N)
        else:
            return "Invalid value"

def main():

    act = int(input("Enter 0 for Fibonacci or 1 for Factorial: ")) #input for action    
    N = int(input("Enter N: ")) #input for the number to be calculated
    

    if N <= 0:
        print("Please enter a positive integer.") #error message for non-positive integers
        return
    
    calc = Calculation(N, act)
    result = calc.calculate()
    if act == 1:
        print (f"The factorial of {N} is: {result}")
    elif act == 0:
        print (f"The {N}th element of the Fibonacci series is: {result}")
    
if __name__ == "__main__":

    main()