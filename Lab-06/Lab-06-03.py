# Lab-06 Task 02
sequence_s = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377,
              610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657]

def print_sequence_comma(seq):
    if not seq:
        print("Послідовність порожня!")
    else:
        print(seq[0], end="")
        for _ in range(1, len(seq)):
            print(f", {_}", end="")
        print(".")

print_sequence_comma(sequence_s)

sequence_empty = []
print_sequence_comma(sequence_empty)