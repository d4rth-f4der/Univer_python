def calculate_stock_value(product_info):
    for product, details in product_info.items():
        stock_value = details['Ціна'] * details['Залишок']
        print(f"Вартість залишку для {product}: {stock_value}")

# calculate_stock_value(products)

def calculate_discount(product_info):
    for product, details in product_info.items():
        if details['Залишок'] < 10:
            discount = details['Ціна'] * 0.05 # 5% знижка
            print(f"Знижка для {product}: {discount} ({details['Ціна']} - 5%)")
        else:
            print(f"Для {product} знижка не застосовується, оскільки залишок становить {details['Залишок']} одиниць")

# calculate_discount(products)