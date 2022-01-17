import unittest

from save_the_universe import input_parser as ip


class TestSaveTheUniverse(unittest.TestCase):
    def test_get_cases(self):
        self.assertEqual(
            ip.get_cases(1),
            [
                [
                    ['Yeehaw', 'googol', 'NSM'],
                    ['googol', 'NSM', 'googol', 'Yeehaw', 'NSM', 'NSM'],
                ],
            ],
        )

    def test_get_engines(self):
        self.assertEqual(ip.get_engines(3), ['Yeehaw', 'googol', 'NSM'])

    def test_get_queries(self):
        self.assertEqual(
            ip.get_queries(6),
            ['googol', 'NSM', 'googol', 'Yeehaw', 'NSM', 'NSM'],
        )


if __name__ == "__main__":
    unittest.main()
