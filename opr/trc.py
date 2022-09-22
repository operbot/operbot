# This file is placed in the Public Domain.


import os
import traceback


from op import name


def from_exception(exc):
    result = []
    for frm in traceback.extract_tb(exc.__traceback__)[::-1]:
        result.append("%s:%s" % (os.sep.join(frm.filename.split(os.sep)[-2:]), frm.lineno))
    return "%s(%s) %s" % (name(exc), exc, " ".join(result))
