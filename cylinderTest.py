import cylinder
import unittest

class cylinderTest(unittest.TestCase):
    def test_surface_area(self):
        assert(cylinder.surface_area(0, 0) == 0)
        assert(round(cylinder.surface_area(2, 4), 2) == 75.4)
    def test_volume(self):
        assert(cylinder.volume(0, 0) == 0)
        assert(round(cylinder.volume(2, 4), 2) == 50.27)
    def test_lateral_surface_area(self):
        assert(cylinder.lateral_surface_area(0, 0) == 0)
        assert(round(cylinder.lateral_surface_area(2, 4), 2) == 50.27)

    def test_top_bottom_surface_area(self):
        assert(cylinder.top_bottom_surface_area(0) == 0)
        assert(round(cylinder.top_bottom_surface_area(2), 2) == 12.57)


if __name__ == '__main__':
    unittest.main()