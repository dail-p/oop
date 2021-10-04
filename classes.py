from random import random


class EvaluatedObject:
    """Отченночный объект"""
    __id = 0

    def __init__(self, **kwargs):
        super().__init__()
        self.cost = EvaluatedObject.__id * kwargs['cost']
        EvaluatedObject.__id += 1
        self._id = EvaluatedObject.__id

    def get_cost(self):
        return self.cost


class Person:
    """ Человек"""
    def __init__(self, name='', surname='', **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.surname = surname


class Student(Person, EvaluatedObject):

    def __init__(self, name='', surname='', **kwargs):
        super().__init__(name, surname, **kwargs)
        super()
        self.grades = []

    def get_cost(self):
        return self.cost * (random() * 0.5 + 0.5)


class Mentor(Person):

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


class Lecturer(Mentor, EvaluatedObject):

    def __init__(self, name='', surname='', **kwargs):
        super().__init__(name, surname, **kwargs)
        self.grades = []

    def get_cost(self):
        return self.cost * (random() * 0.5 + 1)


class Appraiser(Mentor):
    def set_grage(self, person):
        if isinstance(person, Student) or isinstance(person, Lecturer):
            person.grades.append(random() * person.cost)
        else:
            return 'Ошибка'
