def divide():
    try:
        number_of_operands = int(input('Please enter the number of operands: '))
    except ValueError:
        number_of_operands = int(input('That input is not valid. Please enter an integer greater than one: '))
    finally:
        while(number_of_operands < 2):
            number_of_operands = int(input('That input is not valid. Please enter an integer greater than one: '))
    try:
        result = float(input('Please enter the first number: '))
    except ValueError:
        result = float(input('That input is not valid! Please enter a number: '))
    finally:
        i = 1
    while(i < number_of_operands):
        try:
            result = result / float(input('Please enter the next number: '))
        except ZeroDivisionError:
            print('The result of dividing by zero is undefined! (However, you can evaluate the limit of a function as its denominator approaches zero.)')
            result = result / float(input('Please enter a different denominator: '))
        except ValueError:
            result = result / float(input('That input is not valid! Please enter a number: '))
        finally:
            i = i + 1    # i++ doesn't work
    return result