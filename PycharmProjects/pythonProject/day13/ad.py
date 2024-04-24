# import requests
# from bs4 import BeautifulSoup
#
# # 目标URL
# url = 'https://universe.roboflow.com/benito/dog-excrements/browse?queryText=&pageSize=50&startingIndex=0&browseQuery=true'
#
# # 发送HTTP请求
# response = requests.get(url)
#
# # 检查请求是否成功
# if response.status_code == 200:
#     # 解析HTML内容
#     soup = BeautifulSoup(response.text, 'html.parser')
#
#     # 查找你想要的信息，这里只是打印整个页面的内容作为示例
#     print(soup.prettify())
# else:
#     print(f"请求失败，状态码：{response.status_code}")
#
#

import requests

from bs4 import BeautifulSoup

# 目标URL

url = 'https://universe.roboflow.com/benito/dog-excrements/browse?queryText=&pageSize=50&startingIndex=0&browseQuery=true'

# 发送HTTP请求

response = requests.get(url)

# 检查请求是否成功

if response.status_code == 200:

    # 解析HTML内容

    soup = BeautifulSoup(response.text, 'html.parser')

    # 查找具有指定类的div元素

    divs = soup.find_all('div', class_='flex h-full flex-col justify-between md:px-6 xl:px-4')

    # 遍历找到的div元素

    for div in divs:
        # 提取div内部的信息，这里只是简单地打印出来

        print(div.prettify())
        print(1)

else:

    print(f"请求失败，状态码：{response.status_code}")
