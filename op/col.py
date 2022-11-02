# This file is placed in the Public Domain.


"collection"


from op.obj import Object, keys
from op.utl import fntime


class Collection(Object):

    def add(self, key, value):
        setattr(self, key, value)

    def last(self):
        res = sorted(keys(self), key=lambda x: fntime(x))
        if res:
            return getattr(self, res[-1])

    def remove(self, obj):
        todo = []
        for key, obj in items(self):
            if ooo == obj:
                todo.append(key)
        for tdo in todo:
            delattr(self, key)
        