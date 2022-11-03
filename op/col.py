# This file is placed in the Public Domain.


"collection"


from op.obj import Object, items, keys


class Collection(Object):

    def add(self, key, value):
        setattr(self, key, value)

    def last(self):
        res = sorted(keys(self))
        if res:
            return getattr(self, res[-1])

    def remove(self, obj):
        todo = []
        for key, ooo in items(self):
            if ooo == obj:
                todo.append(key)
        for tdo in todo:
            delattr(self, tdo)
        