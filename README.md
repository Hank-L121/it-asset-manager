# IT 資產管理系統

## 專案簡介
本系統為模擬企業 MIS 部門日常資產管理需求所開發的命令列工具，
使用 Python 與 MySQL 實作完整的設備資料管理功能，
並支援 Excel 報表匯出，適用於中小型企業 IT 設備的盤點與追蹤。

## 使用技術
- **語言**：Python 3.9
- **資料庫**：MySQL 8.0
- **套件**：mysql-connector-python、openpyxl
- **工具**：VS Code

## 功能說明
| 功能 | 說明 |
|------|------|
| 新增設備 | 輸入設備名稱、類別、狀態、位置、購買日期，寫入資料庫 |
| 查詢設備 | 列出資料庫中所有設備資料 |
| 更新狀態 | 依設備 ID 修改設備狀態與位置 |
| 刪除設備 | 依設備 ID 刪除指定設備資料 |
| 搜尋設備 | 依名稱、類別、狀態、位置進行關鍵字模糊搜尋 |
| 匯出報表 | 將設備清單匯出為 Excel 檔案，檔名包含時間戳記 |

## 資料庫結構
資料庫名稱：`it_asset_db`

資料表：`assets`

| 欄位 | 型別 | 說明 |
|------|------|------|
| id | INT, AUTO_INCREMENT | 設備唯一識別碼（主鍵） |
| name | VARCHAR(100) | 設備名稱 |
| category | VARCHAR(50) | 設備類別 |
| status | VARCHAR(20) | 設備狀態（使用中／維修中／報廢） |
| location | VARCHAR(100) | 設備所在位置 |
| purchase_date | DATE | 購買日期 |

## 執行方式
1. 確認已安裝 Python 3.9 與 MySQL 8.0
2. 安裝相依套件：
```
pip install mysql-connector-python openpyxl
```
3. 執行資料庫初始化：
```
python setup_db.py
```
4. 啟動主程式：
```
python main.py
```

## 學習重點
- SQL CRUD 操作（INSERT / SELECT / UPDATE / DELETE）
- SQL WHERE 條件查詢與 LIKE 模糊搜尋
- Python 函式設計與模組化
- Python 例外處理（try / except）
- Python 操作 MySQL 資料庫（mysql-connector）
- Python 產生 Excel 報表（openpyxl）

## 開發者
李柏翰 ／ LEE PO-HAN