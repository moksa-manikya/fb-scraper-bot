Python
import csv
import os

# 模擬抓取下來的資料
scraped_data = ["這是第一篇測試貼文內容", "2026-11-05"]

file_name = "data.csv"
file_exists = os.path.isfile(file_name)

# 寫入 CSV 檔案 (使用 utf-8-sig 確保 Excel 開啟中文不亂碼)
with open(file_name, mode="a", encoding="utf-8-sig", newline="") as f:
  writer = csv.writer(f)
  if not file_exists:
    writer.writerow(["Content", "Date"])
  writer.writerow(scraped_data)

print("資料已成功寫入 data.csv！")