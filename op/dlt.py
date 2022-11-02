# This file is placed in the Public Domain.


"deleted"


from .obj import keys
from .col import Collection


class Deleted(Collection):

    @staticmethod
    def check(txt):
        for skipped in keys(Deleted):
            if skipped in txt:
                return True
        return False
            
