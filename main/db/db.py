'''
1. Load to cpu info
2. Load 1 test
3 ... to N test
'''

import sqlite3 as sql3



conn = sql3.connect('data.db')
cursor = conn.cursor()
cursor.execute("")
