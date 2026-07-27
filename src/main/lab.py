import os
import sqlite3

"""
SQL sublanguage: DDL (Data Definition Language)

In the last activity we learned how to create tables in SQL. In this activity we are going to learn how to drop a
table from our database.

The syntax for dropping a table is as follows:
DROP TABLE table_name;
"""

# The lab's root folder (the parent of this "src" folder). Computed from this file's own
# location rather than the current working directory, so problemN.sql is always found no
# matter where this script is launched from.
_LAB_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def _read_sql(filename):
    with open(os.path.join(_LAB_DIR, filename), "r", encoding="utf-8") as f:
        return f.read().strip()


def problem1():
    """
    Task: Drop the table "song"
    song Table Diagram:
    |      title        |        artist         |
    ---------------------------------------------
    |'Let it be'        |'Beatles'              |
    |'Hotel California' |'Eagles'               |
    |'Kashmir'          |'Led Zeppelin'         |

    NOTE: Do not change anything in this code. You should write your sql statement on a single line (do not use
    multi-line formatting) in the problem1.sql file.

    Sets up the "song" table, runs the student's statement against it, and returns the open connection so the
    caller can verify whether the table was actually dropped.
    """
    sql = _read_sql("problem1.sql")

    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    cur.execute("CREATE TABLE song (Title varchar(100), Artist varchar(100));")
    conn.commit()

    try:
        cur.execute(sql)
        conn.commit()
    except Exception as e:
        print(f"problem1: {e}\n")

    return conn
