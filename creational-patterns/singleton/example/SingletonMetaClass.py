from __future__ import annotations
from typing import Optional

class SingletonMeta(type):
    _instance: Optional[Singleton] = None

    def __call__(self, *args, **kwargs) -> Singleton:
        if self._instance is None:
            self._instance = super().__call__(*args, **kwargs)
        return self._instance


    # def __init__(cls, name, bases, dict):
    #     super(SingletonMetaClass, cls)\
    #         .__init__(name, bases, dict)
    #     original_new = cls.__new__

    #     def my_new(cls, *args, **kwds):
    #         if cls.instance is None:
    #             cls.instance = original_new(cls, *args, **kwds)
    #         return cls.instance

    #     cls.instance = None
    #     cls.__new__ = staticmethod(my_new)


class Singleton(metaclass=SingletonMeta):

    def __init__(self, val):
        self.val = val

    def __str__(self):
        return 'self ' + self.val

x = Singleton('sausage')
y = Singleton('eggs')
z = Singleton('spam')
print(x)
print(y)
print(z)
print(x is y is z)