"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде
прямоугольной схемы.

Примеры матриц: см. в методичке.

Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов
класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки
первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, list_of_lists):
        self.__matrix = list_of_lists
    
    def __str__(self):
        matrix = '______________\n'
        for row in self.__matrix:
            string = ''
            for value in row:
                string += f'{value}\t'
            string += '\n'
            matrix += string
        matrix += '______________'
        return matrix
    
    def __add__(self, other):
        if not isinstance(other, Matrix):
            return None
        new_matrix = other.__matrix if len(other.__matrix) >= len(self.__matrix) else self.__matrix
        for i in range(min([len(other.__matrix), len(self.__matrix)])):
            self_row = self.__matrix[i]
            other_row = other.__matrix[i]
            longer = other_row if len(other_row) >= len(self_row) else self_row
            for j in range(min([len(self_row), len(other_row)])):
                longer[j] = self_row[j] + other_row[j]
            new_matrix[i] = longer
        return Matrix(new_matrix)

my_matrix1 = Matrix([[1, 2, 3], [4, 5, 6, 5], [7, 8, 9]])
print(f'Первая матрица:\n{my_matrix1}')
my_matrix2 = Matrix([[7, 9, 4, 3], [6, 5, 3], [4, 2, 1], [1, 2]])
print(f'Вторая матрица:\n{my_matrix2}')
my_matrix1 += my_matrix2
print(f'Сумма:\n{my_matrix1}')
