import cuboid
import unittest

class cuboidTest(unittest.TestCase):
    def test_surface_area(self):
        assert(cuboid.surface_area(0, 0, 0) == 0)
        assert(cuboid.surface_area(3, 4, 5) == 94)
    def test_volume(self):
        assert(cuboid.volume(0, 0, 0) == 0)
        assert(cuboid.volume(3, 4, 5) == 60)
    def test_lateral_surface_area(self):
        assert(cuboid.volume(0, 0, 0) == 0)
        assert(cuboid.lateral_surface_area(3, 4, 5) == 70)


if __name__ == '__main__':
    unittest.main()