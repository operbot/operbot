# This file is placed in the Public Domain.
# pylint: disable=C0112,C0103,C0114,C0115,C0116,R0903


"default"


from .obj import Object


def __dir__():
    return (
            "Default",
           )


class Default(Object):

    __slots__ = ("__default__",)

    def __init__(self, *args, **kwargs):
        Object.__init__(self, *args, **kwargs)
        self.__default__ = ""

    def __getattr__(self, key):
        val = self.__dict__.get(key, None)
        if val:
            return val
        return self.__default__
