import sqlite3

if __name__ == '__main__':
    SQL_FILE_NAME = "main_solo_vals_flame_advantaged.sql"
    DB_FILE_NAME = "solo_values_FA.db"
    connection = sqlite3.connect(DB_FILE_NAME)
    cursor = connection.cursor()
    file = open(SQL_FILE_NAME)
    read_file = file.read()
    cursor.executescript(read_file)
    connection.close()