#!python3

# An estexare app using ayat from estekhare.net

import sys
import random
import sqlite3
from sqlite3 import Error

db = "./db.db"
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

lang = 'fi'

if '-l' in sys.argv:
    try:
        a_lang = sys.argv[sys.argv.index('-l') + 1]
        if a_lang in ['fi', 'fa', 'en']:
            lang = a_lang
        else:
            print('The language is not in deinfed languages. Finglish is default.')
    except IndexError as x:
        print('No language is declared.')

print(estexare_row[lang + '_result'])
if '-f' in sys.argv:
    print(f'{estexare_row[lang + "_comment"]}\n')
    print(f"Sure: {estexare_row['sure']} ({estexare_row['sure_no']}),", end=" ")
    print(f"Aye: {estexare_row['aye_no']}")
    print(estexare_row['aye'])
elif '-c' in sys.argv:
    print(f'{estexare_row[lang + "_comment"]}')
