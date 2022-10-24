# This file is placed in the Public Domain.


import unittest


from operbot.run import Thread


def test():
    pass


class TestThread(unittest.TestCase):

    def test_thread(self):
        thr = Thread(test, "test")
        self.assertEqual(type(thr), Thread)
