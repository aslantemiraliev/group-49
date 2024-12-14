class Computer:
    def __init__(self, cpu: int, memory: int):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computations(self):
        return self.__cpu + self.__memory

    def __str__(self):
        return f"Computer(cpu={self.__cpu}, memory={self.__memory})"

    def __eq__(self, other):
        return self.memory == other.memory

    def __ne__(self, other):
        return self.memory != other.memory

    def __lt__(self, other):
        return self.memory < other.memory

    def __le__(self, other):
        return self.memory <= other.memory

    def __gt__(self, other):
        return self.memory > other.memory

    def __ge__(self, other):
        return self.memory >= other.memory


class Phone:
    def __init__(self, sim_cards_list: list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def call(self, sim_card_number: int, call_to_number: str):
        if 1 <= sim_card_number <= len(self.__sim_cards_list):
            sim_card = self.__sim_cards_list[sim_card_number - 1]
            print(f"Идет звонок на номер {call_to_number} с сим-карты-{sim_card_number} - {sim_card}.")
        else:
            print("Неверный номер сим-карты.")

    def __str__(self):
        return f"Phone(sim_cards_list={self.__sim_cards_list})"


class SmartPhone(Computer, Phone):
    def __init__(self, cpu: int, memory: int, sim_cards_list: list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    def use_gps(self, location: str):
        print(f"Построение маршрута до {location}...")

    def __str__(self):
        return f"SmartPhone(cpu={self.cpu}, memory={self.memory}, sim_cards_list={self.sim_cards_list})"


# Создание объектов
computer = Computer(4, 16)
phone = Phone(["Beeline", "Megacom", "O!"])
smartphone1 = SmartPhone(8, 32, ["Beeline", "Megacom"])
smartphone2 = SmartPhone(6, 64, ["O!"])

# Распечатка информации об объектах
print(computer)
print(phone)
print(smartphone1)
print(smartphone2)

# Опробование методов
print("\nОпробование методов:")
print("Сумма CPU и памяти компьютера:", computer.make_computations())
phone.call(1, "+996 777 99 88 11")
smartphone1.use_gps("Бишкек")
print("Сравнение памяти смартфонов:", smartphone1 < smartphone2)
