from src.flatfair import calculate_membership_fee, OrganisationUnit, OrganisationUnitConfig
import unittest


class TestFlatfair(unittest.TestCase):
    def test_weekly_rent_min_amount(self):
        self.assertEqual(calculate_membership_fee(25, 'week', None), 144)

    def test_weekly_rent_max_amount(self):
        self.assertEqual(calculate_membership_fee(2000, 'week', None), 144)

    def test_monthly_rent_min_amount(self):
        self.assertEqual(calculate_membership_fee(110, 'month', None), 144)

    def test_monthly_rent_max_amount(self):
        self.assertEqual(calculate_membership_fee(8660, 'month', None), 866)

    def test_rent_period_typo(self):
        with self.assertRaises(ValueError):
            calculate_membership_fee(25, 'monthly', None)

    def test_weekly_rent_lower_min_amount(self):
        with self.assertRaises(ValueError):
            calculate_membership_fee(10, 'week', None)

    def test_weekly_rent_higher_max_amount(self):
        with self.assertRaises(ValueError):
            calculate_membership_fee(3000, 'week', None)

    def test_monthly_rent_lower_min_amount(self):
        with self.assertRaises(ValueError):
            calculate_membership_fee(10, 'month', None)

    def test_monthly_rent_higher_max_amount(self):
        with self.assertRaises(ValueError):
            calculate_membership_fee(9000, 'month', None)

    def test_organisation_unit_init(self):
        name = "Test Unit"
        config = OrganisationUnitConfig(True, 500)

        unit = OrganisationUnit(name, config)

        self.assertEqual(unit.name, name)
        self.assertEqual(unit.config, config)


if __name__ == '__main__':
    unittest.main()
