# This file is placed in the Public Domain.
# pylint: disable=C0115,C0116


"database"


import unittest


from operbot import Db


class TestDbs(unittest.TestCase):

    def test_constructor(self):
        dbs = Db()
        self.assertEqual(type(dbs), Db)