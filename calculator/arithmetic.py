import math

class Arithmetic:
    
    @staticmethod
    def addition(x, y):
        return x + y

    @staticmethod
    def subtraction(x, y):
        return x - y

    @staticmethod
    def multiplication(x, y):
        return x * y

    @staticmethod
    def division(x, y):
        if y != 0:
            return x / y
        else:
            return "Error: Division by zero"
        
    @staticmethod
    def puissance(x, y): 
        return x ** y
    
    @staticmethod
    def modulo(x, y):
        return x % y            
    