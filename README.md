# -Программа представляет собой набор функций для работы с словарем, содержащим товары и их цены.

Функция calculate_total_price(items) вычисляет суммарную цену всех товаров в словаре. Она инициализирует переменную total_price со значением 0, затем проходит по каждому товару в словаре и добавляет его цену к общей сумме total_price. В конце возвращает полученную сумму.

Функция calculate_average_price(items) вычисляет среднюю цену товаров в словаре. Она вызывает функцию calculate_total_price(items) для получения общей суммы цен, затем делит эту сумму на количество товаров в словаре (len(items)) и сохраняет результат в переменную average_price. В конце возвращает полученное значение.

Функция find_most_expensive_item(items) находит товар с максимальной ценой в словаре. Она инициализирует переменную max_price значением максимальной цены из словаря (используя функцию max(items.values())). Затем проходит по каждому товару в словаре и проверяет, является ли его цена равной max_price. Если да, то возвращает имя этого товара. Если таких товаров несколько, то возвращает только первый найденный.

Пример использования программы:
- Создаем словарь items с товарами и их ценами.
- Вызываем функцию calculate_total_price(items) для вычисления суммарной цены всех товаров и сохраняем результат в переменную total_price.
- Выводим на экран "Суммарная цена: " и значение переменной total_price.
- Вызываем функцию calculate_average_price(items) для вычисления средней цены товаров и сохраняем результат в переменную average_price.
- Выводим на экран "Средняя цена: " и значение переменной average_price.
- Вызываем функцию find_most_expensive_item(items) для поиска товара с максимальной ценой и сохраняем результат в переменную most_expensive_item.
- Выводим на экран "Самый дорогой товар: " и значение переменной most_expensive_item.
