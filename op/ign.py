# This file is placed in the Public Domain.


"ignore"


from op.obj import Object


class Ignore(Object):

    skip = []

    @staticmethod
    def add(txt):
        Ignore.skip.append(txt)

    @staticmethod
    def check(txt):
        for skipped in Ignore.skip:
            if skipped in txt:
                return True
        return False

    @staticmethod
    def remove(txt):
        Ignore.skip.remove(txt)
