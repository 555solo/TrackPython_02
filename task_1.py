# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
import math


class Book:
    def __init__(self, title: str, author: str, pages: int):
        """
        Создание и подготовка к работе объекта "Книга"

        :param title: Название книги
        :param author: Автор книги
        :param pages: Количество страниц

        Примеры:
        >>> book = Book("1984", "Джордж Оруэлл", 328)  # инициализация экземпляра класса
        """
        if not isinstance(title, str):
            raise TypeError("Название книги должно быть типа str")
        if not title.strip():
            raise ValueError("Название книги не может быть пустой строкой")
        self.title = title

        if not isinstance(author, str):
            raise TypeError("Автор книги должен быть типа str")
        if not author.strip():
            raise ValueError("Автор книги не может быть пустой строкой")
        self.author = author

        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.pages = pages

    def is_thick(self) -> bool:
        """
        Проверяет, является ли книга толстой (более 300 страниц)

        :return: Является ли книга толстой

        Примеры:
        >>> book = Book("1984", "Джордж Оруэлл", 328)
        >>> book.is_thick()
        True
        >>> book = Book("Маленький принц", "Антуан де Сент-Экзюпери", 96)
        >>> book.is_thick()
        False
        """
        return self.pages > 300

    def get_reading_time(self, pages_per_hour: int) -> float:
        """
        Рассчитывает время чтения книги

        :param pages_per_hour: Количество страниц в час
        :raise ValueError: Если количество страниц в час некорректно
        :return: Время чтения в часах

        Примеры:
        >>> book = Book("1984", "Джордж Оруэлл", 328)
        >>> book.get_reading_time(50)
        6.56
        >>> book.get_reading_time(100)
        3.28
        """
        if not isinstance(pages_per_hour, int):
            raise TypeError("Количество страниц в час должно быть типа int")
        if pages_per_hour <= 0:
            raise ValueError("Количество страниц в час должно быть положительным числом")

        return round(self.pages / pages_per_hour, 2)


class Circle:
    def __init__(self, radius: float):
        """
        Создание и подготовка к работе объекта "Круг"

        :param radius: Радиус круга

        Примеры:
        >>> circle = Circle(5.0)  # инициализация экземпляра класса
        """
        if not isinstance(radius, (int, float)):
            raise TypeError("Радиус должен быть типа int или float")
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным числом")
        self.radius = float(radius)

    def get_area(self) -> float:
        """
        Вычисление площади круга

        :return: Площадь круга

        Примеры:
        >>> circle = Circle(5.0)
        >>> circle.get_area()
        78.54
        >>> circle = Circle(2.5)
        >>> circle.get_area()
        19.63
        """
        return round(math.pi * self.radius ** 2, 2)

    def get_circumference(self) -> float:
        """
        Вычисление длины окружности

        :return: Длина окружности

        Примеры:
        >>> circle = Circle(5.0)
        >>> circle.get_circumference()
        31.42
        >>> circle = Circle(10.0)
        >>> circle.get_circumference()
        62.83
        """
        return round(2 * math.pi * self.radius, 2)


class Student:
    def __init__(self, name: str, age: int, student_id: str):
        """
        Создание и подготовка к работе объекта "Студент"

        :param name: Имя студента
        :param age: Возраст студента
        :param student_id: Номер студенческого билета

        Примеры:
        >>> student = Student("Иван Иванов", 20, "СТ-2023-001")  # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Имя должно быть типа str")
        if not name.strip():
            raise ValueError("Имя не может быть пустой строкой")
        self.name = name

        if not isinstance(age, int):
            raise TypeError("Возраст должен быть типа int")
        if age <= 0 or age > 120:
            raise ValueError("Возраст должен быть в диапазоне от 1 до 120 лет")
        self.age = age

        if not isinstance(student_id, str):
            raise TypeError("Номер студенческого билета должен быть типа str")
        if not student_id.strip():
            raise ValueError("Номер студенческого билета не может быть пустой строкой")
        self.student_id = student_id

    def is_adult(self) -> bool:
        """
        Проверяет, является ли студент совершеннолетним (18+ лет)

        :return: Является ли студент совершеннолетним

        Примеры:
        >>> student = Student("Иван Иванов", 20, "СТ-2023-001")
        >>> student.is_adult()
        True
        >>> student = Student("Петр Петров", 16, "СТ-2023-002")
        >>> student.is_adult()
        False
        """
        return self.age >= 18

    def update_age(self, new_age: int) -> None:
        """
        Обновление возраста студента

        :param new_age: Новый возраст
        :raise ValueError: Если новый возраст некорректен

        Примеры:
        >>> student = Student("Иван Иванов", 20, "СТ-2023-001")
        >>> student.update_age(21)
        >>> student.age
        21
        >>> student.update_age(25)
        >>> student.age
        25
        """
        if not isinstance(new_age, int):
            raise TypeError("Возраст должен быть типа int")
        if new_age <= 0 or new_age > 120:
            raise ValueError("Возраст должен быть в диапазоне от 1 до 120 лет")

        self.age = new_age


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации