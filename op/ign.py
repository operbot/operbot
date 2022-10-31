# This file is placed in the Public Domain.


"ignore"


from op import Object


class Ignore(Object):

    skip = []

    @staticmethod
    def add(txt):
        Ignore.skip.append(txt)

    @staticmethod
    def remove(txt):
        Ignore.skip.remove(txt)
