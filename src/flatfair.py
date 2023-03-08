def calculate_membership_fee(rent_amount: int, rent_period: str) -> int:
    rent_amount_pence = rent_amount * 100

    # Validate input rent amount
    if rent_period == 'week':
        min_rent = 25 * 100  # £25 per week, converted to pence
        max_rent = 2000 * 100  # £2000 per week, converted to pence
    elif rent_period == 'month':
        min_rent = 110 * 100  # £110 per month, converted to pence
        max_rent = 8660 * 100  # £8660 per month, converted to pence
    else:
        raise ValueError(f"Invalid rent period: {rent_period}, the rent period should be week or month") # Validates rent period

    if rent_amount_pence < min_rent or rent_amount_pence > max_rent:
        raise ValueError(f"Rent amount must be between {min_rent / 100:.2f} and {max_rent / 100:.2f} for the rent period of a {rent_period}")

    # Calculate membership fee
    membership_fee = rent_amount / (52 if rent_period == 'week' else 12)  # One week or month of rent
    membership_fee += membership_fee * 0.2 # Add VAT
    if membership_fee < 120:  # Minimum membership fee is £120 + VAT
        membership_fee = 120 + round(120 * 0.2)

    return int(membership_fee)


print(calculate_membership_fee(110, 'month'))
