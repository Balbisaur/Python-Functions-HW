def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
     if b == 0:
         return 'cannot divide by 0'
     else:
         return a / b


while True:
        a = int(input('first number: '))
        b = int(input('second number: '))
        operation = input('pick an operation:')
        

        if operation == '+':
            print('total:', addition(a, b))

        elif operation == '-':
            print('total:', subtraction(a, b))

        elif operation == '*':
            print('total:', multiplication(a, b))

        elif operation == '/':
            print('total:', division(a, b))


        total = addition(13, 6)
        print(total)

        total = subtraction(13, 3)
        print(total)

        total = multiplication(25,4)
        print(total)

        total = division(24, 6)
        print(total)