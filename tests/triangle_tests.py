import unittest
import random
import string

from source import triangle


class TriangleTestsCase(unittest.TestCase):
    def test_zero_area(self):
        test_cases = ( (0, random.randint(1, 1_000_000)),
                       (random.randint(1, 1_000_000), 0),
                       (0, 0), )
        for a, h in test_cases:
            with self.subTest(a=a, h=h):
                with self.assertRaises(ValueError):
                    triangle.area(a, h)

    def test_negative_area(self):
        test_cases = tuple([(random.randint(-1_000_000, -1), random.randint(1, 1_000_000))
                            for _ in range(1_000)]
                           + [(random.randint(1, 1_000_000), random.randint(-1_000_000, 1))
                              for _ in range(1_000)]
                           + [(random.randint(-1_000_000, -1), random.randint(-1_000_000, -1))
                              for _ in range(1_000)])
        for a, h in test_cases:
            with self.subTest(a=a, h=h):
                with self.assertRaises(ValueError):
                    triangle.area(a, h)

    def test_strings_area(self):
        test_cases = tuple([('', '')] + [("".join(random.choices(string.ascii_letters, k=random.randint(0, 5_000))),
                            "".join(random.choices(string.ascii_letters, k=random.randint(0, 5_000))))
                           for _ in range(1_000)])
        for a, h in test_cases:
            with self.subTest(a=a, h=h):
                with self.assertRaises(ValueError):
                    triangle.area(a, h)

    def test_string_numbers_area(self):
        test_cases = tuple((str(random.randint(-1_000_000, 1_000_000)),
                            str(random.randint(-1_000_000, 1_000_000)))
                           for _ in range(1_000))
        for a, h in test_cases:
            with self.subTest(a=a, h=h):
                with self.assertRaises(ValueError):
                    triangle.area(a, h)

    def test_regular_area(self):
        test_cases = ( (253, 127, 16065.5), (87350289, 2330948, 101804490721986.0), (2847, 634, 902499.0),
                       (3523847, 2342342, 4127027414837.0), (234513, 523465, 61379673772.5), (532, 255, 67830.0),
                       (87502873645, 89365726378, 3.9098789317238886e+21), (25672345, 23414, 300546142915.0),
                       (3625873, 32746, 59366418629.0),
                       (74579263578623, 6958763246579238756987234659278, 2.594897191739337e+44) )
        for a, h, answer in test_cases:
            with self.subTest(a=a, h=h):
                response = triangle.area(a, h)
                self.assertEqual(response, answer)

    def test_zero_perimeter(self):
        test_cases = ( (0, random.randint(1, 1_000_000), random.randint(1, 1_000_000)),
                       (random.randint(1, 1_000_000), 0, random.randint(1, 1_000_000)),
                       (random.randint(1, 1_000_000), random.randint(1, 1_000_000), 0),
                       (0, 0, 0) )
        for a, b, c, in test_cases:
            with self.subTest(a=a, b=b, c=c):
                with self.assertRaises(ValueError):
                    triangle.perimeter(a, b, c)

    def test_negative_perimeter(self):
        test_cases = tuple( [(random.randint(-1_000_000, -1), random.randint(1, 1_000_000), random.randint(1, 1_000_000))
                             for _ in range(1_000)]
                            + [(random.randint(1, 1_000_000), random.randint(-1_000_000, -1), random.randint(1, 1_000_000))
                               for _ in range(1_000)]
                            + [(random.randint(1, 1_000_000), random.randint(1, 1_000_000), random.randint(-1_000_000, -1))
                               for _ in range(1_000)]
                            + [(random.randint(-1_000_000, -1), random.randint(-1_000_000, -1), random.randint(-1_000_000, -1))
                               for _ in range(1_000)] )
        for a, b, c, in test_cases:
            with self.subTest(a=a, b=b, c=c):
                with self.assertRaises(ValueError):
                    triangle.perimeter(a, b, c)

    def test_strings_perimeter(self):
        test_cases = tuple([('', '', '')]
                           + [("".join(random.choices(string.ascii_letters, k=random.randint(0, 5_000))),
                               "".join(random.choices(string.ascii_letters, k=random.randint(0, 5_000))),
                               "".join(random.choices(string.ascii_letters, k=random.randint(0, 5_000))))
                              for _ in range(1_000)])
        for a, b, c, in test_cases:
            with self.subTest(a=a, b=b, c=c):
                with self.assertRaises(ValueError):
                    triangle.perimeter(a, b, c)

    def test_string_numbers_perimeter(self):
        test_cases = tuple((str(random.randint(-1_000_000, 1_000_000)),
                            str(random.randint(-1_000_000, 1_000_000)),
                            str(random.randint(-1_000_000, 1_000_000)))
                           for _ in range(1_000))
        for a, b, c, in test_cases:
            with self.subTest(a=a, b=b, c=c):
                with self.assertRaises(ValueError):
                    triangle.perimeter(a, b, c)

    def test_non_existent_triangles(self):
        test_cases = tuple( [(random.randint(1, 1_000_000), random.randint(1, 1_000_000), random.randint(2_000_000, 5_000_000))
                             for _ in range(1_000)]
                            + [(random.randint(1, 1_000_000), random.randint(2_000_000, 5_000_000), random.randint(1, 1_000_000))
                               for _ in range(1_000)]
                            + [(random.randint(2_000_000, 5_000_000), random.randint(1, 1_000_000), random.randint(1, 1_000_000))
                               for _ in range(1_000)] )
        for a, b, c, in test_cases:
            with self.subTest(a=a, b=b, c=c):
                response = triangle.perimeter(a, b, c)
                self.assertEqual(response, -1)

    def test_regular_perimeter(self):
        test_cases = ( (3, 4, 5, 12), (6, 8, 10, 24), (5, 12, 13, 30), (12, 35, 37, 84), (9, 40, 41, 90),
                       (8, 15, 17, 40), (7, 24, 25, 56), (15, 36, 39, 90), (20, 21, 29, 70), (21, 28, 35, 84) )
        for a, b, c, answer in test_cases:
            with self.subTest(a=a, b=b, c=c):
                response = triangle.perimeter(a, b, c)
                self.assertEqual(response, answer)
