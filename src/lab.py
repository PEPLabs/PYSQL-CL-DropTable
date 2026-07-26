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

_LAB_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


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

    Returns True if the "song" table was successfully dropped (i.e. it can no longer accept inserts),
    False if the table still exists or the student's statement itself failed to run.
    """
    sql = _read_sql("problem1.sql")

    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()

    cur.execute("CREATE TABLE song (Title varchar(100), Artist varchar(100));")
    conn.commit()

    # Step 1: the student's statement must run without error. If it fails here (e.g. it
    # references the wrong table name), that is NOT the same thing as "song" being dropped.
    try:
        cur.execute(sql)
        conn.commit()
    except Exception as e:
        print(f"Exception: {e}\n")
        conn.close()
        return False

    # Step 2: now check specifically whether "song" itself is gone. In programming we utilize
    # try / except constructs to catch when there is potential for errors / exceptions. If we
    # are able to insert a song into the song table, then the song table was never dropped,
    # and problem1() should return False.
    try:
        cur.execute("INSERT INTO song (Title, Artist) VALUES ('Let it be', 'Beatles');")
        conn.commit()
        print("problem1: Table 'song' was not dropped.")
        return False
    except sqlite3.OperationalError:
        # this is the expected outcome - the table no longer exists
        return True
    finally:
        conn.close()