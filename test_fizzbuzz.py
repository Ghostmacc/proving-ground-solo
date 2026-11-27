"""Subprocess tests for fizzbuzz.py using the standard library unittest module."""
import subprocess
import sys
import unittest


def run_fizzbuzz(*args):
    return subprocess.run(
        [sys.executable, "fizzbuzz.py", *args],
        capture_output=True,
        text=True,
        timeout=30,
    )


class FizzBuzzRoman(unittest.TestCase):
    def test_roman_15(self):
        out = run_fizzbuzz("--roman", "15")
        self.assertEqual(out.returncode, 0, out.stderr)
        want = [
            "I", "II", "Fizz", "IV", "Buzz", "Fizz", "VII", "VIII", "Fizz",
            "Buzz", "XI", "Fizz", "XIII", "XIV", "FizzBuzz",
        ]
        self.assertEqual(out.stdout.splitlines(), want)

    def test_roman_default_100(self):
        out = run_fizzbuzz("--roman")
        self.assertEqual(out.returncode, 0, out.stderr)
        lines = out.stdout.splitlines()
        self.assertEqual(len(lines), 100)
        self.assertEqual(lines[97], "XCVIII")
        self.assertEqual(lines[98], "Fizz")

    def test_upper_roman_5(self):
        out = run_fizzbuzz("--upper", "--roman", "5")
        self.assertEqual(out.returncode, 0, out.stderr)
        self.assertEqual(out.stdout.splitlines(), ["I", "II", "FIZZ", "IV", "BUZZ"])

    def test_upto_roman_4(self):
        out = run_fizzbuzz("--upto", "4", "--roman")
        self.assertEqual(out.returncode, 0, out.stderr)
        self.assertEqual(out.stdout.splitlines(), ["I", "II", "Fizz", "IV"])

    def test_plain_output_unchanged(self):
        out = run_fizzbuzz("5")
        self.assertEqual(out.returncode, 0, out.stderr)
        self.assertEqual(out.stdout.splitlines(), ["1", "2", "Fizz", "4", "Buzz"])

    def test_roman_above_3999_exits_2_without_output(self):
        out = run_fizzbuzz("--roman", "4000")
        self.assertEqual(out.returncode, 2)
        self.assertEqual(out.stdout, "")
        self.assertTrue(out.stderr.strip())


if __name__ == "__main__":
    unittest.main()
