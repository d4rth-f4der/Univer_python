def swap_array_elements(array, index1, index2):
    array[index1], array[index2] = array[index2], array[index1]

def max_heapify_down(array, index, heap_boundary):
    while True:
        left, right = index * 2 + 1, index * 2 + 2

        if max(left, right) < heap_boundary:
            if array[index] >= max(array[left], array[right]):
                break
            elif array[left] > array[right]:
                swap_array_elements(array, index, left)
                index = left
            else:
                swap_array_elements(array, index, right)
                index = right
        elif left < heap_boundary:
            if array[left] > array[index]:
                swap_array_elements(array, index, left)
                index = left
            else:
                break
        elif right < heap_boundary:
            if array[right] > array[index]:
                swap_array_elements(array, index, right)
                index = right
            else:
                break
        else:
            break

def max_heap_sort(array):
    n = len(array)
    for j in range((n - 2) // 2, -1, -1):
        max_heapify_down(array, j, n)

    for unsorted_last_index in range(n - 1, 0, -1):
        swap_array_elements(array, 0, unsorted_last_index)
        max_heapify_down(array, 0, unsorted_last_index)

def sort_els_in_range_desc(array, min_val, max_val):
    elements_to_sort = []
    indexes_to_sort = []

    for i, element in enumerate(array):
        if min_val < element < max_val:
            elements_to_sort.append(element)
            indexes_to_sort.append(i)

    max_heap_sort(elements_to_sort)

    for i in range(len(elements_to_sort)):
        array[indexes_to_sort[i]] = elements_to_sort[i]

my_array = [34, 0, 16, 2, 10, -9, 48, 5, 17, 51, -6, 7, 94, 54]
min_value = 0
max_value = 30
print(f"Initial array:\n{my_array}")

sort_els_in_range_desc(my_array, min_value, max_value)
print(f"\nArray sorted descending affecting elements with values from {min_value} to {max_value}:\n{my_array}"
      f"\n(elements not within range left unaffected)")