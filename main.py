#calculate the factors of the total flames
import sqlite3
import queries
import check_value
import calculate_tiers
import format_output

def start_old():
    connection = sqlite3.connect('dual_values.db')
    # file = open("solo_values.sql")
    # read_file = file.read()
    cursor = connection.cursor()
    #cursor = connection.execute("SELECT * from solovals WHERE 'Min Level' <= 140 AND 'Max Level' >= 140")
    # for i in read_file:
    # cursor.executescript(read_file)
    for row in cursor.execute('SELECT * FROM dual_vals'):
        print(row)
    connection.close()

def start() -> (int, list):
    level = input('Enter the equipment level:')
    stats = [input('Enter the stats: (order: str, dex, int, luk)')]

    return level, stats


if __name__ == '__main__':
    print('PyCharm')
    print(queries.get_specific_tier_at_level(140, 1, 7))
    print(check_value.is_solo_list(140, [32, 32, 32, 33]))
    temporary_roll = [115, 30, -1, 30]
    x = calculate_tiers.calculate_tiers(200, temporary_roll, 3)
    print(x)
    # print(format_output.unpack_nested(x, 4))
    x = format_output.unpack_nested(x, 3)
    x.sort(key=lambda x:x[1])
    print(x)
    for i in x:
        format_output.print_stat_tiers(*i, 200)


