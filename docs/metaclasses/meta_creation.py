# -*- coding: utf-8 -*-


class TestMeta(type):
    counter = 0

    # metacls - metaclass TestMeta
    @classmethod
    def __prepare__(metacls, name, bases, **kwargs):
        print(f"{metacls.__name__}.__prepare__, metacls={metacls}, name={name}, bases={bases}, **kwargs={kwargs}")
        metacls.counter += 1
        return {"x": 42}

    # metacls - metaclass TestMeta
    def __new__(metacls, name, bases, attrs):
        print(f"{metacls.__name__}.__new__, metacls={metacls}, name={name}, bases={bases}, attrs={attrs}")
        metacls.counter += 1
        return type.__new__(metacls, name, bases, attrs)

    # cls - new class that __new__ returns
    def __init__(cls, name, bases, attrs):
        print(f"TestMeta.__init__, cls={cls}, name={name}, bases={bases}, attrs={attrs}")
        super().__init__(name, bases, attrs)

    def __call__(cls, *args, **kwargs):
        print(f"TestMeta.__call__, cls={cls}, *args={args}, **kwargs={kwargs}")
        super().__call__(*args, **kwargs)


class Class(metaclass=TestMeta):

    def __new__(cls, *args, **kwargs):
        print("Class.__new__")
        return object.__new__(cls)

    def __init__(self, v):
        print("Class.__init__")
        self.v = v


if __name__ == '__main__':
    Class(42)