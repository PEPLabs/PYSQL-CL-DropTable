import sqlite3
import unittest

from src.main.lab import problem1


class LabTest(unittest.TestCase):
    def test_drop_table(self):
        """
        In programming we utilize try / except constructs to catch when there is potential for errors /
        exceptions. For this test, if we are able to insert a song into the song table, then the song table
        was never dropped, and the test should fail.
        """
        conn = problem1()
        cur = conn.cursor()

        try:
            cur.execute("INSERT INTO song (Title, Artist) VALUES ('Let it be', 'Beatles');")
            conn.commit()
            print("problem1: Table 'song' was not dropped.")
            self.fail("Table 'song' was not dropped.")
        except sqlite3.OperationalError:
            pass
        finally:
            conn.close()


if __name__ == "__main__":
    unittest.main()
