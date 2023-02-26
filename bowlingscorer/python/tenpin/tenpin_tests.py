import tenpin
import unittest


class TenpinScoreTests(unittest.TestCase):
    def test_20_gutter_balls_returns_zero(self):
        self.assertEqual(0, tenpin.score("00 00 00 00 00 00 00 00 00 00"))


if __name__ == '__main__':
    unittest.main()
