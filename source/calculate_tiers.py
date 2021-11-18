import queries
import check_value
from functools import partial

def _min_of_values_at_true(bool_list: list, value_list) -> (int, int):
    temp_values = []
    for i in range(len(bool_list)):
        if bool_list[i]: temp_values.append(value_list[i])
    return min(temp_values), value_list.index(min(temp_values))

def _finished_list(values: list) -> bool:
    # Return if all elements in list are -1
    for v in values:
        if v != -1: return False
    return True

def _count_nested(nested: list) -> int:
    count = 0
    for item in nested:
        if type(item) != list:
            count += 1
        else:
            count += _count_nested(item)
    return count

def calculate_tiers(level: int, value_list: list, num_rolls: int, is_fa: bool):
    # Return a nested list detailing the tiers of the rolls that constitute the argument list
    # Each element within the list is in the form
    # x: tier of the roll
    # y: index/location of the roll
    # z: index/location of other half of dual roll/ -1 if solo roll

    if _finished_list(value_list):
        return
    else:
        # Find the smallest double roll and subtract it from every other value in the list
        # Check if the new list is a combination of solos/duals
        is_dual_value_at_lvl = partial(check_value.is_dual_value, level, is_fa)
        bool_is_double_roll = list(map(is_dual_value_at_lvl, value_list))
        dual_values = queries.get_all_tiers_at_level(level, is_fa, 2)
        if any(bool_is_double_roll):
            dual_value_subtracted,dual_vs_index = _min_of_values_at_true(bool_is_double_roll, value_list)
            # value_list.remove(dual_value_subtracted)
            value_list[dual_vs_index] = -1
            for i in range(len(value_list)):
                temp_list = list(value_list)
                if type(temp_list[i]) == int:
                    temp_list[i] -= dual_value_subtracted
                    if temp_list[i] >= 0:
                        # Fix error of solo value index being incorrect since it is the index at the reduced list
                        result = [(dual_values.index(dual_value_subtracted)-1 if not is_fa else
                                   dual_values.index(dual_value_subtracted)+1,dual_vs_index,i),
                                calculate_tiers(level, temp_list, num_rolls-1, is_fa)]
                        if -2 not in result and _count_nested(result) == num_rolls:
                            return result
        else:
            solo_values = queries.get_all_tiers_at_level(level, is_fa, 1)
            is_solo_value_at_lvl = partial(check_value.is_solo_value, level, is_fa)
            bool_is_solo_roll = list(map(is_solo_value_at_lvl, value_list))
            if any(bool_is_solo_roll):
                solo_value_removed, solo_value_index = _min_of_values_at_true(bool_is_solo_roll, value_list)
                # value_list.remove(solo_value_removed)
                value_list[solo_value_index] = -1
                result = [(solo_values.index(solo_value_removed)-1 if not is_fa else
                           solo_values.index(solo_value_removed)+1, solo_value_index, -1),
                        calculate_tiers(level, value_list, num_rolls-1, is_fa)]
                if None in result: result.remove(None)
                if -2 not in result and _count_nested(result) == num_rolls:
                    return result
            else:
                # case where 3 rolls occupy 2 spots, solo & solo & dual on the two solos
                # the fourth roll, if any, must be a solo on the other 2 stats
                # or a dual with the smallest stat being on another index
                reduced_list = [value for value in value_list if value > 0]
                if len(reduced_list) == 2:
                    potential_solo_lists = [[reduced_list[0]-dv,reduced_list[1]-dv] for dv in dual_values[2:]]
                    check_solo_lists = partial(check_value.is_solo_list, level, is_fa)
                    solo_list = list(map(all, map(check_solo_lists, potential_solo_lists)))
                    solo_list_index = solo_list.index(True)
                    result = [(solo_list_index+1 if not is_fa else solo_list_index+3
                               , value_list.index(reduced_list[0]), value_list.index(reduced_list[1])),
                              calculate_tiers(level, [value-dual_values[2+solo_list_index] if value > 0 else value
                                                      for value in value_list], num_rolls-1, is_fa)]
                    if -2 not in result and _count_nested(result) == num_rolls:
                        return result
                return -2