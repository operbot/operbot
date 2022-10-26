# This file is placed in the Public Domain.


"collection"


from op.obj import Object


class Collection(Object):

    def __init__(self):
        Object.__init__(self)
        self.objs = []

    def add(self, obj):
        self.objs.append(obj)

    def remove(self, obj):
        self.objs.remove(obj)
