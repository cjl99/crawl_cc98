import requests
from bs4 import BeautifulSoup
import json

# 定义要爬取的页面范围，根据时间排序的帖子
start_id = ???????  
end_id = ???????

# 爬取的数据结果
titles = []

for id in range(start_id, end_id + 1):
    url = f"https://api.cc98.org/Topic/{id}/post?from=0&size=10"  
    headers = {
        "Authorization": "fill-in-your-token-here"  # Replace with the token copied from the browser
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        print("爬取成功：", id)

        # 遍历 list[dict] 中每一个, 提取出 not-null 的 tǐtle
        for item in data:
            if item["title"] is not None and item["likeCount"]>20: # 筛选条件 赞比较多
                titles.append({"id":id, "title":item["title"], "data":item["content"]})
                break
    else:
        print(f"无法访问页面：{url}")

# 保存数据
print(titles)
with open("titles.json", "w", encoding="utf-8") as f:
    json.dump(titles, f, ensure_ascii=False, indent=4)
