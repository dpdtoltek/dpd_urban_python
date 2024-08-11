from pprint import pprint


class Product:

    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'
        name = self.__file_name
        file = open(name, 'a')
        file.write(f'')
        file.close()

    def get_products(self):
        name = self.__file_name
        file = open(name, 'r')
        date = file.read()
        file.close()
        return date

    def add(self, *products):
        self.products = products

        for i in self.products:
            if i.name not in s1.get_products():
                name = self.__file_name
                file = open(name, 'a')
                file.write(f'{i.name}, {i.weight}, {i.category}\n')
                file.close()
            elif i.name in s1.get_products():
                print(f'Продукт {i.name} уже есть в магазине')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
