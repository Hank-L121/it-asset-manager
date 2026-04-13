import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("DB_PASSWORD")  # 改成你安裝MySQL時設的密碼
)

if conn.is_connected():
    print("MySQL 連線成功！")
    conn.close()