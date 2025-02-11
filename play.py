import asyncio
from playwright.async_api import async_playwright

from gmgn_request import gmgn


async def scrape_x_search1():
    async with async_playwright() as p:
        # 启动浏览器
        # browser = await p.chromium.launch(headless=False)  # 先不开启无头模式，方便手动登录
        browser = await p.chromium.launch(
            headless=False,  # 关闭无头模式，方便调试
            args=["--disable-blink-features=AutomationControlled"]
        )
        context = await browser.new_context()
        page = await context.new_page()

        # 访问 X 登录页面
        await page.goto("https://x.com/home")

        # 手动登录（首次运行）
        print("请手动登录 X（Twitter），然后回到终端按 Enter 继续...")
        input()

        # 登录成功后保存 session
        await context.storage_state(path="x_login.json")
        print("✅ 登录状态已保存，文件 x_login.json 生成。请重新运行脚本。")

        await browser.close()

        # asyncio.run(scrape_x_search1())


async def scrape_x_search2():
    gg = gmgn()
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)  # 打开无头模式，方便调试
        gg.randomise_request()
        # context = await browser.new_context(storage_state="x_login.json")
        context = await browser.new_context(
            storage_state="x_login.json",
            user_agent=gg.user_agent,
            ignore_https_errors=True,  # 忽略 HTTPS 错误
            proxy={"server": "http://127.0.0.1:7890"}  # 让 Playwright 走 Clash 代理
        )
        page = await context.new_page()

        # 伪装 Playwright，绕过 X 反爬虫检测
        await page.add_init_script("""
            Object.defineProperty(navigator, 'webdriver', {get: () => undefined});
        """)

        # 访问搜索页面
        search_url = "https://x.com/search?q=7oBYdEhV4GkXC19ZfgAvXpJWp2Rn9pm1Bx2cVNxFpump&src=typed_query"
        # search_url = "http://playwright.dev"
        await page.goto(search_url, timeout=60000, wait_until="domcontentloaded")

        # 检查是否被登出
        if "login" in page.url:
            print("⚠️ X 要求重新登录，请更新 x_login.json")
            await browser.close()
            return

        # 等待推文加载
        await page.wait_for_selector("article", timeout=120000)  # 30 秒超时

        # 获取推文内容
        tweets = await page.locator("article div[data-testid='tweetText']").all_text_contents()

        # 输出推文
        for tweet in tweets:
            print(tweet)

        await browser.close()


asyncio.run(scrape_x_search2())
