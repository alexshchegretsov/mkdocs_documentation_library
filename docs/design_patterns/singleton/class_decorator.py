# -*- coding: utf-8 -*-

def singleton(cls):
    def get_instance(*args, **kwargs):
        if not hasattr(cls, "_inst"):
            cls._inst = cls(*args, **kwargs)
        return cls._inst

    return get_instance


@singleton
class Foo:
    pass


if __name__ == '__main__':
    f = Foo()
    f2 = Foo()
    print(f._inst)
