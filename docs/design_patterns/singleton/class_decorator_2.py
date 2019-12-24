# -*- coding: utf-8 -*-

class single:
    _instances = {}

    def __init__(self, cls):
        self.cls = cls

    def __call__(self, *args, **kwargs):
        if not self.cls.__name__ in self._instances:
            self._instances[self.cls.__name__] = self.cls(*args, **kwargs)
        return self._instances[self.cls.__name__]


@single
class OnlyOne:
    pass


if __name__ == '__main__':
    s = OnlyOne()
    s2 = OnlyOne()
    print(s is s2)