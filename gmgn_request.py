import random

import requests
import tls_client
from fake_useragent import UserAgent


def gm_request():
    url = "https://gmgn.ai/defi/quotation/v1/rank/sol/swaps/1h"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        "Referer": "https://gmgn.ai/",
        "Origin": "https://gmgn.ai",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive"
    }

    response = requests.get(url, headers=headers)

    print(response.status_code)
    print(response.text)


class gmgn:
    def __init__(self):
        self.headers = None
        self.user_agent = None
        self.sendRequest = None
        self.identifier = None

    def randomise_request(self):
        self.identifier = random.choice([browser for browser in tls_client.settings.ClientIdentifiers.__args__ if
                                         browser.startswith(('chrome', 'safari', 'firefox', 'opera'))])
        self.sendRequest = tls_client.Session(random_tls_extension_order=True, client_identifier=self.identifier)

        parts = self.identifier.split('_')
        identifier, version, *rest = parts
        other = rest[0] if rest else None

        os = 'windows'
        if identifier == 'opera':
            identifier = 'chrome'
        elif version == 'ios':
            os = 'ios'
        else:
            os = 'windows'

        self.user_agent = UserAgent(browsers=[identifier], os=[os]).random

        self.headers = {
            'Host': 'gmgn.ai',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
            'dnt': '1',
            'priority': 'u=1, i',
            'referer': 'https://gmgn.ai/?chain=sol',
            'user-agent': self.user_agent
        }

    def gm_tls(self):
        self.randomise_request()
        url = "https://gmgn.ai/defi/quotation/v1/rank/sol/swaps/1h"

        # 伪装成真实浏览器
        session = tls_client.Session(client_identifier=self.identifier, random_tls_extension_order=True)

        # headers = {
        #     "User-Agent": self.user_agent,
        #     "Referer": "https://gmgn.ai/",
        #     "Origin": "https://gmgn.ai",
        #     "Accept": "application/json, text/plain, */*",
        #     "Accept-Language": "zh-CN,zh;q=0.9",
        #     "Connection": "keep-alive"
        # }

        response = session.get(url, headers=self.headers)

        print(response.status_code)
        print(response.text)
