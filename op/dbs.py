# This file is placed in the Public Domain.
# pylint: disable=R,C,W


"database"


import _thread


from .obj import Object, items, kind, update
from .cls import Class
from .col import Collection
from .jsn import hook
from .wdr import Wd
from .utl import fns, fntime, locked


dblock = _thread.allocate_lock()


def __dir__():
    return (
            "Db",
            'allobj',
            "find",
            "last",
            "search"
           )


class Db():

    @staticmethod
    def all(otp, selector=None, timed=None):
        res = []
        for fnm in fns(Wd.getpath(otp), timed):
            obj = hook(fnm)
            if selector and not search(obj, selector):
                continue
            res.append((fnm, obj))
        return res

    @staticmethod
    def find(otp, selector=None, index=None, timed=None):
        if selector is None:
            selector = {}
        nmr = -1
        res = []
        for fnm in fns(Wd.getpath(otp), timed):
            obj = hook(fnm)
            if selector and not search(obj, selector):
                continue
            nmr += 1
            if index is not None and nmr != index:
                continue
            res.append((fnm, obj))
        return res

    @staticmethod
    def last(otp, selector=None, index=None, timed=None):
        res = sorted(
                     Db.find(otp, selector, index, timed), key=lambda x: fntime(x[0]))
        if res:
            return res[-1]
        return (None, None)

def allobj(name, selector=None, timed=None):
    names = Class.full(name)
    if not names:
        names = Wd.types(name)
    result = []
    for nme in names:
        for fnm, obj in Db.all(nme, selector, timed):
            result.append((fnm, obj))
    return result


def find(name, selector=None, index=None, timed=None):
    names = Class.full(name)
    if not names:
        names = Wd.types(name)
    result = []
    for nme in names:
        for item in Db.find(nme, selector, index, timed):
            result.append((item[0], item[1]))
    return result


def last(obj):
    path, ooo = Db.last(kind(obj))
    if ooo:
        update(obj, ooo)


def match(name, selector=None):
    names = Class.full(name)
    if not names:
        names = Wd.types(name)
    for nme in names:
        for item in Db.last(nme, selector):
            return item
    return None


def search(obj, selector):
    res = False
    select = Object(selector)
    for key, value in items(select):
        val = getattr(obj, key)
        if str(value) in str(val):
            res = True
            break
    return res
