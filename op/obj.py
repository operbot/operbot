# This file is placed in the Public Domain.
# pylint: disable=R,C,W


"Object"


import datetime
import os
import uuid


from .cls import Class


def __dir__():
    return (
            'Object',
            'edit',
            'items',
            'keys',
            'kind',
            'register',
            'update',
            'values'
           )


class Object:

    __slots__ = ("__dict__", "__fnm__")

    def __init__(self, *args, **kwargs):
        object.__init__(self)
        self.__fnm__ = os.path.join(
            kind(self),
            str(uuid.uuid4()),
            os.sep.join(str(datetime.datetime.now()).split()),
        )
        if args:
            val = args[0]
            if isinstance(val, dict):
                update(self, val)
            elif isinstance(val, Object):
                update(self, vars(val))
        if kwargs:
            self.__dict__.update(kwargs)

    def __delitem__(self, key):
        self.__dict__.__delitem__(key)

    def __getitem__(self, key):
        self.__dict__.__getitem__(key)
          
    def __iter__(self):
        return iter(self.__dict__)

    def __len__(self):
        return len(self.__dict__)

    def __str__(self):
        return str(self. __dict__)

    def __setitem__(self, key, value):
        self.__dict__.__setitem__(key, value)


Class.add(Object)


def edit(obj, setter):
    for key, value in items(setter):
        register(obj, key, value)


def items(obj):
    if isinstance(obj, type({})):
        return obj.items()
    return obj.__dict__.items()


def keys(obj):
    return obj.__dict__.keys()


def kind(obj):
    kin = str(type(obj)).split()[-1][1:-2]
    if kin == "type":
        kin = obj.__name__
    return kin


def register(obj, key, value):
    setattr(obj, key, value)


def update(obj, data):
    for key, value in items(data):
        setattr(obj, key, value)


def values(obj):
    return obj.__dict__.values()
