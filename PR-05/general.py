def print_product_names(product_names, index=0):
    # Перевіряємо, чи індекс не виходить за межі списку
    if index < len(product_names):
        # Виводимо назву товару з поточним індексом
        print(product_names[index])
        # Рекурсивно викликаємо функцію з наступним індексом
        print_product_names(product_names, index +1)

def find_product_by_name(products, product_name, index = 0):
    product_keys = list(products.keys())

    if index >= len(product_keys):
        print("Товар не знайдено.")
        return

    if product_keys[index] == product_name:
        product_info = products[product_name]
        print(f"Товар знайдено: {product_name}, Ціна: {product_info['Ціна']}, залишок: {product_info['Залишок']}")
        return

    find_product_by_name(products, product_name, index + 1)