# This file is placed in the Public Domain.
# pylint: disable=C0115,C0116


"timer"


import unittest


from oper import Timer


def test():
    pass


class TestTimer(unittest.TestCase):

    def testcontructor(self):
        timer = Timer(60, test)
        self.assertEqual(type(timer), Timer)
