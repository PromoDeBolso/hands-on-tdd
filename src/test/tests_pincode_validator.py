import unittest
from helpers.validator import Validator

class TestPinCodeValidator(unittest.TestCase):

    def setUp(self):
        pass

    def test_return_true_when_pincode_is_valid(self):
        valid_pincode = 'a12s45d789'
        is_valid = Validator.pincode_validator(valid_pincode)
        self.assertTrue(is_valid)

    def test_return_false_when_pincode_is_invalid(self):
        invalid_pincode = '123'
        is_valid = Validator.pincode_validator(invalid_pincode)
        self.assertFalse(is_valid)


if __name__ == '__main__':
    unittest.main()
