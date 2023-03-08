from src.flatfair import calculate_membership_fee
import unittest


class TestFlatfair(unittest.TestCase):
    def test_weekly_rent_min_amount(self):
        self.assertEqual(calculate_membership_fee(25, 'week'), 144)

    def test_weekly_rent_max_amount(self):
        self.assertEqual(calculate_membership_fee(2000, 'week'), 144)

    def test_monthly_rent_min_amount(self):
        self.assertEqual(calculate_membership_fee(110, 'month'), 144)

    def test_monthly_rent_max_amount(self):
        self.assertEqual(calculate_membership_fee(8660, 'month'), 866)

    def test_rent_period_typo(self):
        with self.assertRaises(ValueError):
            calculate_membership_fee(25, 'monthly')

    def test_weekly_rent_lower_min_amount(self):
        with self.assertRaises(ValueError):
            calculate_membership_fee(10, 'week')

    def test_weekly_rent_higher_max_amount(self):
        with self.assertRaises(ValueError):
            calculate_membership_fee(3000, 'week')

    def test_monthly_rent_lower_min_amount(self):
        with self.assertRaises(ValueError):
            calculate_membership_fee(10, 'month')

    def test_monthly_rent_higher_max_amount(self):
        with self.assertRaises(ValueError):
            calculate_membership_fee(9000, 'month')


if __name__ == '__main__':
    unittest.main()
