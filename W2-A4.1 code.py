class MathSeries:

    def __init__(self, N=0):
        self.N = N #number of elements of the series

    def fibonacci_series(n):
        if n <= 0:
            raise ValueError("Fibonacci is not defined for negative numbers.")
        elif n == 1:
            return 1 #considering 1 as first element
    
        series = [0,1] #initializing the series with first two elements
    
        a, b = 0, 1 #aux variables to hold the last two elements
    
        for _ in range(2, n):
            a, b = b, a + b #updating the last two elements
            series.append(b) #appending the next element to the series 
           
        return series #returning the fibonacci series up to n elements

    
if __name__ == "__main__":
    
    N = int(input("Enter N: ")) #input from the user
    series_obj = MathSeries(N) #creating an object of MathSeries class
    if N <= 0:
        print("Please enter a positive integer.") #error message for non-positive integers
    else:
        print("Fibonacci series up to", N, "elements:", MathSeries.fibonacci_series(N))
        