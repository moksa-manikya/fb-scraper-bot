import csv
import os
from bs4 import BeautifulSoup
import requests

# 1. 設定要爬取的目標網頁網址 (這裡以範例公開網站為例)
url = "https://facebook.com/sanyeminhgao/"  # 請替換成你想抓取的真實網頁網址

# 2. 發送 HTTP 請求取得網頁內容
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    )
}
response = requests.get(url, headers=headers)
response.encoding = "utf-8"  # 確保中文不會亂碼

scraped_content = ""
scraped_date = "2026-11-05"  # 或使用 datetime 自動取得當天日期

if response.status_code == 200:
  # 3. 使用 BeautifulSoup 解析 HTML
  soup = BeautifulSoup(response.text, "html.parser")

  # 4. 尋找目標元素 (例如抓取網頁的第一個 <h1> 標題作為範例)
  target_element = soup.find("h1")
  if target_element:
    scraped_content = target_element.text.strip()
  else:
    scraped_content = "未找到指定標題"
else:
  scraped_content = f"連線失敗，狀態碼: {response.status_code}"

# 5. 將抓取到的真實資料寫入 data.csv
file_name = "data.csv"
file_exists = os.path.isfile(file_name)

with open(file_name, mode="a", encoding="utf-8-sig", newline="") as f:
  writer = csv.writer(f)
  if not file_exists:
    writer.writerow(["Content", "Date"])
  writer.writerow([scraped_content, scraped_date])

print(f"成功抓取並寫入資料：{scraped_content}")
