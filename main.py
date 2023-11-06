#Рівень доступу Protected (внутрішній або захищений)
class MyClass:
    def __init__(self):
        self._protected_attribute = 10 #захищенний атрибут

    def _protected_method(self): #захищенний метод
        print("Це захищений метод")

class SubClass(MyClass):
    def access_protected(self):
        print(self._protected_attribute)
        self._protected_method()

a = MyClass()
obj = SubClass()
#print(dir(a))
print(a._protected_attribute) #моветон
obj.access_protected()
#Рівень доступу Private (приватний)
class MyClass:
    def __init__(self):
        self.__private_attribute = 20

    def __private_method(self):
        print("Це приватний метод")

obj = MyClass()
#print(obj.__private_attribute)
#obj.__private_method()
print(dir(obj))
print(obj._MyClass__private_attribute)
#приклад з банком
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Недостатньо коштів на рахунку")

    def get_balance(self):
        return self.__balance

# Використання:
account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
print(account.__balance)
print(account.get_balance())  # Результат: 1300