def int_func(string):
    list = string.split(" ")
    temp_list = []
    for item in list:
        temp_item = chr(ord(item[0]) - 32) + item[1:]
        temp_list.append(temp_item)
    return " ".join(temp_list)


    # return string.title()

print(int_func('atext rewrwe tewtwer rrrw'))
