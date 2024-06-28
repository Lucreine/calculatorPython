import tkinter as tk
from tkinter import *
import tkinter.messagebox as messagebox
from arithmetic import Arithmetic
from trigonometric import Trigonometry
from exponential import Exponential
from conversion import BaseConversion
import math

calc_input = "0"

bg_color = "#f0f0f0"  
button_bg = "#444"  
button_fg = "#FFF"  
result_fg = "#333333" 
result_bg = "#d9d9d9"

def digit(value):
    global calc_input
    calc_input += value
    print(calc_input)

def input_key(key):
    global calc_input
    if calc_input == "0":
        calc_input = key
    else:
        calc_input += key
    calc_input_text.set(calc_input)
    print(calc_input)
    
def backspace():
    global calc_input
    if len(calc_input) > 1:
        calc_input = calc_input[:-1]
    else:
        calc_input = "0"
    calc_input_text.set(calc_input)

def empty():
    global calc_input
    calc_input = "0"
    calc_input_text.set(calc_input)

def comma():
    global calc_input
    if calc_input and calc_input[-1].isdigit():
        calc_input += "."
        calc_input_text.set(calc_input)
    elif not calc_input:
        calc_input += "0."
        calc_input_text.set(calc_input)

def parse_expression(expression):
    operators = set('+-x÷^%')
    stack = []
    num = ""
    trig_function = ""
    is_trig = False
    i = 0

    while i < len(expression):
        char = expression[i]
        
        if char in operators:
            if num:
                stack.append(float(num))
                num = ""
            stack.append(char)
        
        elif char.isdigit() or char == '.':
            num += char
        
        elif char.isalpha():
            trig_function += char
            is_trig = True
        
        elif char == '√':
            j = i + 1
            if expression[j] == '(':
                j += 1
                arg = ""
                while expression[j] != ')':
                    arg += expression[j]
                    j += 1
                arg_value = float(arg)
                stack.append(math.sqrt(arg_value))
                i = j
            else:
                arg = ""
                while j < len(expression) and (expression[j].isdigit() or expression[j] == '.'):
                    arg += expression[j]
                    j += 1
                arg_value = float(arg)
                stack.append(math.sqrt(arg_value))
                i = j - 1
        
        elif char == '(':
            if is_trig:
                j = i + 1
                arg = ""
                while expression[j] != ')':
                    arg += expression[j]
                    j += 1
                arg_value = float(arg)
                if trig_function == 'sin':
                    stack.append(Trigonometry.sinus(arg_value))
                elif trig_function == 'cos':
                    stack.append(Trigonometry.cosinus(arg_value))
                elif trig_function == 'tan':
                    stack.append(Trigonometry.tangente(arg_value))
                elif trig_function == 'ln':
                    stack.append(Exponential.ln(arg_value))
                elif trig_function == 'log':
                    stack.append(Exponential.log(arg_value))
                elif trig_function == 'e':
                    stack.append(Exponential.exp(arg_value))
                i = j
                trig_function = ""
                is_trig = False
        
        i += 1

    if num:
        stack.append(float(num))
    return stack

def calculate_expression(stack):
    operators = {
        '+': Arithmetic.addition,
        '-': Arithmetic.subtraction,
        'x': Arithmetic.multiplication,
        '÷': Arithmetic.division,
        '^': Arithmetic.puissance,
        '%': Arithmetic.modulo
    }
    result = stack[0]
    i = 1
    while i < len(stack):
        operator = stack[i]
        next_num = stack[i + 1]
        result = operators[operator](result, next_num)
        i += 2
    return result

def equal():
    global calc_input, last_was_operator
    try:
        stack = parse_expression(calc_input)
        result = calculate_expression(stack)
        calc_input = str(result)
        calc_input_text.set(calc_input)
        last_was_operator = False
    except Exception as e:
        messagebox.showerror(f"Error", f"Please check what you wrote: {e}")
    print(result)

window = Tk()
window.title("Scientific Calculator")
window.geometry("500x400")
window.config(bg=bg_color)


Button(window, text="Close", bg=button_bg, fg=button_fg, font=("Arial", 16), command=window.quit, width=5).grid(row=0, column=4)
Button(window, text="0" , bg=button_bg, fg=button_fg, font=("Arial", 16), command=lambda: input_key("0"), width=5).grid(row=7, column=0)
Button(window, text="1" , bg=button_bg, fg=button_fg, font=("Arial", 16), command=lambda: input_key("1"), width=5).grid(row=6, column=0)
Button(window, text="2" , bg=button_bg, fg=button_fg, font=("Arial", 16), command=lambda: input_key("2"), width=5).grid(row=6, column=1)
Button(window, text="3" , bg=button_bg, fg=button_fg, font=("Arial", 16), command=lambda: input_key("3"), width=5).grid(row=6, column=2)
Button(window, text="4" , bg=button_bg, fg=button_fg, font=("Arial", 16), command=lambda: input_key("4"), width=5).grid(row=5, column=0)
Button(window, text="5" , bg=button_bg, fg=button_fg, font=("Arial", 16), command=lambda: input_key("5"), width=5).grid(row=5, column=1)
Button(window, text="6" , bg=button_bg, fg=button_fg, font=("Arial", 16), command=lambda: input_key("6"), width=5).grid(row=5, column=2)
Button(window, text="7" , bg=button_bg, fg=button_fg, font=("Arial", 16), command=lambda: input_key("7"), width=5).grid(row=4, column=0)
Button(window, text="8" , bg=button_bg, fg=button_fg, font=("Arial", 16), command=lambda: input_key("8"), width=5).grid(row=4, column=1)
Button(window, text="9" , bg=button_bg, fg=button_fg, font=("Arial", 16), command=lambda: input_key("9"), width=5).grid(row=4, column=2)
Button(window, text="+" , bg=button_bg, fg=button_fg, font=("Arial", 16), command=lambda: input_key("+"), width=5).grid(row=4, column=3)
Button(window, text="-" , bg=button_bg, fg=button_fg, font=("Arial", 16), command=lambda: input_key("-"), width=5).grid(row=5, column=3)
Button(window, text="x" , bg=button_bg, fg=button_fg, font=("Arial", 16), command=lambda: input_key("x"), width=5).grid(row=6, column=3)
Button(window, text="÷" , bg=button_bg, fg=button_fg, font=("Arial", 16), command=lambda: input_key("÷"), width=5).grid(row=7, column=3)
Button(window, text="C" , bg=button_bg, fg=button_fg, font=("Arial", 16), command=backspace, width=5).grid(row=3, column=3)
Button(window, text="," , bg=button_bg, fg=button_fg, font=("Arial", 16), command=comma, width=5).grid(row=7, column=1)
Button(window, text="sin" , bg=button_bg, fg=button_fg, font=("Arial", 16), command=lambda: input_key("sin("), width=5).grid(row=3, column=0)
Button(window, text="cos" , bg=button_bg, fg=button_fg, font=("Arial", 16), command=lambda: input_key("cos("), width=5).grid(row=3, column=1)
Button(window, text="tan" , bg=button_bg, fg=button_fg, font=("Arial", 16), command=lambda: input_key("tan("), width=5).grid(row=3, column=2)
Button(window, text="sqrt" , bg=button_bg, fg=button_fg, font=("Arial", 16), command=lambda: input_key("√("), width=5).grid(row=3, column=4)
Button(window, text="exp" , bg=button_bg, fg=button_fg, font=("Arial", 16), command=lambda: input_key("e("), width=5).grid(row=4, column=4)
Button(window, text="ln" , bg=button_bg, fg=button_fg, font=("Arial", 16), command=lambda: input_key("ln("), width=5).grid(row=5, column=4)
Button(window, text="log" , bg=button_bg, fg=button_fg, font=("Arial", 16), command=lambda: input_key("log("), width=5).grid(row=6, column=4)
Button(window, text="P" , bg=button_bg, fg=button_fg, font=("Arial", 16), command=lambda: input_key("^"), width=5).grid(row=7, column=4)
Button(window, text="(" , bg=button_bg, fg=button_fg, font=("Arial", 16), command=lambda: input_key("("), width=5).grid(row=8, column=0)
Button(window, text=")" , bg=button_bg, fg=button_fg, font=("Arial", 16), command=lambda: input_key(")"), width=5).grid(row=8, column=1)
Button(window, text="%" , bg=button_bg, fg=button_fg, font=("Arial", 16), command=lambda: input_key("%"),width=5).grid(row=8, column=2)
Button(window, text="AC" , bg=button_bg, fg=button_fg, font=("Arial", 16), command=empty, width=5).grid(row=8, column=3)
Button(window, text="bin" , bg=button_bg, fg=button_fg, font=("Arial", 16), command=lambda: input_key("bin"), width=5).grid(row=9, column=0)
Button(window, text="oct" , bg=button_bg, fg=button_fg, font=("Arial", 16), command=lambda: input_key("oct"), width=5).grid(row=9, column=1)
Button(window, text="hex" , bg=button_bg, fg=button_fg, font=("Arial", 16), command=lambda: input_key("hex"), width=5).grid(row=9, column=2)
Button(window, text="dec" , bg=button_bg, fg=button_fg, font=("Arial", 16), command=lambda: input_key("dec"), width=5).grid(row=9, column=3)
Button(window, text="=", bg=button_bg, fg=button_fg, font=("Arial", 16), command=equal, width=5).grid(row=7, column=2)

calc_input_text = StringVar()
calc_input_text.set("0")
Label(window).grid(row=2, column=0, columnspan=5)
affichage = Entry(window, width=30, textvariable=calc_input_text, borderwidth=5, font=('Arial', 14)).grid(row=1, column=0, columnspan=5)

window.mainloop()
