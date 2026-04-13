import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("DB_PASSWORD"),
    database="it_asset_db"
)

cursor = conn.cursor()

# UPDATE 語法：修改指定資料的內容
sql = """
    UPDATE assets
    SET status = %s, location = %s
    WHERE id = %s
"""

# 把 id=1 的設備狀態改為「維修中」，位置改為「資訊室」
data = ("維修中", "資訊室", 1)

cursor.execute(sql, data)
conn.commit()

print(f"更新成功！影響筆數：{cursor.rowcount}")

cursor.close()
conn.close()