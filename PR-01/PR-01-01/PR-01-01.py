# Введення тексту

text = input("Введіть текст для аналізу: ")

# print(f"{}") дозволяє вставити значення змінної в {}
print(f"Аналіз тексту: {text}")

# Розділити текст на слова та речення - пробіл відокремлює слова, крапка - речення
words = text.split(" ")
sentences = text.split(".")

print(words)
print(sentences)

# Імпорт бібліотеки
import math

# Підрахунок загальної кількості речень і слів у введеному тексті
count = len(sentences)
word_count = len(words)

# Підрахунок середньої кількості слів на 1 речення
if count > 0:
    average_words_per_sentence = word_count / count
else:
    average_words_per_sentence = 0

# Виводимо статистику
print(f"Кількість речень: {count}")
print(f"Кількість слів: {word_count}")
print(f"Середня кількість слів у реченні: "
      f"{math.ceil(average_words_per_sentence)}")