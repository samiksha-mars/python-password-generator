import string
import unittest

from password_generator import generate_password


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


if __name__ == "__main__":
    unittest.main()
