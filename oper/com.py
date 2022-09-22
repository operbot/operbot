# This file is placed in the Public Domain.


from op import Object


def __dir__():
    return (
            "Commands",
            "dispatch"
           )


class Commands(Object):

    cmds = {}

    @staticmethod
    def add(cmd):
        Commands.cmds[cmd.__name__] = cmd

    @staticmethod
    def get(cmd):
        return Commands.cmds.get(cmd)

    @staticmethod
    def remove(cmd):
        del Commands.cmds[cmd]


def dispatch(evt):
    evt.parse()
    func = Commands.get(evt.cmd)
    if func:
        func(evt)
        evt.show()
    evt.ready()
