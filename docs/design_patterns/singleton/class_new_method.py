# -*- coding: utf-8 -*-
class Singleton:
    _instances = None

    def __new__(cls, *args, **kwargs):
        if not cls._instances:
            cls._instances = object.__new__(cls)
        return cls._instances


if __name__ == '__main__':
    s = Singleton()
    s2 = Singleton()
    print(s is s2)