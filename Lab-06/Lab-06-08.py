# Lab-06 Task 08
def add_element_if_not_exists(my_list: list, element_to_add):

    if element_to_add not in my_list:
        my_list.append(element_to_add)
        print(f"Елемент '{element_to_add}' додано до списку.")
    else:
        print(f"Елемент '{element_to_add}' вже присутній у списку.")

    element_index = my_list.index(element_to_add)

    return element_index



initial_list = [10, 20, 30, 40]
print(f"Початковий список: {initial_list}")

print("-" * 20)

element1 = 50
index1 = add_element_if_not_exists(initial_list, element1)
print(f"Список після операції: {initial_list}")
print(f"Повернутий індекс елемента '{element1}': {index1}")

print("-" * 20)

element2 = 20
index2 = add_element_if_not_exists(initial_list, element2)
print(f"Список після операції: {initial_list}")
print(f"Повернутий індекс елемента '{element2}': {index2}")

print("-" * 20)

element3 = 5
index3 = add_element_if_not_exists(initial_list, element3)
print(f"Список після операції: {initial_list}")
print(f"Повернутий індекс елемента '{element3}': {index3}")

print("-" * 20)

element4 = 40.0
index4 = add_element_if_not_exists(initial_list, element4)
print(f"Список після операції: {initial_list}")
print(f"Повернутий індекс елемента '{element4}': {index4}")