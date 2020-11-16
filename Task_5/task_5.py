break_point = True

while break_point:
    list = input().split(" ")
    temp_value = 0
    for item in list:
        if item == "!":
            break_point = False
            break
        temp_value += int(item)
    if break_point:
        print(temp_value)

print("The END!")


