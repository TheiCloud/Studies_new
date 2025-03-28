class Rectangle:
    def __init__(self, width, length, *kwargs):
        super().__init__(*kwargs)
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length

    def perimetr(self):
        return (self.width + self.width)*2


class BankAccount:
    def __init__(self,  number, balance = 0, region = "RU"):
        self._accountNumber =  number
        self._balance = balance
        self._region = region

    @property
    def balance(self):
        return self._balance

    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, region):
        if region in ["RU", "BR", "SER"]:
            self._region = region
            print(f"Регион усешно изменен на {self._region}")
        else:
            print("Мы не обслуживаем ваш регион или вы ввели регион не корректно")

    def add_sum(self, summ):
        self._balance+=summ

    def withdraw(self, summ):
        if summ > self._balance:
            print("Недостаточно средств")
        else:
            self._balance-=summ
            print(f"Снятие прошло успешно, на балансе осталось {self._balance} $")

from abc import ABC, abstractmethod
class Course(ABC):
    def __init__(self, name, price, duration_hours):
        self.name = name
        self.price = price
        self.duration_hours = duration_hours


    @abstractmethod
    def calculate_rating(self):
        """Рейтинг = цена / количество часов"""
        return self.price / self.duration_hours


class OnlineCourse(Course):
    def calculate_rating(self):
        base_rating = super().calculate_rating()
        return base_rating * 0.8  # Уменьшаем рейтинг на 20%


class OfflineCourse(Course):
    def calculate_rating(self):
        base_rating = super().calculate_rating()
        return base_rating * 1.2  # Увеличиваем рейтинг на 20%



python_online = OnlineCourse("Python Online", 10000, 40)
print(f"Рейтинг онлайн-курса: {python_online.calculate_rating():.1f} руб/час")

java_offline = OfflineCourse("Java Offline", 15000, 30)
print(f"Рейтинг оффлайн-курса: {java_offline.calculate_rating():.1f} руб/час")