import queries

def unpack_nested(nested_list: list, num_rolls: int) -> list:
    for i in range(num_rolls - 1):
        nested_list, temp_list = nested_list[:-1], nested_list[-1]
        nested_list.extend(temp_list)
    return nested_list


def print_stat_tiers(tier: int, roll_index: int, dual_index: int, level:int, is_fa: bool):
    stat_dict = {
        0: 'STR',
        1: 'DEX',
        2: 'INT',
        3: 'LUK'
    }
    if dual_index == -1:
        #solo rolls
        print(f'Tier {tier} {stat_dict[roll_index]}: {queries.get_specific_tier_at_level(level, 1, tier, is_fa)}')

    else:
        #dual rolls
        print(f'Tier {tier} {stat_dict[roll_index]} and {stat_dict[dual_index]}:'
              f' {queries.get_specific_tier_at_level(level, 2, tier, is_fa)}')
