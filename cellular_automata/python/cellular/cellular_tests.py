import unittest
from cellular import cellular


class CellularTests(unittest.TestCase):

    def test_rule_0_makes_everything_empty(self):
        for a in [cellular.EMPTY, cellular.FILLED]:
            for b in [cellular.EMPTY, cellular.FILLED]:
                for c in [cellular.EMPTY, cellular.FILLED]:
                    with self.subTest(msg=f"{a}{b}{c}"):
                        self.assertEqual("".join([cellular.EMPTY, cellular.EMPTY, cellular.EMPTY]),
                                         cellular.next_state("".join([a, b, c]), 0))


if __name__ == '__main__':
    unittest.main()
