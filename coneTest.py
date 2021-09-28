import cone
import unittest

class coneTest(unittest.TestCase):
    def test_volume1(self):
        assert(cone.volume(2, 2) == 0)


if __name__ == '__main__':
    unittest.main()