# This file does not work!  Haven't had time to implement the unittest.mock.

# https://stackoverflow.com/questions/4219717/how-to-assert-output-with-nosetest-unittest-in-python

import contextlib
from io import StringIO
import geometry_calculator_an
import unittest

class geometry_calc_test(unittest.TestCase):
    def test_foo(self):
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            geometry_calculator_an.main()
        output = temp_stdout.getvalue().strip()
        assert output == 'hello world!'


if __name__ == '__main__':
    unittest.main()
