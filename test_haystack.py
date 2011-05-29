#!/usr/bin/env python
# -*- coding: utf-8 -*-


import unittest2 as unittest

import haystack



class HaystackTestSuite(unittest.TestCase):
    """Haystack Test Suite."""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_maths_returns_int(self):
        assert isinstance(haystack.maths(), float)



if __name__ == '__main__':
    unittest.main()