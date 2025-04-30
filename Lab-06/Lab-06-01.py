# Lab-06 Task 01
my_list =  [1, 5, 87, 32]
print(my_list)
my_list[1] = 13
print(my_list)
my_list.append(25)
print(my_list)
my_list[1:2] = [4, 5]   # slice assignment
print(my_list)
del my_list[3:5]
print(my_list)
my_list.insert(2, 8)
print(my_list)
my_tuple = tuple(my_list)
print(my_tuple)
my_list.extend(my_tuple)    # працює з iterable
print(my_list)
my_list.pop()
print(my_list)
print(f"""
кортеж: {my_tuple}
кортеж в зворотньому напрямку: {my_tuple[::-1]}
""")    # від початку до кінця зх кроком -1