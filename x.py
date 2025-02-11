import requests
from bs4 import BeautifulSoup

url = "https://x.com/search?q=7oBYdEhV4GkXC19ZfgAvXpJWp2Rn9pm1Bx2cVNxFpump&src=typed_query"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
}

response = requests.get(url, headers=headers)
print(response.text)  # 打印网页内容

soup = BeautifulSoup(response.text, "html.parser")
tweets = soup.find_all("div", class_="css-901oao")  # 查找可能的推文内容
for tweet in tweets:
    print(tweet.text)
