import calculate_tiers
import format_output

def print_tiers(tiers: list, level: int, is_fa: bool):
    for roll in tiers:
        format_output.print_stat_tiers(*roll, level, is_fa)

def check_valid_inputs(level: int, stats: list, num_rolls: int, is_fa: bool) -> bool:
    return 0 <= level <= 275 and 0 <= num_rolls <= 4

def input_list() -> list:
    temp_list = []
    for _ in range(4):
        temp_list.append(int(input('Enter the stats: (order: str, dex, int, luk) (-1 if not present)')))
    return temp_list

def bool_input() -> bool:
    is_flame_advantaged = input('Is flame advantaged?: (y/n)')
    if is_flame_advantaged.lower() == 'y':
        return True
    else: return False

def start() -> (int, list, int):
    level = int(input('Enter the equipment level:'))
    stats = input_list()
    num_rolls = int(input('Enter the number of rolls:'))
    flame_advantaged = bool_input()
    return level, stats, num_rolls, flame_advantaged

if __name__ == '__main__':
    temp = start()
    level, num_rolls = temp[0], temp[2]
    while not check_valid_inputs(*temp):
        temp = start()
    is_fa = temp[3]
    temp = calculate_tiers.calculate_tiers(*temp)
    temp = format_output.unpack_nested(temp, num_rolls)
    temp.sort(key=lambda x:x[1])
    print_tiers(temp, level, is_fa)
