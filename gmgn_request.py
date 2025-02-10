import requests


def gm_request():
    url = "https://gmgn.ai/defi/quotation/v1/rank/sol/swaps/1h?device_id=5cf06822-f597-480e-8ac2-efd016feffe7&client_id=gmgn_web_2025.0208.195617&from_app=gmgn&app_ver=2025.0208.195617&tz_name=Asia%2FShanghai&tz_offset=28800&app_lang=%22zh-CN%22&orderby=swaps&direction=desc&filters[]=renounced&filters[]=frozen"

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
