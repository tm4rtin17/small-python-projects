import pyinputplus as pyip

num_1 = pyip.inputInt('Enter your first number ')
operator = pyip.inputMenu(['+', '-', '*', '/'], numbered=True)
num_2 = pyip.inputInt('Enter your second number ')

if operator == '+':
  ans = num_1 + num_2
elif operator == '-':
    ans = num_1 - num_2
elif operator == '*':
    ans = num_1 * num_2
elif operator == '/':
    ans = num_1 / num_2

print(f'The solution is {ans}.')