# -*- coding: utf-8 -*-


class Human:

    def __init__(self, age, name, gender):
        self.__age = age
        self.__name = name
        self.__gender = gender
        self.test = 'aiu'
        self._test2 = 'kakiku'

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age
        return

    @property
    def name(self):
        return self.__name

    # @name.setter
    # def name(self, name):
    #     self.__name = name
    #     return

    # @property
    # def gender(self):
    #     return self.__gender

    # @gender.setter
    # def gender(self, gender):
    #     self.__gender = gender
    #     return

    def __lt__(self, other):
        return self.__age > other.age

    def __str__(self):
        return f"<Human | {self.__age}, {self.__name}, {self.__gender} >"

    def __repr__(self):
        return f"<Human || {self.__age}, {self.__name}, {self.__gender} >"


if __name__ == '__main__':
    users = [
        Human(10, 'yuta', 'man'),
        Human(20, 'hanako', 'woman'),
        Human(15, 'ichiro', 'man')
    ]
    print(users)
    print(sorted(users))
    print(users[0].age)
    print(users[0].test)
    print(users[0]._test2)
    print(users[0]._Human__gender)
    print(users[0].age)
    users[0].age = 1
    print(users[0].age)
    # error
    users[0].name = 'test'
