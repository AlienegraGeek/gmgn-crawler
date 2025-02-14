# This is a sample Python script.
from gmgn_mb import get_rank_data, get_rank_data2
import uiautomator2 as u2

from gmgn_request import gmgn
from play import scrape_x_search2


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    device = u2.connect() # 连接手机
    gg = gmgn()
    # print_hi('PyCharm')
    gg.gm_tls()
    # scrape_x_search2()
    # baidu_driver()
    # get_rank_data(d)
    # get_rank_data2(device)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
