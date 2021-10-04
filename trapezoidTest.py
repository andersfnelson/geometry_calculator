import trapezoid
import unittest

class trapezoidTest(unittest.TestCase):
    def test_area(self):
        assert(trapezoid.area(0, 0, 0) == 0)
        assert(round(trapezoid.area(4, 4, 7), 2) == 28.0)


    def test_median(self):
        assert(trapezoid.median(0, 0) == 0)
        assert(round(trapezoid.median(4, 4), 2) == 4.0)



if __name__ == '__main__':
    unittest.main()