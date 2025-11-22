#activity 3 Fibonacci and Factorial

def main():

    Fibo = 1 #smallest Fiboacci element considering the series started as 0, 1
    Factorial = 1 #smallest Factorial 
    i = 1 # aux variables
    
    N = int(input("Enter N: ")) #enter from the user

    j = N # aux variables

    while i < N: #calculating element N of Fibonacci series
        Fibo = Fibo + i
        i = Fibo - i

    print (f"The Nth element of the Fibonacci series is: {Fibo}")

    while j > 0: #calculating factorial
        Factorial = j * Factorial
        j=j-1

    print (f"The Factorial of {N} is: {Factorial}")

if __name__ == "__main__":

    main()

