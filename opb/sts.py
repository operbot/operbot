# This file is placed in the Public Domain.
# pylint: disable=W0622,C0116


"show errors on all registered bots."


import time


from op import elapsed, format
from opr import Bus


def __dir__():
    return (
            "sts",
           )


def sts(event):
    for bot in Bus.objs:
        try:
            event.reply("%s: %s (%s)" % (
                                         bot.cfg.server,
                                         format(bot.state, skip="last"),
                                         elapsed(time.time()-bot.state.last))
                                        )
        except AttributeError:
            continue
