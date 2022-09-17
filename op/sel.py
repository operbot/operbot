# This file is placed in the Public Domain.
# pylint: disable=C0112,C0103,C0114,C0115,C0116,R0903


"selector"


from .dft import Default


def __dir__():
    return (
            "Selector",
           )


class Selector(Default):

    pass
