import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("DB_PASSWORD"),
    database="it_asset_db"  # 直接指定資料庫
)

cursor = conn.cursor()

# INSERT 語法：把一筆資料新增到資料表
sql = """
    INSERT INTO assets (name, category, status, location, purchase_date)
    VALUES (%s, %s, %s, %s, %s)
"""

# 要新增的資料
data = ("Dell筆電-001", "筆記型電腦", "使用中", "台北總部3F", "2023-06-01")

cursor.execute(sql, data)
conn.commit()  # 確認寫入，少了這行資料不會真的存進去

print(f"新增成功！資料ID為：{cursor.lastrowid}")

cursor.close()
conn.close()