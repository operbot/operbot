# This file is placed in the Public Domain.


import unittest


from operbot.run import Timer


def test():
    pass


class TestTimer(unittest.TestCase):

    def testcontructor(self):
        timer = Timer(60, test)
        self.assertEqual(type(timer), Timer)
