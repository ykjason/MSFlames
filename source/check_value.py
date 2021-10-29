import queries

def is_solo_value(level: int, value: int) -> bool:
    # Return whether or not the value at the specified level is a valid roll
    return value in queries.get_all_tiers_at_level(level, 1)

def is_dual_value(level: int, value: int) -> bool:
    # Functions the same as above, could be replaced with an additional parameter
    return value in queries.get_all_tiers_at_level(level, 2)

def is_solo_list(level: int, value_list: list) -> list:
    # Check if all values in the list are solo rolls
    solo_values = queries.get_all_tiers_at_level(level, 1)
    return [value in solo_values for value in value_list]

