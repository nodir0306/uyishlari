"""
Calculator() nomli class elon qiling. classga N soni beriladi. Mos ravishda classda plus, minus, multiply, divide, sqrt, pow, mod nomli methodlari bo’lsin.
Masalan:
input: N = 10
calc = Calculator(10)
calc.plus(5)             # N = 15
calc.plus()	         # N = 16
calc.mod(2)             # N = 0
calc.plus()               # N = 1	
calc.multiply(100)   # N = 100
calc.multiply()         # N = 200
calc.minus(40)        # N = 160
calc.minus()            # N = 159
calc.get_answer()  # N ning qiymati 159.
"""
import math

class Calculator:
    def __init__(self, N):
        self.result = N

    def plus(self, son=1):
        self.result += son

    def minus(self, son=1):
        self.result -= son

    def mod(self, N):
        self.result %= N

    def multiply(self, N = 2):
        self.result *= N

    def divide(self, N):
        self.result /= N

    def sqrt(self):
        self.result = math.sqrt(self.result)

    def pow(self, exp):
        self.result **= exp

    def get_answer(self):
        return self.result

N =10
calc = Calculator(10)
calc.plus(5)
calc.plus()
calc.mod(2)
calc.plus()
calc.multiply(100)
calc.multiply()
calc.minus(40)
calc.minus()
print("N=", calc.get_answer())
