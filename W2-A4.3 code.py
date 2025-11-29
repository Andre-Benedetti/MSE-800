class MathSeries:
    def __init__(self, n):
        self.n = n  # number for which calculations will be done

    def factorial_recursive(self):
        n_val = self.n

        if n_val < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        
        def _calculate(k):
            if k in (0, 1):
                return 1
            # Chamada recursiva correta usando a função interna.
            return k * _calculate(k - 1)
        
        return _calculate(n_val)

       
    def fibonacci_recursive(self):
        n_val = self.n
        if n_val < 0:
            raise ValueError("Fibonacci is not defined for negative numbers.")
        
        def _calculate(k):
            if k == 0:
                return 0
            if k == 1:
                return 1
            return (_calculate(k - 1) + _calculate(k - 2))

    # New method to print all Fibonacci values up to n
    def fibonacci_series(self):
        n_val = self.n
        series = []
        def _calculate_fib(k):
            if k == 0: return 0
            if k == 1: return 1
            return (_calculate_fib(k - 1) + _calculate_fib(k - 2))
        for i in range(n_val + 1):
            series.append(_calculate_fib(i))

        return series


if __name__ == "__main__":

    N = int(input("Enter N: ")) #input from the user

    # Create an object
    obj1 = MathSeries(N)

    # Print the entire Fibonacci series
    print(f"Fibonacci series (0 to {N}th element):", obj1.fibonacci_series())
