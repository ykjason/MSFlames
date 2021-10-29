import sqlite3

#roll identifiers:  1 - solo roll
#                   2 - dual roll

def get_all_tiers_at_level(level: int, roll_identifier: int) -> tuple:
    # At the specified table, return the entire row at the corresponding level
    if roll_identifier == 1:
        connection = sqlite3.connect('solo_values.db')
        table = 'solo_vals'
    elif roll_identifier == 2:
        connection = sqlite3.connect('dual_values.db')
        table = 'dual_vals'
    else:
        return ((-1,))

    cursor = connection.cursor()
    # sql_query = 'SELECT * FROM "{a}" WHERE "{b}" <= ? AND "{c}" >= ?'
    result_query = cursor.execute('SELECT * FROM "{}" WHERE "{}" <= ? AND "{}" >= ?'
                                  .format(table, "Min Level".replace('"','""'),
                                    "Max Level".replace('"','""')),(level,level)).fetchone()
    connection.close()
    return result_query

def get_specific_tier_at_level(level: int, roll_identifier: int, tier: int) -> int:
    # Return the stat available at the level range at the specific tier
    # Min and max tiers are 1 and 7 respectively, (the better the tier, the high the tier number)
    if tier not in range(1,8):  # stop is exclusive, must stop at 8
        return -1
    else:
        # first two values indicate levels, corresponding tier at integer is 1 above the int
        return get_all_tiers_at_level(level, roll_identifier)[tier + 1]
