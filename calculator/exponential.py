import math

class Exponential:

    @staticmethod
    def ln(x):
        if x > 0:
            return math.log(x)
        else:
            return "Error: Input must be greater than 0"
    
    @staticmethod
    def log(x):
        if x > 0:
            return math.log10(x)
        else:
            return "Error: Input must be greater than 0"
        
    @staticmethod
    def exp(x):
        return math.exp(x)
    