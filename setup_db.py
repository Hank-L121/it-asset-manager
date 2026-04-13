import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("DB_PASSWORD")
)

cursor = conn.cursor()  # cursor 是用來執行 SQL 指令的工具

# 建立資料庫
cursor.execute("CREATE DATABASE IF NOT EXISTS it_asset_db")
print("資料庫建立成功！")

# 切換到該資料庫
cursor.execute("USE it_asset_db")

# 建立資料表
cursor.execute("""
    CREATE TABLE IF NOT EXISTS assets (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        category VARCHAR(50),
        status VARCHAR(20),
        location VARCHAR(100),
        purchase_date DATE
    )
""")
print("資料表建立成功！")

conn.commit()
cursor.close()
conn.close()