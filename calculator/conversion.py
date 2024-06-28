class BaseConversion:
    
    @staticmethod
    def binary(x):
        return bin(int(x))[2:]

    @staticmethod
    def octal(x):
        return oct(int(x))[2:]

    @staticmethod
    def hexadecimal(x):
        return hex(int(x))[2:].upper()

    
    @staticmethod
    def decimal(x, base):
        if base == 2:
            return int(str(x), 2)
        elif base == 8:
            return int(str(x), 8)
        elif base == 10:
            return int(str(x), 10)
        elif base == 16:
            return int(str(x), 16)
        else:
            return "Error: Base must be 2, 8, 10, or 16"