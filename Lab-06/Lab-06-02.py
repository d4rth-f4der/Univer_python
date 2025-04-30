# Lab-06 Task 02
sequence_s = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377,
              610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657]
print(sequence_s[:10])
print(sequence_s[:10][::-1])
print(sequence_s[10:20])
print(sequence_s[-10:])
print(sequence_s[:-11:-1])
print(sequence_s[:(len(sequence_s) + 1) // 2])
print(sequence_s[:len(sequence_s) // 2])
print(sequence_s[:len(sequence_s) // 3])
print(sequence_s[len(sequence_s) // 2:])
print(sequence_s[(len(sequence_s) + 1) // 2:])
print(sequence_s[len(sequence_s) // 3: 2 * (len(sequence_s) // 3)])
print(sequence_s[2::3])
print(sequence_s[2::3][::-1])