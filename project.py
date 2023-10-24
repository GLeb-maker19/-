def calculate_total_price(items):
  total_price = 0

for item in items:
    price = items[item]
    total_price += price

return total_price

def calculate_average_price(items):
    total_price = calculate_total_price(items)
    average_price = total_price / len(items)

return average_price

def find_most_expensive_item(items):
    max_price = max(items.values())

for item in items:
  if items[item] == max_price:
  return item

# Пример использования

# Словарь с товарами и их ценами
items = {
"Яблоко": 50,
"Банан": 30,
"Груша": 40,
}

# Вычисление суммарной цены
total_price = calculate_total_price(items)
print("Суммарная цена: ", total_price)

# Вычисление средней цены
average_price = calculate_average_price(items)
print("Средняя цена: ", average_price)

# Поиск товара с максимальной ценой
most_expensive_item = find_most_expensive_item(items)
print("Самый дорогой товар: ", most_expensive_item)