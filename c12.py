# -*- coding: utf-8 -*-


class Human:

    def __init__(self, age, name, gender):
        self.age = age
        self.name = name
        self.gender = gender

    def __lt__(self, other):
        return self.age > other.age

    def __str__(self):
        return f"<Human | {self.age}, {self.name}, {self.gender} >"

    def __repr__(self):
        return f"<Human || {self.age}, {self.name}, {self.gender} >"


if __name__ == '__main__':
    users = [
        Human(10, 'yuta', 'man'),
        Human(20, 'hanako', 'woman'),
        Human(15, 'ichiro', 'man')
    ]
    print(users)
    print(sorted(users))
