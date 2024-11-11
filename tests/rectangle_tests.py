import unittest
import random
import string

from source import rectangle


class RectangleTestsCase(unittest.TestCase):
    def test_zero_area(self):
        test_cases = ( (0, random.randint(1, 1_000_000)),
                       (random.randint(1, 1_000_000), 0),
                       (0, 0) )
        for a, b in test_cases:
            with self.subTest(a=a, b=b):
                with self.assertRaises(ValueError):
                    rectangle.area(a, b)

    def test_negative_area(self):
        test_cases = tuple([(random.randint(-1_000_000, -1), random.randint(1, 1_000_000)) for _ in range(1_000)]
                           + [(random.randint(1, 1_000_000), random.randint(-1_000_000, -1)) for _ in range(1_000)]
                           + [(random.randint(-1_000_000, -1), random.randint(-1_000_000, -1)) for _ in range(1_000)])
        for a, b in test_cases:
            with self.subTest(a=a, b=b):
                with self.assertRaises(ValueError):
                    rectangle.area(a, b)

    def test_strings_area(self):
        test_cases = tuple([('', '')] + [("".join(random.choices(string.ascii_letters, k=random.randint(0, 5_000))),
                            "".join(random.choices(string.ascii_letters, k=random.randint(0, 5_000))))
                           for _ in range(1_000)])
        for a, b in test_cases:
            with self.subTest(a=a, b=b):
                with self.assertRaises(ValueError):
                    rectangle.area(a, b)

    def test_string_numbers_area(self):
        test_cases = tuple((str(random.randint(-1_000_000, 1_000_000)),
                            str(random.randint(-1_000_000, 1_000_000)))
                           for _ in range(1_000))
        for a, b in test_cases:
            with self.subTest(a=a, b=b):
                with self.assertRaises(ValueError):
                    rectangle.area(a, b)

    def test_regular_area(self):
        test_cases = ( (123, 53, 6519), (871534, 7, 6100738),
                       (84782946782937482374, 917823567157812543, 77815786650466667245353341161458617082),
                       (98149, 71897016576472163591, 7056620279964166384293059),
                       (1368716284, 237492749898352, 325060194117813727163968),
                       (813, 910230, 740016990),
                       (5673426598734265897634578629387456928374659783, 905720345620578923475982734,
                        5138537899858584843189842237701986502663292187189834137700566448832186722),
                       (90437508273579863052+1123, 724976237864987421+123123, 65565044510074738429123786598880361200),
                       (234827348967856+8937870217, 93278407023+89237498617869, 20978107976885479124694313116),
                       (57038954+3280975401892365091, 636+29175809720659861027567,
                        95725114025441317286557402363716787281135) )
        for a, b, answer in test_cases:
            with self.subTest(a=a, b=b):
                response = rectangle.area(a, b)
                self.assertEqual(response, answer)

    def test_zero_perimeter(self):
        test_cases = ( (0, random.randint(1, 1_000_000)),
                       (random.randint(1, 1_000_000), 0),
                       (0, 0) )
        for a, b in test_cases:
            with self.subTest(a=a, b=b):
                with self.assertRaises(ValueError):
                    rectangle.perimeter(a, b)

    def test_negative_perimeter(self):
        test_cases = tuple([(random.randint(-1_000_000, -1), random.randint(1, 1_000_000)) for _ in range(1_000)]
                           + [(random.randint(1, 1_000_000), random.randint(-1_000_000, -1)) for _ in range(1_000)]
                           + [(random.randint(-1_000_000, -1), random.randint(-1_000_000, -1)) for _ in range(1_000)])
        for a, b in test_cases:
            with self.subTest(a=a, b=b):
                with self.assertRaises(ValueError):
                    rectangle.perimeter(a, b)

    def test_strings_perimeter(self):
        test_cases = tuple([('', '')] + [("".join(random.choices(string.ascii_letters, k=random.randint(0, 5_000))),
                            "".join(random.choices(string.ascii_letters, k=random.randint(0, 5_000))))
                           for _ in range(1_000)])
        for a, b in test_cases:
            with self.subTest(a=a, b=b):
                with self.assertRaises(ValueError):
                    rectangle.perimeter(a, b)

    def test_string_numbers_perimeter(self):
        test_cases = tuple((str(random.randint(-1_000_000, 1_000_000)),
                            str(random.randint(-1_000_000, 1_000_000)))
                           for _ in range(1_000))
        for a, b in test_cases:
            with self.subTest(a=a, b=b):
                with self.assertRaises(ValueError):
                    rectangle.perimeter(a, b)

    def test_regular_perimeter(self):
        test_cases = ( (123, 53, 352), (871534, 7, 1743082),
                       (84782946782937482374, 917823567157812543, 171401540700190589834),
                       (98149, 71897016576472163591, 143794033152944523480),
                       (1368716284, 237492749898352, 474988237229272),
                       (813, 910230, 1822086),
                       (5673426598734265897634578629387456928374659783, 905720345620578923475982734,
                        11346853197468531797080597950016071703701285034),
                       (90437508273579863052+1123, 724976237864987421+123123, 182324969022889949438),
                       (234827348967856+8937870217, 93278407023+89237498617869, 648334127725930),
                       (57038954+3280975401892365091, 636+29175809720659861027567,
                        58358181392123620864496) )
        for a, b, answer in test_cases:
            with self.subTest(a=a, b=b):
                response = rectangle.perimeter(a, b)
                self.assertEqual(response, answer)
