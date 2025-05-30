import datetime

class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

# ЗАДАНИЕ 1

    @property
    def name_items(self):
        return self.__name_items

    @property
    def number_items(self):
        return self.__number_items

# ЗАДАНИЕ 2

    def add_item_to_cheque(self, name):
            if len(name) == 0 or len(name) > 40:
                raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')
            if name not in self.__item_price:
                raise NameError('Позиция отсутствует в товарном справочнике')
            else:
                self.__name_items.append(name)
                self.__number_items += 1

# ЗАДАНИЕ 3

    def delete_item_from_check(self, name):
            if name not in self.__name_items:
                raise NameError('Позиция отсутствует в чеке')
            else:
                self.__name_items.remove(name)
                self.__number_items -= 1

# ЗАДАНИЕ 4

    def check_amount(self):
        total = []
        for product in self.__name_items:
            total.append(self.__item_price[product])
        if self.__number_items > 10:
            total = sum(total) * 0.9
        else:
            total = sum(total)
        return total

# ЗАДАНИЕ 5

    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = []
        total = []
        for product in self.__name_items:
            if self.__tax_rate[product] == 20:
                twenty_percent_tax.append(product)
        for items in twenty_percent_tax:
            total.append(self.__item_price[items])
        if self.__number_items > 10:
            total = (sum(total) * 0.9) * 0.2
        else:
            total = sum(total) * 0.2
        return total

# ЗАДАНИЕ 6

    def ten_percent_tax_calculation(self):
        ten_percent_tax = []
        total = []
        for product in self.__name_items:
            if self.__tax_rate[product] == 10:
                ten_percent_tax.append(product)
        for items in ten_percent_tax:
            total.append(self.__item_price[items])
        if self.__number_items > 10:
            total = (sum(total) * 0.9) * 0.1
        else:
            total = sum(total) * 0.1
        return total

# ЗАДАНИЕ 7

    def total_tax(self):
        return self.twenty_percent_tax_calculation() + self.ten_percent_tax_calculation()

# ЗАДАНИЕ 8

    @staticmethod
    def get_telephone_number(telephone_number):
        full_telephone_number = f'+7{telephone_number}'
        if telephone_number != int(telephone_number):
            raise ValueError(f'Необходимо ввести цифры')
        if len(str(telephone_number)) != 10:    # ЗАМЕНИЛ УСЛОВИЕ "БОЛЕЕ 10" НА "НЕ РАВНО 10", Т.К. ЕСТЬ ТРЕБОВАНИЕ В САМОМ НАЧАЛЕ ЗАДАНИЯ, ЧТО НЕ ПРОСТО БОЛЕЕ 10, А ИМЕННО 10 ЦИФР
            raise NameError(f'Необходимо ввести 10 цифр после "+7"')
        else:
            return full_telephone_number


# ПРОВЕРКА_ПРОВЕРКА_ПРОВЕРКА_ПРОВЕРКА_ПРОВЕРКА

# ЗАДАНИЕ 2
online = OnlineSalesRegisterCollector()
online.add_item_to_cheque('чипсы')
online.add_item_to_cheque('чипсы')
online.add_item_to_cheque('кола')
online.add_item_to_cheque('молоко')
online.add_item_to_cheque('кефир')
online.add_item_to_cheque('кола')
online.add_item_to_cheque('кола')
online.add_item_to_cheque('кола')
online.add_item_to_cheque('кола')
online.add_item_to_cheque('кола')
online.add_item_to_cheque('кола')
online.add_item_to_cheque('кола')
online.add_item_to_cheque('кола')

# ЗАДАНИЕ 1
print(online.name_items)
print(online.number_items)

# ЗАДАНИЕ 3
online.delete_item_from_check('чипсы')
print(online.name_items)
print(online.number_items)

# ЗАДАНИЕ 4
print(online.check_amount())

# ЗАДАНИЕ 5
print(online.twenty_percent_tax_calculation())

# ЗАДАНИЕ 6
print(online.ten_percent_tax_calculation())

# ЗАДАНИЕ 7
print(online.total_tax())

# ЗАДАНИЕ 8

print(online.get_telephone_number(9155556677))