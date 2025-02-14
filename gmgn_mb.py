import uiautomator2 as u2


def get_rank_data(device):

    # 找到 HorizontalScrollView 下的所有 ViewGroup
    view_groups = device.xpath("//android.widget.HorizontalScrollView//android.view.ViewGroup").all()

    for index, vg in enumerate(view_groups):
        # 在每个 ViewGroup 下面寻找 TextView
        text_views = d.xpath(".//android.widget.TextView").all()
        for tv in text_views:
            print(f"ViewGroup {index} - TextView Text: {tv.text}")


def get_rank_data2(device):
    scroll_view = device(className="android.widget.HorizontalScrollView")

    if scroll_view.exists:
        view_groups = scroll_view.child(className="android.view.ViewGroup")

        for index, vg in enumerate(view_groups):
            text_views = vg.child(className="android.widget.TextView")
            for tv in text_views:
                print(f"ViewGroup {index} - TextView Text: {tv.get_text()}")
