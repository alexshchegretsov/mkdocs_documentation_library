# -*- coding: utf-8 -*-

# SecondMeta -> FirstMeta -> type

class FirstMeta(type):

    def __new__(metacls, *args, **kwargs):
        print("3. FirstMeta.__new__ in action")
        # FirstMeta -> type
        return type.__new__(metacls, *args, **kwargs)

    def __call__(cls, *args, **kwargs):
        print(f"6. FirstMeta.__call__, args={args}, kwargs={kwargs}")
        # FirstMeta -> type
        super().__call__(*args, **kwargs)


class SecondMeta(FirstMeta):

    @classmethod
    def __prepare__(metacls, name, bases, **kwargs):
        print(f"1. {metacls.__name__}.__prepare__, metacls={metacls}, name={name}, bases={bases}, **kwargs={kwargs}")
        # return attrs which go to the __new__
        return {42: 78}

    def __new__(metacls, name, bases, attrs):
        print(f"2. {metacls.__name__}.__new__, metacls={metacls}, name={name}, bases={bases}, attrs={attrs}")
        return super().__new__(metacls, name, bases, attrs)

    def __init__(cls, name, bases, attrs):
        print("when we achieved type - type.__new__ creates new type & returns it into SecondMeta.__init__")
        print(f"4. SecondMeta.__init__", cls.mro())
        super(SecondMeta, cls).__init__(name, bases, attrs)

    def __call__(cls, *args, **kwargs):
        print(f"5. SecondMeta.__call__, args={args}, kw={kwargs}")
        return super(SecondMeta, cls).__call__(*args, **kwargs)


# SimpleClass is an instance of SecondMeta !!
# call 1st state
class SimpleClass(metaclass=SecondMeta):

    def __new__(cls, *args, **kwargs):
        print(f"7. SimpleClass.__new__, args={args}, kw={kwargs}")
        # SimpleClass -> object, because object.__new__
        return object.__new__(cls)

    def __init__(self, v):
        print("8. SimpleClass.__init__")
        self.v = v


if __name__ == '__main__':
    print("=" * 20)
    SimpleClass(78)
