import math

class myMath:
    def __init__(self, a):
        # Initialize the value of a
        self.a = a

    def algebra(self, b):
        # Method to calculate a^2 + 2ab + b^2
        result = self.a**2 + 2*self.a*b + b**2
        print(f"Algebra result: {result}")

    def factorial(self):
        # Method to calculate factorial of a
        if self.a.is_integer() and self.a >= 0:
            result = math.factorial(int(self.a))
            print(f"Factorial of {self.a}: {result}")
        else:
            print("Factorial is only defined for non-negative integers.")

# Example usage
callmath = myMath(2.3)
callmath.factorial()  # This will print an error message as 2.3 is not an integer
callmath.algebra(3)   # This will calculate a^2 + 2ab + b^2 for a=2.3 and b=3
