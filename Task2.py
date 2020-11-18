"""
Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность
(класс) этого проекта — одежда, которая может иметь определенное название. К типам одежды в
этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для
пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
(V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу
декоратора @property.
"""

from abc import ABC, abstractmethod


class Wear(ABC):
    @abstractmethod
    def fabric(self):
        pass


class Coat(Wear):
    def __init__(self, V):
        self.__V = V
    
    @property
    def fabric(self):
        return self.__V / 6.5 + 0.5


class Suit(Wear):
    def __init__(self, H):
        self.__H = H
    
    @property
    def fabric(self):
        return 2 * self.__H + 0.3


coat1 = Coat(10)
suit1 = Suit(5)
print(coat1.fabric + suit1.fabric)
