def list_filler():
    """Creates and fill a list with strings from the terminal"""
    list_of_strings = []
    stop = 0
    while stop != 1:
        data = str(input("Введите то что хотите: "))
        if data == "":
            stop = 1
        else:
            list_of_strings.append(data)

    return list_of_strings

def find_less_then_three(some_list):
    """Creates and fill a list with strings with lenght less the 3 from the existing list"""
    result_list =[]
    for item in some_list:
        if len(item) <= 3:
            result_list.append(item)
        else:
            continue
    return result_list

def print_list(some_list):
    """Form beutiful string to print into terminal"""
    text = "["
    for idx, item in enumerate(some_list):
        if idx < len(some_list) - 1:
            text += f"{item}, "
        else:
            text += f"{item}]"
    return text

print("Вводите желаемое количество строк, если хотите прекратить нажмите Enter")
my_list = list_filler()
print("Исходный список: ")
print(print_list(my_list))
result = find_less_then_three(my_list)
print("Список после исполнения кода: ")
print(print_list(result))