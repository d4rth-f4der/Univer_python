# Лабораторна 7, завдання 19
import numpy as np

def compare_numpy(v1, v2):
    if v1.shape != v2.shape:
        return None

    if np.array_equal(v1, v2):
        return 0
    unequal_indices = np.where(v1 != v2)[0]
    first_diff_index = unequal_indices[0]

    if v1[first_diff_index] < v2[first_diff_index]:
        return -1
    else:
        return 1

print("# Лабораторна 7, завдання 19 (Функція compare_numpy)")

np_vector_a = np.array([True, False, True], dtype=bool)
np_vector_b = np.array([True, False, True], dtype=bool)
np_vector_c = np.array([True, True, False], dtype=bool)
np_vector_d = np.array([False, True, True], dtype=bool)
np_vector_e = np.array([True, False, False], dtype=bool)
np_vector_f = np.array([True, False], dtype=bool)
np_vector_g = np.array([], dtype=bool)
np_vector_h = np.array([], dtype=bool)


print(f"\ncompare_numpy({np_vector_a}, {np_vector_b}) -> {compare_numpy(np_vector_a, np_vector_b)}")
print(f"compare_numpy({np_vector_a}, {np_vector_c}) -> {compare_numpy(np_vector_a, np_vector_c)}")
print(f"compare_numpy({np_vector_a}, {np_vector_d}) -> {compare_numpy(np_vector_a, np_vector_d)}")
print(f"compare_numpy({np_vector_a}, {np_vector_e}) -> {compare_numpy(np_vector_a, np_vector_e)}")
print(f"compare_numpy({np_vector_a}, {np_vector_f}) -> {compare_numpy(np_vector_a, np_vector_f)}")
print(f"compare_numpy({np_vector_f}, {np_vector_a}) -> {compare_numpy(np_vector_f, np_vector_a)}")
print(f"compare_numpy({np_vector_g}, {np_vector_h}) -> {compare_numpy(np_vector_g, np_vector_h)}")