class Product:
    """
    Класс продукта
    """
    name: str
    price: float
    description: str
    quantity: int

    def __init__(self, name, price, description, quantity):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity

    def check_quantity(self, quantity) -> bool:
        return self.quantity >= quantity

    def buy(self, quantity):
        if self.check_quantity(quantity):  # проверка наличия продукта
            self.quantity -= quantity  # уменьшение количества продукта
        else:
            raise ValueError("Not enough products")  # выброс исключения если продукта не хватает

    def __hash__(self):
        return hash(self.name + self.description)


class Cart:
    """
    Класс корзины. В нем хранятся продукты, которые пользователь хочет купить.
    """

    # Словарь продуктов и их количество в корзине
    products: dict[Product, int]

    def __init__(self):
        # По-умолчанию корзина пустая
        self.products = {}

    def add_product(self, product: Product, buy_count=1):
        """
        Метод добавления продукта в корзину.
        Если продукт уже есть в корзине, то увеличиваем количество
        """
        if product in self.products:  # проверка наличия продукта в корзине
            self.products[product] += buy_count  # увеличение количества продукта в корзине, если он уже есть
        else:
            self.products[product] = buy_count  # добавление продукта в корзину

    def remove_product(self, product: Product, remove_count=None):
        """
        Метод удаления продукта из корзины.
        Если remove_count не передан, то удаляется вся позиция
        Если remove_count больше, чем количество продуктов в позиции, то удаляется вся позиция
        """
        if product in self.products:  # проверка наличия продукта в корзине
            if remove_count is None or self.products[product] <= remove_count:  # проверка наличия remove_count
                del self.products[product]  # удаление продукта из корзины
            else:
                self.products[product] -= remove_count  # уменьшаем количество продукта в корзине

    def clear(self):
        self.products.clear()  # очистка корзины

    def get_total_price(self) -> float:
        total = 0  # общая стоимость
        for product, count in self.products.items():  # перебор продуктов в корзине
            total += product.price * count  # подсчет общей стоимости
        return total  # возвращение общей стоимости

    def buy(self):
        """
        Метод покупки.
        Учтите, что товаров может не хватать на складе.
        В этом случае нужно выбросить исключение ValueError
        """
        for product, thing in self.products.items():  # перебор продуктов в корзине
            if product.quantity < thing:  # проверка наличия продукта на складе
                raise ValueError('Not enough products')  # выброс исключения если продукта не хватает
            else:
                product.buy(thing)  # покупка продукта
        self.clear()
