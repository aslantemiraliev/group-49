class Figure:
    """
    Базовый класс Figure (фигура).
    """
    unit = "cm"  # Единица измерения по умолчанию

    def __init__(self):
        pass  # Конструктор без атрибутов объекта

    def calculate_area(self):
        """
        Нереализованный метод для подсчета площади.
        """
        raise NotImplementedError("Метод calculate_area должен быть реализован в подклассе.")

    def info(self):
        """
        Нереализованный метод для вывода информации о фигуре.
        """
        raise NotImplementedError("Метод info должен быть реализован в подклассе.")


class Square(Figure):
    """
    Класс Square (квадрат), наследуется от Figure.
    """

    def __init__(self, side_length: float):
        super().__init__()
        self.__side_length = side_length  # Приватный атрибут длины стороны

    def calculate_area(self):
        """
        Рассчитывает площадь квадрата.
        """
        return self.__side_length ** 2

    def info(self):
        """
        Выводит информацию о квадрате.
        """
        area = self.calculate_area()
        print(f"Square side length: {self.__side_length}{self.unit}, area: {area}{self.unit}.")


class Rectangle(Figure):
    """
    Класс Rectangle (прямоугольник), наследуется от Figure.
    """

    def __init__(self, length: float, width: float):
        super().__init__()
        self.__length = length  # Приватный атрибут длины
        self.__width = width  # Приватный атрибут ширины

    def calculate_area(self):
        """
        Рассчитывает площадь прямоугольника.
        """
        return self.__length * self.__width

    def info(self):
        """
        Выводит информацию о прямоугольнике.
        """
        area = self.calculate_area()
        print(f"Rectangle length: {self.__length}{self.unit}, width: {self.__width}{self.unit}, area: {area}{self.unit}.")


if __name__ == "__main__":
    # Создаем список фигур
    shapes = [
        Square(5),
        Square(8),
        Rectangle(5, 10),
        Rectangle(7, 3),
        Rectangle(6, 4)
    ]

    # Вызываем метод info у всех объектов
    for shape in shapes:
        shape.info()
