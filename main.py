import csv
import time
from playwright.sync_api import sync_playwright

def scrape_facebook():
    posts_data = []
    
    print("正在啟動雲端瀏覽器...")
    with sync_playwright() as p:
        # 啟動無頭瀏覽器 (headless=True 適合在 GitHub Actions 雲端執行)
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        # 設定目標粉絲專頁網址
        target_url = "https://www.facebook.com/sanyeminhgao"
        print(f"正在前往: {target_url}")
        
        try:
            page.goto(target_url, timeout=60000)
            
            # 模擬向下滾動以載入動態貼文（Facebook 需要滾動才會載入內容）
            print("正在向下滾動頁面以載入貼文...")
            for i in range(3):  # 示範滾動 3 次
                page.mouse.wheel(0, 1500)
                time.sleep(3) # 等待網頁載入
            
            # 嘗試抓取貼文文字內容（注意：Facebook 網頁結構常變動，此選擇器為常見範例）
            post_elements = page.locator('div[data-ad-preview="message"]').all_inner_texts()
            
            print(f"成功抓取到 {len(post_elements)} 筆原始貼文內容。")
            
            for index, content in enumerate(post_elements):
                posts_data.append({
                    "index": index + 1,
                    "content": content.replace("\n", " "), # 將換行替換避免破壞 CSV 格式
                    "source_url": target_url
                })
                
        except Exception as e:
            print(f"爬取過程發生錯誤: {e}")
            
        finally:
            browser.close()

    # 將抓取到的資料儲存為 CSV 檔案
    filename = "facebook_posts.csv"
    fieldnames = ["index", "content", "source_url"]
    
    with open(filename, mode="w", encoding="utf-8-sig", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for post in posts_data:
            writer.writerow(post)
            
    print(f"資料已成功寫入至 {filename}")

if __name__ == "__main__":
    scrape_facebook()
