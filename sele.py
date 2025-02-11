from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC


def x_driver():
    # 设置 Chrome 选项
    options = webdriver.ChromeOptions()
    options.add_argument("--user-data-dir=selenium_x_profile")  # 使用本地浏览器缓存，保持登录状态
    options.add_argument("--headless")  # 无头模式（不打开浏览器窗口）
    options.add_argument("--disable-blink-features=AutomationControlled")

    service = webdriver.ChromeService()
    service.path = "/Users/yuvan/Downloads/chromedriver-mac-x64/chromedriver"
    # 启动浏览器 /Users/yuvan/Downloads/chromedriver-mac-x64
    driver = webdriver.Chrome(service=service, options=options)
    # driver.get("https://x.com/search?q=7oBYdEhV4GkXC19ZfgAvXpJWp2Rn9pm1Bx2cVNxFpump&src=typed_query")

    # input("请手动登录 X（Twitter），然后按 Enter 继续...")

    # 访问搜索页面
    search_url = "https://x.com/search?q=7oBYdEhV4GkXC19ZfgAvXpJWp2Rn9pm1Bx2cVNxFpump&src=typed_query"
    driver.get(search_url)
    WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "root"))
            )
    # time.sleep(3)  # 等待页面加载
    # 获取搜索结果
    tweets = driver.find_elements(By.XPATH, "//div[@data-testid='tweetText']")
    for tweet in tweets:
        print(tweet.text)

    driver.quit()


def baidu_driver():
    # url = "https://evm.ink/address/0xf6372ef94026f71e5e48f0ff2ff5ceb06fdff303"
    url = 'http://www.baidu.com'
    chrome_options = Options()
    # chrome_options.add_argument('--headless')
    driver_path = '/Users/yuvan/Downloads/chromedriver-mac-x64/chromedriver'
    s = Service(driver_path)
    driver = webdriver.Chrome(service=s, options=chrome_options)
    driver.get(url)
    print('open success')
