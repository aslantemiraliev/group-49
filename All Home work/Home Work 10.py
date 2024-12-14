class Person:
    """
    Класс Person представляет человека с именем, возрастом и статусом семейного положения.
    """
    def __init__(self, full_name: str, age: int, is_married: bool):
        self.full_name = full_name
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        """
        Выводит информацию о человеке.
        """
        married_status = "замужем/женат" if self.is_married else "не замужем/не женат"
        print(f"Имя: {self.full_name}\nВозраст: {self.age}\nСемейное положение: {married_status}")


class Student(Person):
    """
    Класс Student наследуется от Person и дополнен атрибутом marks.
    """
    def __init__(self, full_name: str, age: int, is_married: bool, marks: dict):
        super().__init__(full_name, age, is_married)
        self.marks = marks

    def calculate_average_mark(self):
        """
        Подсчитывает среднюю оценку студента по всем предметам.
        """
        total_marks = sum(self.marks.values())
        num_subjects = len(self.marks)
        return total_marks / num_subjects if num_subjects > 0 else 0

    def introduce_myself(self):
        """
        Расширяет метод родителя для отображения оценок.
        """
        super().introduce_myself()
        print("Оценки по предметам:")
        for subject, mark in self.marks.items():
            print(f"{subject}: {mark}")


class Teacher(Person):
    """
    Класс Teacher наследуется от Person и дополнен атрибутами experience и base_salary.
    """
    base_salary = 30000

    def __init__(self, full_name: str, age: int, is_married: bool, experience: int):
        super().__init__(full_name, age, is_married)
        self.experience = experience

    def calculate_salary(self):
        """
        Рассчитывает зарплату учителя с учетом опыта.
        """
        bonus_years = max(0, self.experience - 3)
        bonus = Teacher.base_salary * 0.05 * bonus_years
        return Teacher.base_salary + bonus


def create_students():
    """
    Создает 3 объекта Student и возвращает их в виде списка.
    """
    student1 = Student("Иван Иванов", 15, False, {"Математика": 4, "Физика": 5, "История": 3})
    student2 = Student("Анна Смирнова", 16, False, {"Математика": 5, "Физика": 4, "История": 4})
    student3 = Student("Петр Петров", 14, False, {"Математика": 3, "Физика": 4, "История": 3})
    return [student1, student2, student3]


# Пример использования:

# Создаем учителя
teacher = Teacher("Мария Петровна", 45, True, 10)
teacher.introduce_myself()
print(f"Зарплата: {teacher.calculate_salary()} руб.\n")

# Создаем студентов
students = create_students()
for student in students:
    student.introduce_myself()
    print(f"Средняя оценка: {student.calculate_average_mark():.2f}\n")
