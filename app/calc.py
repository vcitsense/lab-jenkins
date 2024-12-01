import app
import math

class InvalidPermissions(Exception):
    pass


def add_internal( x, y):    
    return x + y

def substract_internal( x, y):
    
    return x - y

def multiply_internal( x, y):
    if not app.util.validate_permissions(f"{x} * {y}", "user1"):
        raise InvalidPermissions('User has no permissions')

    
    return x * y

def divide_internal( x, y):
    
    if y == 0:
        raise TypeError("Division by zero is not possible")

    return x / y

def power_internal( x, y):
    
    return x ** y

def check_types_internal( x, y):
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise TypeError("Parameters must be numbers")
    
def sqrt_internal( x):
    
    if x < 0:
        raise ValueError("Cannot calculate the square root of a negative number")
    
    return math.sqrt(x)

def log_internal( x):
    
    if x <= 0:
        raise ValueError("Logarithm base 10 is only defined for positive numbers") 
        
    return math.log10(x)

# if __name__ == "__main__":  # pragma: no cover
#     calc = Calculator()
#     result = calc.add(2, 2)
#     print(result)
