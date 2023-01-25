cart = {}

def add_to_cart(item, price):
    try:
        if price <= 0:
            raise ValueError("Invalid price. Price must be greater than 0.")
        cart[item] = price
    except ValueError as e:
        print(e)

def remove_from_cart(item):
    if item in cart:
        del cart[item]
    else:
        print(f"{item} not in cart.")

def update_cart(item, new_price=None, new_item=None):
    try:
        if item not in cart:
            raise ValueError(f"{item} not in cart.")
        if new_price and new_price <= 0:
            raise ValueError("Invalid price. Price must be greater than 0.")
        if new_price:
            cart[item] = new_price
        if new_item:
            cart[new_item] = cart.pop(item)
    except ValueError as e:
        print(e)
        
def view_cart():
    for item, price in cart.items():
        print(f"{item}: ${price:.2f}")

add_to_cart("apple", 0.99)
add_to_cart("banana", 0.59)
add_to_cart("milk", 2.99)

view_cart()

remove_from_cart("banana")

view_cart()

update_cart("milk", new_price=3.49, new_item="whole milk")

view_cart()




Этот код является простым примером программы для работы с корзиной покупок. 
Корзина представлена ​​в виде словаря, где ключ - это название товара, а значение - это цена товара.

Функция add_to_cart(item, price) добавляет товар в корзину с заданной ценой. 
Перед добавлением происходит проверка, что цена больше 0. Если цена меньше или равна 0 генерируется исключение.

Функция remove_from_cart(item) удаляет товар из корзины. Если товар отсутствует в корзине, то выводится сообщение об этом.

Функция update_cart(item, new_price=None, new_item=None) обновляет товар в корзине. 
Принимает товар который нужно обновить, новую цену и новое название товара. 
Перед обновлением проверяет, что товар находится в корзине, цена больше 0. Если какое-либо из этого не соответствует, генерируется исключение.

Функция view_cart() выводит содержимое корзины на экран. Для каждого товара выводится название и цена. Цена округляется до 2 знаков после запятой.

В конце кода есть несколько примеров использования этих функций для добавления товаров в корзину, 
удаления товаров из корзины и обновления товаров в корзине, а также для просмотра содержимого корзины.
