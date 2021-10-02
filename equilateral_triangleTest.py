import equilateral_triangle
import unittest

class equilateral_triangleTest(unittest.TestCase):
    def test_area(self):
        assert(equilateral_triangle.area(0) == 0)
        assert(round(equilateral_triangle.area(7), 2) == 21.22)
    def test_perimeter(self):
        assert(equilateral_triangle.perimeter(0) == 0)
        assert(round(equilateral_triangle.perimeter(7), 2) == 21)
    def test_semiperimeter(self):
        assert(equilateral_triangle.semiperimeter(0) == 0)
        assert(round(equilateral_triangle.semiperimeter(7), 2) == 10.5)

    def test_altitude(self):
        assert(equilateral_triangle.altitude(0) == 0)
        assert(round(equilateral_triangle.altitude(7), 2) == 6.06)


if __name__ == '__main__':
    unittest.main()