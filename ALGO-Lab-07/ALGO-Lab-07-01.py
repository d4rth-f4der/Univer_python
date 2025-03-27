def odd_even_sort_decreasing(array):
    for index, element in enumerate(array):
        if element % 2 != 0:
            first_odd_index = index
            break
    print(f"\nfirst odd element: {array[index]}, index: {index}")
    n = len(array)
    is_sorted = 0
    while is_sorted == 0:
        is_sorted = 1
        for i in range(first_odd_index + 2, n - 1, 2):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                is_sorted = 0

        for i in range(first_odd_index + 1, n - 1, 2):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                is_sorted = 0
    return

array = [34, 0, 16, 2, 10, -9, 48, 5, 17, 51, -6, 7, 94, 54]
print("Unsorted array:", array)

odd_even_sort_decreasing(array)
print(f"\narray sorted (decreasing) starting after 1st odd:\n{array}")