first_user_value = int(input())
second_user_value = int(input())

def divideNumbers(first_number, second_number):
    try:
        print(first_number / second_number)
    except Exception as err:
        print(err)

divideNumbers(first_user_value, second_user_value)