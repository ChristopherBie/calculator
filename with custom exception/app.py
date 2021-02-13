import addition
import subtraction
import multiplication
import division

def calculate():
    print('What would you like to do?')
    print('1. add')
    print('2. subtract')
    print('3. multiply')
    print('4. divide')

    print()
    try:
        operation = int(input(''))
    except ValueError:
        operation = int(input('That is not valid input. Please enter 1, 2, 3 or 4: '))
    finally:
        while(operation != 1 and operation != 2 and operation != 3 and operation != 4):    #the function would not work properly with the
            operation = int(input('That is not valid input. Please enter 1, 2, 3 or 4: '))     #while loop nested in an except statement
    if(operation == 1):
        print('You chose to add.')
        result = addition.add()
    elif(operation == 2):
        print('You chose to subtract.')
        result = subtraction.subtract()
    elif(operation == 3):
        print('You chose to multiply.')
        result = multiplication.multiply()
    elif(operation == 4):
        print('You chose to divide.')
        result = division.divide()
    print()
    print('The result is ' + str(result))

calculate()