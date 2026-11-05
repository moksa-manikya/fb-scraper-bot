import csv
import os
from playwright.sync_api import sync_playwright

url = "https://facebook.com/sanyeminhgao"
scraped_content = ""
scraped_date = "2026-11-05"

with sync_playwright() as p:
  # 啟動無頭瀏覽器 (headless=True 代表在背景執行，不跳出視窗)
  browser = p.chromium.launch(headless=True)
  page = browser.new_page()

  try:
    # 連線至目標網頁，設定超時時間為 60 秒
    page.goto(url, timeout=60000)

    # 等待頁面載入並取得網頁標題（可依需求改為抓取貼文的 CSS 選擇器）
    page.wait_for_load_timeout(5000)  # 稍微等待 JS 渲染
    scraped_content = page.title()

  except Exception as e:
    scraped_content = f"抓取失敗或被阻擋: {e}"

  browser.close()

# 將結果寫入 data.csv
file_name = "data.csv"
file_exists = os.path.isfile(file_name)

with open(file_name, mode="a", encoding="utf-8-sig", newline="") as f:
  writer = csv.writer(f)
  if not file_exists:
    writer.writerow(["Content", "Date"])
  writer.writerow([scraped_content, scraped_date])

print(f"執行結果：{scraped_content}")
