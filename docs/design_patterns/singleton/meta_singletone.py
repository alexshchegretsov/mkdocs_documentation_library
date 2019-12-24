# -*- coding: utf-8 -*-

class MetaSingletone(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if not cls.__name__ in  cls._instances:
            cls._instances[cls.__name__] = super().__call__(*args, **kwargs)
        return cls._instances[cls.__name__]


class OnlyOne(metaclass=MetaSingletone):
    pass


if __name__ == '__main__':
    s = OnlyOne()
    s2 = OnlyOne()
    print(s is s2)