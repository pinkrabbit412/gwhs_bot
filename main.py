import sys
import mariadb

from DBServerAccount import *

# 1. Connect to MariaDB server
try:
    conn = mariadb.connect (
        user = DBServerAccount.MariaDB_ID,
        password = DBServerAccount.MariaDB_PW,
        host = "127.0.0.1",
        port = 3306,
        database = "sample"
    )
except mariadb.Error as e:
    print("[!] DB 서버에 연결할 수 없습니다. 프로그램을 종료합니다.")
    print("    - ", e)
    sys.exit(1)

# 2. Get cursor
db_cursor = conn.cursor()

db_cursor.execute("SELECT field1, field2 from sampletable")
for (field1, field2) in db_cursor:
    print(f"밥: {field1}, 국/찌개: {field2}")
