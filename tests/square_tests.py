import unittest
import random
import string

from source import square


class SquareTestsCase(unittest.TestCase):
    def test_zero_area(self):
        self.assertRaises(ValueError, square.area, 0)

    def test_negative_area(self):
        test_cases = tuple(random.randint(-1_000_000, -1) for _ in range(1_000))
        for case in test_cases:
            with self.subTest(case=case):
                with self.assertRaises(ValueError):
                    square.area(case)

    def test_string_area(self):
        test_cases = tuple([''] + ["".join(random.choices(string.ascii_letters, k=random.randint(0, 5_000)))
                           for _ in range(1_000)])
        for case in test_cases:
            with self.subTest(case=case):
                with self.assertRaises(ValueError):
                    square.area(case)

    def test_string_number_area(self):
        test_cases = tuple(str(random.randint(-1_000_000, 1_000_000)) for _ in range(1_000))
        for case in test_cases:
            with self.subTest(case=case):
                with self.assertRaises(ValueError):
                    square.area(case)

    def test_regular_area(self):
        test_cases = ( (68243, 4657107049), (3169817389127, 10047742280411910937822129),
                       (15, 225), (124124, 15406767376),
                       (4127401872309469287561782365, 17035446215543712617713784937859171705207046935624993225),
                       (372526735, 138776168289760225),
                       (79082375672128, 6254022141947582539756048384),
                       (258709834650283750825206378926582,
                        66930778544777158880641967202973352720339003106121637138546202724),
                       (534856703856778923745972635723605872,
                        286071693660538110443388791118002904340679934625695295598230897992880384),
                       (857209354602346597836457896239874346659,
                        734807877617771592393797165693118979848863525589330337525063241113082104462281) )
        for test, answer in test_cases:
            with self.subTest(test=test, answer=answer):
                response = square.area(test)
                self.assertEqual(response, answer)

    def test_zero_perimeter(self):
        self.assertRaises(ValueError, square.perimeter, 0)

    def test_negative_perimeter(self):
        test_cases = tuple(random.randint(-1_000_000, -1) for _ in range(1_000))
        for case in test_cases:
            with self.subTest(case=case):
                with self.assertRaises(ValueError):
                    square.perimeter(case)

    def test_string_perimeter(self):
        test_cases = tuple([''] + ["".join(random.choices(string.ascii_letters, k=random.randint(0, 5_000)))
                           for _ in range(1_000)])
        for case in test_cases:
            with self.subTest(case=case):
                with self.assertRaises(ValueError):
                    square.perimeter(case)

    def test_string_number_perimeter(self):
        test_cases = tuple(str(random.randint(-1_000_000, 1_000_000)) for _ in range(1_000))
        for case in test_cases:
            with self.subTest(case=case):
                with self.assertRaises(ValueError):
                    square.perimeter(case)

    def test_regular_perimeter(self):
        test_cases = ( (68243, 272972), (3169817389127, 12679269556508), (15, 60), (124124, 496496),
                      (4127401872309469287561782365, 16509607489237877150247129460),
                      (372526735, 1490106940), (79082375672128, 316329502688512),
                      (258709834650283750825206378926582, 1034839338601135003300825515706328),
                      (534856703856778923745972635723605872, 2139426815427115694983890542894423488),
                      (857209354602346597836457896239874346659, 3428837418409386391345831584959497386636) )
        for test, answer in test_cases:
            with self.subTest(test=test, answer=answer):
                response = square.perimeter(test)
                self.assertEqual(response, answer)
