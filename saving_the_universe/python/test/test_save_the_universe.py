import unittest

from save_the_universe import save_the_universe as stu

input: str = """
2
5
Yeehaw
NSM
Dont Ask
B9
Googol
10
Yeehaw
Yeehaw
Googol
B9
Googol
NSM
B9
NSM
Dont Ask
Googol
5
Yeehaw
NSM
Dont Ask
B9
Googol
7
Googol
Dont Ask
NSM
NSM
Yeehaw
Yeehaw
Googol
"""

output: str = """
Case #1: 1
Case #2: 0
"""


class TestSaveTheUniverse(unittest.TestCase):
    def test_should_switch(self):
        self.assertTrue(stu.should_switch('Googol', 'Googol'))

    def test_should_not_switch(self):
        self.assertFalse(stu.should_switch('Googol', 'notgoogle'))

    def test_count_switches_case_one(self):
        engines = [
            'Yeehaw',
            'NSM',
            'Dont Ask',
            'B9',
            'Googol',
        ]
        queries = [
            'Yeehaw',
            'Yeehaw',
            'Googol',
            'B9',
            'Googol',
            'NSM',
            'B9',
            'NSM',
            'Dont Ask',
            'Googol',
        ]
        self.assertEqual(stu.count_switches(engines, queries), 3)

    def test_count_switches_case_two(self):
        engines = [
            'Yeehaw',
            'NSM',
            'Dont Ask',
            'B9',
            'Googol',
        ]
        queries = [
            'Googol',
            'Dont Ask',
            'NSM',
            'NSM',
            'Yeehaw',
            'Yeehaw',
            'Googol',
        ]
        self.assertEqual(stu.count_switches(engines, queries), 1)

    def test_count_min_switches_case_one(self):
        engines = [
            'Yeehaw',
            'NSM',
            'Dont Ask',
            'B9',
            'Googol',
        ]
        queries = [
            'Yeehaw',
            'Yeehaw',
            'Googol',
            'B9',
            'Googol',
            'NSM',
            'B9',
            'NSM',
            'Dont Ask',
            'Googol',
        ]
        self.assertEqual(
            stu.count_min_switches(
                engines,
                queries,
                len(queries),
                len(engines),
            ),
            1,
        )

    def test_count_min_switches_case_two(self):
        engines = [
            'Yeehaw',
            'NSM',
            'Dont Ask',
            'B9',
            'Googol',
        ]
        queries = [
            'Googol',
            'Dont Ask',
            'NSM',
            'NSM',
            'Yeehaw',
            'Yeehaw',
            'Googol',
        ]
        self.assertEqual(
            stu.count_min_switches(
                engines,
                queries,
                len(queries),
                len(engines),
            ),
            0,
        )


if __name__ == "__main__":
    unittest.main()
