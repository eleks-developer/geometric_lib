import unittest
import random
import string

from source import circle


class CircleTestsCase(unittest.TestCase):
    def test_zero_area(self):
        self.assertRaises(ValueError, circle.area, 0)

    def test_negative_area(self):
        test_cases = tuple(random.randint(-1_000_000, -1) for _ in range(1_000))
        for case in test_cases:
            with self.subTest(case=case):
                with self.assertRaises(ValueError):
                    circle.area(case)

    def test_string_area(self):
        test_cases = tuple([''] + ["".join(random.choices(string.ascii_letters, k=random.randint(0, 5_000)))
                           for _ in range(1_000)])
        for case in test_cases:
            with self.subTest(case=case):
                with self.assertRaises(ValueError):
                    circle.area(case)

    def test_string_number_area(self):
        test_cases = tuple(str(random.randint(-100_000_000, 1_000_000)) for _ in range(1_000))
        for case in test_cases:
            with self.subTest(case=case):
                with self.assertRaises(ValueError):
                    circle.area(case)

    def test_regular_area(self):
        test_cases = ( (52, 8494.8665353068), (1, 3.141592653589793), (1_000_000, 3141592653589.793),
                       (2_000_000, 12566370614359.172), (52_132, 8538049058.365678),
                       (94352, 27967399978.459522), (1225, 4714352.475793184),
                       (79527923784234, 1.9869601718179383e+28),
                       (12875623987659784365238437189, 5.208185490534165e+56),
                       (12847861278367167358365789263478562785823418, 5.185749692136711e+86) )
        for test, answer in test_cases:
            with self.subTest(test=test):
                response = circle.area(test)
                self.assertEqual(response, answer)

    def test_zero_perimeter(self):
        self.assertRaises(ValueError, circle.perimeter, 0)

    def test_negative_perimeter(self):
        test_cases = tuple(random.randint(-1_000_000, -1) for _ in range(1_000))
        for case in test_cases:
            with self.subTest(case=case):
                with self.assertRaises(ValueError):
                    circle.perimeter(case)

    def test_string_perimeter(self):
        test_cases = tuple([''] + ["".join(random.choices(string.ascii_letters, k=random.randint(0, 5_000)))
                           for _ in range(1_000)])
        for case in test_cases:
            with self.subTest(case=case):
                with self.assertRaises(ValueError):
                    circle.perimeter(case)

    def test_string_number_perimeter(self):
        test_cases = tuple(str(random.randint(-100_000_000, 1_000_000)) for _ in range(1_000))
        for case in test_cases:
            with self.subTest(case=case):
                with self.assertRaises(ValueError):
                    circle.perimeter(case)

    def test_regular_perimeter(self):
        test_cases = ( (52, 326.7256359733385), (1, 6.283185307179586), (1_000_000, 6283185.307179586),
                       (2_000_000, 12566370.614359172), (52_132, 327555.0164338862),
                       (94352, 592831.1001030083), (1225, 7696.902001294993),
                       (79527923784234, 499688682231597.0),
                       (12875623987659784365238437189, 8.089993146003299e+28),
                       (12847861278367167358365789263478562785823418, 8.072549321291812e+43) )
        for test, answer in test_cases:
            with self.subTest(test=test):
                response = circle.perimeter(test)
                self.assertEqual(response, answer)
