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

# SELECT 語法：查詢資料表裡的資料
sql = "SELECT * FROM assets"
cursor.execute(sql)

# fetchall() 把所有查詢結果取出來，回傳一個 list
results = cursor.fetchall()

print("===== 設備清單 =====")
for row in results:
    print(f"ID:{row[0]} | 名稱:{row[1]} | 類別:{row[2]} | 狀態:{row[3]} | 位置:{row[4]} | 購買日期:{row[5]}")

cursor.close()
conn.close()