"""
Завдання 2
Реалізуйте клас "Кошик для покупок" з можливістю
додавання товарів та підрахунку загальної вартості.
Застосуйте інкапсуляцію для забезпечення правильності
обробки даних."""

class ShoppingCart:
    def __init__(self):
        self.__items = {}#словник товарів

    def add_items(self, product, quanity, price):
        if product not in self.__items:
            self.__items[product] = {'quanity': quanity, 'price': price}
        else:
            self.__items[product]["quanity"] += quanity

    def calculate_total(self):
        total = 0
        for product, data in self.__items.items():
            total += data["quanity"] * data["price"]
        return total

    def display_items(self):
        for product, data in self.__items.items():
            print(f"товар: {product} в кількості {data['quanity']} шт ціна за штуку {data['price']}")

cart = ShoppingCart()
cart.add_items("Телефон", 2, 100)
cart.add_items("Книга", 3, 200)
cart.display_items()
print("Занальна вартість ", cart.calculate_total())


