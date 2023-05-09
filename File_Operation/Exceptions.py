"""
Исключение — это неожиданное событие, возникающее во время выполнения программы.
Ошибки, возникающие во время выполнения (после прохождения синтаксической проверки), называются исключениями или логическими ошибками .

"""

try:
    x, v = 10, 0
    result = x / v
    print(result)
except ZeroDivisionError:
    print('Error - Fuck')
    # Output: Error - Fuck


# program to print the reciprocal of even numbers
try:
    num = int(input("Enter a number: "))
    assert num % 2 == 0
except:
    print("Not an even number!")
else:
    reciprocal = 1/num
    print(reciprocal)


# block try...except...finally
    try:
        numerator = 10
        denominator = 0

        result = numerator/denominator

        print(result)
    except:
        print("Error: Denominator cannot be 0.")
    finally:
        print("This is finally block.")

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

# Custom Exceptions
# Example: Python User-Defined Exception
# define Python user-defined exceptions


class InvalidAgeException(Exception):
    "Raised when the input value is less than 18"
    pass


# you need to guess this number
number = 18

try:
    input_num = int(input("Enter a number: "))
    if input_num < number:
        raise InvalidAgeException
    else:
        print("Eligible to Vote")

except InvalidAgeException:
    print("Exception occurred: Invalid Age")
