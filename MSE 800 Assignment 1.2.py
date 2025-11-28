import math

def main():

    N = int(input("Enter N: ")) #enter from the user

    
    phi = (1 + math.sqrt(5)) / 2 #aux variable
    nth_fib=round((phi ** N - (1 - phi) ** N) / math.sqrt(5)) #calculatin the N th term using Binet's formula


    print(f"The {N}th Fibonacci number is: {nth_fib}")

if __name__ == "__main__":

    main()