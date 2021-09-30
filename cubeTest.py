import cube
import unittest

class cubeTest(unittest.TestCase):
    def test_surface_area(self):
        assert(cube.surface_area(0) == 0)
        assert(cube.surface_area(3) == 54)

    def test_volume(self):
        assert(cube.volume(0) == 0)
        assert(cube.volume(3) == 27)

    def test_lateral_surface_area(self):
        assert(cube.lateral_surface_area(0) == 0)
        assert(cube.lateral_surface_area(3) == 36)
        

if __name__ == '__main__':
    unittest.main()