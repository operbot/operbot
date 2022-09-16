# This file is placed in the Public Domain.


import traceback


def from_exception(exc, txt="", sep=" "):
    result = []
    for frm in traceback.extract_tb(exc.__traceback__):
        result.append("%s:%s" % (os.sep.join(frm.filename.split(os.sep)[-2:]), frm.lineno))
    return "%s(%s) %s" % (name(exc), exc, " ".join(result))
