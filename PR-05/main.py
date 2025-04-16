from data_input import input_product
from calculations import *
from general import *

def main():
    products = input_product()
    print(products)

    calculate_stock_value(products)
    calculate_discount(products)

    product_names = list(products.keys())
    print_product_names(product_names)

    # Приклад пошуку товару
    find_product_by_name(products, "Товар 2")

# Отримуємо список назв товарів
# product_names = list(products.keys())
# Викликаємо рекурсивну функцію для виведення назв товарів
# print_product_names(product_names)

if __name__ == "__main__":
    main()