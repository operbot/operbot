# This file is placed in the Public Domain.


import time


from oper.cfg import Config
from oper.evt import Event


starttime = time.time()


Cfg = Config()


def docmd(clt, txt):
    cmd = Event()
    cmd.channel = ""
    cmd.orig = repr(clt)
    cmd.txt = txt
    clt.handle(cmd)
    cmd.wait()
    return cmd
