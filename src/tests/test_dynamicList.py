import unittest
from unittest import TestCase
# import pytest

from helper_func import DynamicList

import multiprocessing
logger = multiprocessing.log_to_stderr()
logger.setLevel(multiprocessing.SUBDEBUG)

class TestDynamicList(TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dyn = DynamicList(DynamicList("stub"))

    def add_data(self):
        dyn = self.dyn
        dyn[2][1] = "actual_data"
        self.assertEqual(dyn[2][1], "actual_data")
        # if dyn[2][1] != "actual_data":
        #     self.fail()

    def default_value(self):
        dyn = self.dyn
        self.assertEqual(dyn[2][1], "stub")
        # if dyn[1][1] != "actual_data":
        #     self.fail()

    def test_shrink_2dtable(self):
        dyn = self.dyn
        dyn[1][1] = "stub"
        dyn[2][2] = "actual_data"
        dyn[3][3] = "actual_data"
        dyn[4][4] = "stub"

        self.assertEqual(len(dyn), 5)
        self.assertEqual(dyn.cols, 5)

        dyn.shrink_2dtable()

        self.assertEqual(len(dyn), 2)
        self.assertEqual(dyn.cols, 2)
        # self.assertEqual(dyn[0][0], "actual_data")
        # if len(dyn) != 1:
        #     self.fail()
        # if 'actual_data' != dyn[0]:
        #     self.fail()

if __name__ == '__main__':
    unittest.main()
    # runner = unittest.TextTestRunner()
    # runner.run(TestDynamicList())
    import doctest
    doctest.testmod()

