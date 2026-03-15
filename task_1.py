class Vehicle:
    """Базовый класс для всех транспортных средств."""

    def __init__(self, brand: str, speed: int):
        """
        Инициализация транспортного средства.

        :param brand: Марка транспортного средства
        :param speed: Максимальная скорость (км/ч)
        """
        self.brand = brand
        self._speed = speed  # непубличный атрибут для инкапсуляции

    def get_speed(self) -> int:
        """Получить максимальную скорость."""
        return self._speed

    def move(self) -> str:
        """Метод движения (будет переопределен в дочерних классах)."""
        return "Транспортное средство движется"

    def __str__(self) -> str:
        """Строковое представление для пользователя."""
        return f"Транспорт: {self.brand}, скорость: {self._speed} км/ч"

    def __repr__(self) -> str:
        """Официальное строковое представление для разработчика."""
        return f"{self.__class__.__name__}(brand={self.brand!r}, speed={self._speed})"


class Car(Vehicle):
    """Класс для легкового автомобиля."""

    def __init__(self, brand: str, speed: int, doors: int):
        """
        Инициализация автомобиля.

        :param brand: Марка автомобиля
        :param speed: Максимальная скорость
        :param doors: Количество дверей
        """
        super().__init__(brand, speed)  # вызов конструктора базового класса
        self._doors = doors  # непубличный атрибут

    def get_doors(self) -> int:
        """Получить количество дверей."""
        return self._doors

    def move(self) -> str:
        """
        Перегруженный метод движения.

        Причина перегрузки: автомобиль едет по дороге, а не просто "движется".
        """
        return f"Автомобиль {self.brand} едет по дороге со скоростью {self._speed} км/ч"

    def honk(self) -> str:
        """Новый метод: сигнал автомобиля."""
        return "Бип-бип!"

    def __str__(self) -> str:
        """Перегруженный магический метод."""
        return f"Автомобиль: {self.brand}, скорость: {self._speed} км/ч, дверей: {self._doors}"


class Boat(Vehicle):
    """Класс для лодки."""

    def __init__(self, brand: str, speed: int, capacity: int):
        """
        Инициализация лодки.

        :param brand: Марка лодки
        :param speed: Максимальная скорость
        :param capacity: Вместимость (человек)
        """
        super().__init__(brand, speed)
        self._capacity = capacity

    def get_capacity(self) -> int:
        """Получить вместимость."""
        return self._capacity

    def move(self) -> str:
        """
        Перегруженный метод движения.

        Причина перегрузки: лодка плывет по воде, а не просто "движется".
        """
        return f"Лодка {self.brand} плывет по воде со скоростью {self._speed} км/ч"

    def anchor(self) -> str:
        """Новый метод: бросить якорь."""
        return "Якорь брошен!"

    def __str__(self) -> str:
        """Перегруженный магический метод."""
        return f"Лодка: {self.brand}, скорость: {self._speed} км/ч, вместимость: {self._capacity} чел."


if __name__ == "__main__":
    # Демонстрация работы
    print("=" * 40)
    print("ТРАНСПОРТНЫЕ СРЕДСТВА")
    print("=" * 40)

    # Создание объектов
    car = Car("Toyota", 180, 4)
    boat = Boat("Yamaha", 60, 6)

    # Демонстрация __str__ и __repr__
    print("\n1. СТРОКОВЫЕ ПРЕДСТАВЛЕНИЯ:")
    print(f"car: {car}")
    print(f"car.__repr__(): {repr(car)}")
    print(f"boat: {boat}")
    print(f"boat.__repr__(): {repr(boat)}")

    # Демонстрация унаследованного метода
    print("\n2. УНАСЛЕДОВАННЫЙ МЕТОД (get_speed):")
    print(f"Скорость автомобиля: {car.get_speed()} км/ч")
    print(f"Скорость лодки: {boat.get_speed()} км/ч")

    # Демонстрация перегруженного метода
    print("\n3. ПЕРЕГРУЖЕННЫЙ МЕТОД (move):")
    print(car.move())
    print(boat.move())

    # Демонстрация новых методов
    print("\n4. НОВЫЕ МЕТОДЫ:")
    print(f"Автомобиль сигналит: {car.honk()}")
    print(f"Лодка: {boat.anchor()}")

    # Демонстрация инкапсуляции
    print("\n5. ИНКАПСУЛЯЦИЯ (доступ через методы):")
    print(f"Дверей у автомобиля: {car.get_doors()}")
    print(f"Вместимость лодки: {boat.get_capacity()} человек")