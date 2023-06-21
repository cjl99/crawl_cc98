## 爬取 CC98，记录一下事项
0. 先确定一个 id 范围（这个id根据时间来的）
1. CC98 需要一个 Authorization 认证，自己登陆一下网页，F12 看一下 Get 中的字段，复制过来就好
2. 数据都在 `https://api.cc98.org/Topic/{id}/post?from=0&size=10` 
4. postprocess 根据like 数量做了简单过滤

环境只需要 `pip install requests beautifulsoup4 `

`test.py` 测试一下 一个网页的爬取效果

`crawl_data.py` 爬取id范围