import io
import string
import unittest
from contextlib import redirect_stderr, redirect_stdout

from password_generator import generate_password, main


class GeneratePasswordTest(unittest.TestCase):

    def test_default_length(self):
        self.assertEqual(len(generate_password()), 16)

    def test_custom_length(self):
        self.assertEqual(len(generate_password(length=32)), 32)

    def test_contains_all_character_sets(self):
        password = generate_password(length=64)
        self.assertTrue(any(c in string.ascii_uppercase for c in password))
        self.assertTrue(any(c in string.ascii_lowercase for c in password))
        self.assertTrue(any(c in string.digits for c in password))
        self.assertTrue(any(c in string.punctuation for c in password))

    def test_only_lowercase_when_others_disabled(self):
        password = generate_password(
            length=10,
            use_uppercase=False,
            use_digits=False,
            use_symbols=False,
        )
        self.assertTrue(password.islower())

    def test_no_character_sets_raises(self):
        with self.assertRaises(ValueError):
            generate_password(
                use_uppercase=False,
                use_lowercase=False,
                use_digits=False,
                use_symbols=False,
            )

    def test_length_too_short_raises(self):
        with self.assertRaises(ValueError):
            generate_password(length=3)

    def test_generates_different_passwords(self):
        self.assertNotEqual(generate_password(), generate_password())


class MainTest(unittest.TestCase):

    def run_main(self, *argv):
        out, err = io.StringIO(), io.StringIO()
        with redirect_stdout(out), redirect_stderr(err):
            main(list(argv))
        return out.getvalue()

    def test_prints_count_passwords(self):
        lines = self.run_main("--count", "3", "--length", "12").splitlines()
        self.assertEqual(len(lines), 3)
        self.assertTrue(all(len(line) == 12 for line in lines))

    def test_non_positive_count_is_an_error(self):
        for count in ("0", "-2"):
            with self.assertRaises(SystemExit) as ctx:
                self.run_main("--count", count)
            self.assertEqual(ctx.exception.code, 2)


if __name__ == "__main__":
    unittest.main()
