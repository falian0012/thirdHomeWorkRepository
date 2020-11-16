def my_func(var_1, var_2):
    temp_value = var_1
    while var_2 > 1:
        temp_value *= var_1
        var_2 -=1
    return temp_value

value_1 = float(input())
value_2 = int(input())

print(my_func(value_1, value_2))