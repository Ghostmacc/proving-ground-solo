"""Unit tests for roman.to_roman using the standard library unittest module."""
import unittest

import roman


class ToRomanExamples(unittest.TestCase):
    def test_documented_examples(self):
        cases = {
            1: "I",
            4: "IV",
            9: "IX",
            14: "XIV",
            40: "XL",
            90: "XC",
            400: "CD",
            1994: "MCMXCIV",
            3999: "MMMCMXCIX",
        }
        for n, want in cases.items():
            with self.subTest(n=n):
                self.assertEqual(roman.to_roman(n), want)

    def test_lower_bound(self):
        self.assertEqual(roman.to_roman(1), "I")

    def test_upper_bound(self):
        self.assertEqual(roman.to_roman(3999), "MMMCMXCIX")


class ToRomanRangeErrors(unittest.TestCase):
    def test_zero(self):
        with self.assertRaises(ValueError):
            roman.to_roman(0)

    def test_negative(self):
        with self.assertRaises(ValueError):
            roman.to_roman(-1)

    def test_above_upper_bound(self):
        with self.assertRaises(ValueError):
            roman.to_roman(4000)


class ToRomanTypeErrors(unittest.TestCase):
    def test_non_integer_rejected_with_type_error(self):
        for bad in ("1", 1.0, 4.5, None, []):
            with self.subTest(bad=bad):
                with self.assertRaises(TypeError):
                    roman.to_roman(bad)

    def test_bool_rejected(self):
        with self.assertRaises(TypeError):
            roman.to_roman(True)
        with self.assertRaises(TypeError):
            roman.to_roman(False)


class ToRomanExhaustive(unittest.TestCase):
    def test_all_values_distinct_and_valid_letters(self):
        seen = {}
        for n in range(1, 4000):
            numeral = roman.to_roman(n)
            self.assertTrue(numeral)
            self.assertTrue(
                set(numeral) <= set("IVXLCDM"),
                f"{n}: {numeral} uses invalid letters",
            )
            self.assertNotIn(
                numeral, seen, f"{n}: {numeral} duplicates {seen.get(numeral)}"
            )
            seen[numeral] = n
        self.assertEqual(len(seen), 3999)


if __name__ == "__main__":
    unittest.main()
