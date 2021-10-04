import triangle
import unittest

class triangleTest(unittest.TestCase):
    def test_area(self):
        assert(triangle.area(0, 0, 0, 0) == 0)
        assert(round(triangle.area(3, 4, 5, 6), 2) == 6.0)
    def test_perimeter(self):
        assert(triangle.perimiter(0, 0, 0) == 0)
        assert(round(triangle.perimiter(3, 4, 5), 2) == 12)
    def test_semiperimeter(self):
        assert(triangle.semiperimeter(0, 0, 0) == 0)
        assert(round(triangle.semiperimeter(3, 4, 5), 2) == 6.0)


if __name__ == '__main__':
    unittest.main()