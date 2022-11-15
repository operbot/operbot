# This file is placed in the Public Domain


"skip"


import os
import sys


SKIP = []


try:
    SKIP.extend([x.strip() for x in open("fin.cfg", "r").readlines()[-1].split(",")])
except:
    pass


def doskip(txt, skip=[]):
    for skp in skip:
        if skp in txt:
            return True
    return False


def popen(txt, skip=[]):
    for line in os.popen(txt).readlines():
        if doskip(line, skip):
            continue
        print(line.strip())
        sys.stdout.flush()
