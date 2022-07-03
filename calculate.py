import random
import time

def check (input_number, answer):
    if input_number == "exit" or input_number == "quit":
        return -1
    elif input_number == answer:
        print('Correct!')
        return 1
    else:
        print('Try again!')
        return 0
a = 1
result = 1
while True:
    if result == 1:
        a = random.randint(1, 3)
        num1 = random.randint(0, 30)
        num2 = random.randint(0, 30)
    if a == 1:
        print(str(num1) + " + " + str(num2) + " = ")
        answer = num1 + num2
        input_word = input()
        result = check(input_word, str(answer))
        if result == -1:
            break
    else:
        if num1 > num2:
            print(str(num1) + " - " + str(num2))
            answer = num1 - num2
        else:
            print(str(num2) + " - " + str(num1))
            answer = num2 - num1
        input_word = input()
        result = check(input_word, str(answer))
        if result == -1:
            break
