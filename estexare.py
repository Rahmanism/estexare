#!python3

# An estexare app using ayat from estekhare.net

import sys
import random
import sqlite3
from sqlite3 import Error

db = "./estexare.db"
try:
    conn = sqlite3.connect(db)
except Error as e:
    print(e)
    sys.exit(e)

conn.row_factory = sqlite3.Row
cur = conn.cursor()

MAX_ESTEXARE_NO = 181
estexare_no = random.randint(1, MAX_ESTEXARE_NO)
select_estexare_query = f"""
    select * from estexare
    where rowid = {estexare_no}
    """
cur.execute(select_estexare_query)  # , tuple(str(estexare_no)))

estexare_row = cur.fetchone()
print(estexare_row['fi_result'])

if '-f' in sys.argv:
    print(f'{estexare_row["fi_comment"]}\n')
    print(f"Sure: {estexare_row['sure']} ({estexare_row['sure_no']}),", end=" ")
    print(f"Aye: {estexare_row['aye_no']}")
    print(estexare_row['aye'])
elif '-c' in sys.argv:
    print(f'{estexare_row["fi_comment"]}')
