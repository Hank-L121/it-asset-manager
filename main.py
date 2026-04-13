import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()
import openpyxl
from datetime import datetime

# 建立連線的函式，之後每個操作都呼叫這個
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password=os.getenv("DB_PASSWORD"),
        database="it_asset_db"
    )

# 新增設備
def add_asset(name, category, status, location, purchase_date):
    conn = get_connection()
    cursor = conn.cursor()
    sql = """
        INSERT INTO assets (name, category, status, location, purchase_date)
        VALUES (%s, %s, %s, %s, %s)
    """
    data = (name, category, status, location, purchase_date)
    cursor.execute(sql, data)
    conn.commit()
    print(f"新增成功!資料ID為:{cursor.lastrowid}")
    cursor.close()
    conn.close()

# 查詢所有設備
def query_all():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM assets")
    results = cursor.fetchall()
    if not results:
        print("目前沒有任何設備資料")
    else:
        print("\n===== 設備清單 =====")
        for row in results:
            print(f"ID:{row[0]} | 名稱:{row[1]} | 類別:{row[2]} | 狀態:{row[3]} | 位置:{row[4]} | 購買日期:{row[5]}")
    cursor.close()
    conn.close()

# 更新設備狀態
def update_asset(asset_id, status, location):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "UPDATE assets SET status = %s, location = %s WHERE id = %s"
    cursor.execute(sql, (status, location, asset_id))
    conn.commit()
    print(f"更新成功！影響筆數：{cursor.rowcount}")
    cursor.close()
    conn.close()

# 刪除設備
def delete_asset(asset_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM assets WHERE id = %s", (asset_id,))
    conn.commit()
    print(f"刪除成功！影響筆數：{cursor.rowcount}")
    cursor.close()
    conn.close()

# 匯出設備清單到 Excel
def export_to_excel():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM assets")
    results = cursor.fetchall()
    
    # 建立 Excel 檔案
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "設備清單"
    
    # 寫入標題列
    ws.append(["ID", "設備名稱", "類別", "狀態", "位置", "購買日期"])
    
    # 寫入每筆資料
    for row in results:
        ws.append(list(row))
    
    # 用日期當檔名，避免覆蓋舊檔
    filename = f"設備清單_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
    wb.save(filename)
    print(f"匯出成功！檔案名稱：{filename}")
    
    cursor.close()
    conn.close()

# 依條件搜尋設備
def search_asset(keyword, search_type):
    conn = get_connection()
    cursor = conn.cursor()
    
    if search_type == "1":  # 依名稱搜尋
        sql = "SELECT * FROM assets WHERE name LIKE %s"
    elif search_type == "2":  # 依類別搜尋
        sql = "SELECT * FROM assets WHERE category LIKE %s"
    elif search_type == "3":  # 依狀態搜尋
        sql = "SELECT * FROM assets WHERE status LIKE %s"
    elif search_type == "4":  # 依位置搜尋
        sql = "SELECT * FROM assets WHERE location LIKE %s"
    
    # % 是 SQL 的萬用字元，代表任意字元
    # 例如搜尋 "筆電" 會找到 "Dell筆電-001"、"HP筆電-002" 等
    cursor.execute(sql, (f"%{keyword}%",))
    results = cursor.fetchall()
    
    if not results:
        print(f"找不到符合「{keyword}」的設備")
    else:
        print(f"\n===== 搜尋結果：{len(results)} 筆 =====")
        for row in results:
            print(f"ID:{row[0]} | 名稱:{row[1]} | 類別:{row[2]} | 狀態:{row[3]} | 位置:{row[4]} | 購買日期:{row[5]}")
    
    cursor.close()
    conn.close()

# 主選單
def main():
    while True:
        print("\n===== IT 資產管理系統 =====")
        print("1. 新增設備")
        print("2. 查詢所有設備")
        print("3. 更新設備狀態")
        print("4. 刪除設備")
        print("5. 搜尋設備")
        print("6. 匯出 Excel 報表")
        print("7. 離開")
        
        choice = input("請選擇功能（1-7）：")
        
        if choice == "1":
            name = input("設備名稱：")
            category = input("類別：")
            status = input("狀態：")
            location = input("位置：")
            
            while True:
                purchase_date = input("購買日期（格式 2024-01-01）：")
                try:
                    from datetime import datetime
                    datetime.strptime(purchase_date, "%Y-%m-%d")
                    break
                except ValueError:
                    print("日期格式錯誤，請重新輸入（格式：2024-01-01）")
            
            add_asset(name, category, status, location, purchase_date)
        
        elif choice == "2":
            query_all()
        
        elif choice == "3":
            asset_id = input("請輸入要更新的設備ID：")
            status = input("新狀態：")
            location = input("新位置：")
            update_asset(asset_id, status, location)
        
        elif choice == "4":
            asset_id = input("請輸入要刪除的設備ID：")
            delete_asset(asset_id)
        
        elif choice == "5":
            print("\n搜尋方式：")
            print("1. 依名稱搜尋")
            print("2. 依類別搜尋")
            print("3. 依狀態搜尋")
            print("4. 依位置搜尋")
            search_type = input("請選擇搜尋方式（1-4）：")
            keyword = input("請輸入關鍵字：")
            search_asset(keyword, search_type)

        elif choice == "6":
            export_to_excel()

        elif choice == "7":
            print("已離開系統")
            break
        
        else:
            print("無效選項，請重新輸入")
main()