"""
Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка. В его
конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число). В классе должны быть
реализованы методы перегрузки арифметических операторов: сложение (add()), вычитание (sub()), умножение (mul()),
деление (truediv()). Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и
целочисленное (с округлением до целого) деление клеток, соответственно.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше
нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих
двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный метод
позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку:
*****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку:
*****\n*****\n*****.
Подсказка: подробный список операторов для перегрузки доступен по ссылке.
"""


class Cell:
    def __init__(self, num_part):
        self.__cell = num_part
        self.__order = 1000
    
    def __add__(self, other):
        return Cell(self.__cell + other.__cell)
    
    def __sub__(self, other):
        if self.__cell > other.__cell:
            return Cell(self.__cell - other.__cell)
        else:
            print('Вычитание невозможно')
            return None
    
    def __mul__(self, other):
        return Cell(self.__cell * other.__cell)
    
    def __truediv__(self, other):
        return Cell(max([self.__cell, other.__cell]) // min([self.__cell, other.__cell]))
        
    def __str__(self):
        output = ''
        num_part = self.__cell
        while num_part > self.__order:
            output += 'о' * self.__order + '\n'
            num_part -= self.__order
        output += 'о' * num_part + '\n'
        return output

    def make_order(self, num_part):
        self.__order = num_part


first_cell = Cell(3)
second_cell = Cell(20)
print(f'Первая клетка: {first_cell}')
print(f'Вторая клетка: {second_cell}')
third_cell = (first_cell / second_cell)
third_cell.make_order(50)
print(f'Результат деления: {third_cell}')