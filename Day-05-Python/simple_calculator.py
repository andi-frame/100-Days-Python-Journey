print('''
===================================
!! WELCOME TO SIMPLE CALCULATOR !!
===================================
• Working on float numbers
• Simple operations (+, -, *, /, %)
-----------------------------------
''')
def addition(first_num, second_num):
    return first_num + second_num
def subtract(first_num, second_num):
    return first_num - second_num
def multiply(first_num, second_num):
    return first_num * second_num
def divide(first_num, second_num):
    return first_num / second_num
def modulo(first_num, second_num):
    return first_num % second_num

operator = {'+':addition, '-':subtract, '*':multiply, '/':divide, '%':modulo}

is_continue = True
while is_continue:
    first_num = float(input("The first number: "))
    operation = input("Please choose the operation (+, -, *, /, %): ")
    while operation == ('+' and '-' and '*' and '/' and '%'): 
        print("Please input the available operation")
        operation = input("Please choose the operation (+, -, *, /, %): ")
    second_num = float(input("The second number: "))
    print(f"{first_num} {operation} {second_num} = {operator[operation](first_num, second_num)}")