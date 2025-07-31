# Исходные данные
from statistics import mean

purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},]

#Создадим временные переменные
stack_list = []
stack_dict = {}

# ======================
# Первая функция - расчет общей выручки
# ======================

def total_revenue(purchases):
    global stack_list
    for p in purchases:
        price,quantity = p['price'], p['quantity']
        stack_list.append(price * quantity)

    print(f"Общая выручка: {sum(stack_list)}") # Посчитаем общую выручку
    stack_list.clear() # Очистим список

# ======================
# Вторая функция - вывод списка товаров по категориям
# ======================

def items_by_category(purchases):
    global stack_dict
    for p in purchases:
        cat, val = p['category'], p['item']

        if cat not in stack_dict:
            stack_dict[cat] = []

        stack_dict[cat].append(val)

    print(f"Товары по категориям: {stack_dict}")
    stack_dict.clear() # Очистим словарь

# ======================
# Третья функция - вывод покупок, где цена превышает заданное значение.
# ======================

# Определим минимальную цену
min_price = min([p['price'] for p in purchases])

def expensive_purchases(purchases, min_price):
    global stack_list
    stack_list = [p for p in purchases if p['price'] >= min_price]

    print(f"Покупки дороже {min_price}: {stack_list}")
    stack_list.clear() # Очистим список

# ======================
# Четвертая функция - вывод средней цены товаров по категориям.
# ======================

def average_price_by_category(purchases):
    global stack_dict

    for p in purchases:
        cat, price = p['category'], p['price']

        if cat not in stack_dict:
            stack_dict[cat] = []

        stack_dict[cat].append(price)
    stack_dict = {key: mean(value) for key, value in stack_dict.items()}

    print(f"Средняя цена по категориям: {stack_dict}")
    stack_dict.clear()  # Очистим словарь

# ======================
# Пятая функция - вывод категорий с наибольшим числом проданных товаров
# ======================

def most_frequent_category(purchases):
    global stack_dict

    for p in purchases:
        cat, quantity = p['category'], p['quantity']

        if cat not in stack_dict:
            stack_dict[cat] = []

        stack_dict[cat].append(quantity)

    stack_dict = max({key: sum(value) for key, value in stack_dict.items()})

    print(f"Категория с наибольшим количеством проданных товаров: {stack_dict}")

# Запустим функции
try:
    total_revenue(purchases)
    items_by_category(purchases)
    expensive_purchases(purchases, min_price)
    average_price_by_category(purchases)
    most_frequent_category(purchases)
except Exception as e:
    print("Произошла ошибка:", e)
