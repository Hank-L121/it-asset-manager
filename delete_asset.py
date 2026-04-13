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

# DELETE 語法：刪除指定資料
sql = "DELETE FROM assets WHERE id = %s"

data = (1,)  # 刪除 id=1 的資料，注意單一值也要加逗號變成 tuple

cursor.execute(sql, data)
conn.commit()

print(f"刪除成功！影響筆數：{cursor.rowcount}")

cursor.close()
conn.close()