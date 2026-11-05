import requests
from bs4 import BeautifulSoup

url = 'https://facebook.com/sanyeminhgao'
headers = {
    'User-Agent': (
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    )
}
response = requests.get(url, headers=headers)
response.encoding = 'utf-8'

# 把下載回來的原始碼存成檔案，方便用記事本打開檢查
with open('debug.html', 'w', encoding='utf-8') as f:
  f.write(response.text)

print('網頁原始碼已儲存至 debug.html')
