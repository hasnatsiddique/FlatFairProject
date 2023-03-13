from typing import Optional


class OrganisationUnit:
    def __init__(self, name: str, config: Optional["OrganisationUnitConfig"] = None):
        self.name = name
        self.config = config
        self.parent = None

    def set_parent(self, parent: "OrganisationUnit"):
        self.parent = parent


class OrganisationUnitConfig:
    def __init__(self, has_fixed_membership_fee: bool, fixed_membership_fee_amount: int):
        self.has_fixed_membership_fee = has_fixed_membership_fee
        self.fixed_membership_fee_amount = fixed_membership_fee_amount


def calculate_membership_fee(rent_amount: int, rent_period: str, organisation_unit: OrganisationUnit) -> int:
    rent_amount_pence = rent_amount * 100

    # Validate input rent amount
    if rent_period == 'week':
        min_rent = 25 * 100  # £25 per week, converted to pence
        max_rent = 2000 * 100  # £2000 per week, converted to pence
    elif rent_period == 'month':
        min_rent = 110 * 100  # £110 per month, converted to pence
        max_rent = 8660 * 100  # £8660 per month, converted to pence
    else:
        raise ValueError(
            f"Invalid rent period: {rent_period}, the rent period should be week or month")  # Validates rent period

    if rent_amount_pence < min_rent or rent_amount_pence > max_rent:
        raise ValueError(
            f"Rent amount must be between {min_rent / 100:.2f} and {max_rent / 100:.2f} for the rent period of a {rent_period}")

    # Find the first OrganisationUnitConfig starting from organisation_unit
    config = None
    unit = organisation_unit
    while unit is not None:
        if unit.config is not None:
            config = unit.config
            break
        unit = unit.parent

    # Calculate membership fee
    membership_fee = rent_amount / (52 if rent_period == 'week' else 12)  # One week or month of rent
    membership_fee += membership_fee * 0.2  # Add VAT

    if config is not None and config.has_fixed_membership_fee:
        membership_fee = config.fixed_membership_fee_amount

    if membership_fee < 120:  # Minimum membership fee is £120 + VAT
        membership_fee = 120 + round(120 * 0.2)

    return int(membership_fee)


client = OrganisationUnit("client", OrganisationUnitConfig(False, 0))
division_a = OrganisationUnit("division_a", OrganisationUnitConfig(False, 0))
division_b = OrganisationUnit("division_b", OrganisationUnitConfig(True, 35000))
area_a = OrganisationUnit("area_a", OrganisationUnitConfig(True, 45000))
area_b = OrganisationUnit("area_b", OrganisationUnitConfig(False, 0))
area_c = OrganisationUnit("area_c", OrganisationUnitConfig(True, 45000))
area_d = OrganisationUnit("area_d", OrganisationUnitConfig(False, 0))
branch_a = OrganisationUnit("branch_a")
branch_b = OrganisationUnit("branch_b", OrganisationUnitConfig(False, 0))
branch_c = OrganisationUnit("branch_c", OrganisationUnitConfig(False, 0))
branch_d = OrganisationUnit("branch_d")
branch_e = OrganisationUnit("branch_e", OrganisationUnitConfig(False, 0))
branch_f = OrganisationUnit("branch_f", OrganisationUnitConfig(False, 0))
branch_g = OrganisationUnit("branch_g", OrganisationUnitConfig(False, 0))
branch_h = OrganisationUnit("branch_h", OrganisationUnitConfig(False, 0))
branch_i = OrganisationUnit("branch_i", OrganisationUnitConfig(False, 0))
branch_j = OrganisationUnit("branch_j", OrganisationUnitConfig(False, 0))
branch_k = OrganisationUnit("branch_k", OrganisationUnitConfig(False, 25000))
branch_l = OrganisationUnit("branch_l", OrganisationUnitConfig(False, 0))
branch_m = OrganisationUnit("branch_m")
branch_n = OrganisationUnit("branch_n", OrganisationUnitConfig(False, 0))
branch_o = OrganisationUnit("branch_o", OrganisationUnitConfig(False, 0))
branch_p = OrganisationUnit("branch_p", OrganisationUnitConfig(False, 0))

print(calculate_membership_fee(450, 'month', None))
