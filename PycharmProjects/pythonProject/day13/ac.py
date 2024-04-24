import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin

# 基础URL和请求头
base_url = 'https://universe.roboflow.com/benito/dog-excrements/browse'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# 创建保存图片的文件夹
images_folder = 'downloaded_images'
os.makedirs(images_folder, exist_ok=True)


# 爬取图片的函数
def crawl_images(starting_index, page_size):
    params = {
        'queryText': '',
        'pageSize': page_size,
        'startingIndex': starting_index,
        'browseQuery': True
    }

    # 发送GET请求
    response = requests.get(base_url, params=params, headers=headers)
    response.raise_for_status()  # 如果请求失败，则抛出异常

    # 解析HTML内容
    soup = BeautifulSoup(response.text, 'html.parser')

    # 找到包含图片的div元素，这里需要具体分析网页结构来确定选择器
    # 假设每个图片都在一个class为"image-container"的div中，你需要根据实际情况调整选择器
    image_divs = soup.select('div.image-container')  # 替换为实际的CSS选择器

    # 遍历div元素并提取图片链接
    for image_div in image_divs:
        img_tag = image_div.find('img')
        if img_tag:
            img_src = img_tag['src']

            # 如果图片链接是相对路径，则使用urljoin将其转换为绝对路径
            if not img_src.startswith('http'):
                img_src = urljoin(base_url, img_src)

                # 下载图片并保存到本地
            img_filename = os.path.join(images_folder, img_src.split('/')[-1])
            with requests.get(img_src, stream=True, headers=headers) as img_response:
                with open(img_filename, 'wb') as img_file:
                    for chunk in img_response.iter_content(chunk_size=8192):
                        img_file.write(chunk)
            print(f'Downloaded: {img_filename}')

        # 设置起始索引和页面大小


starting_index = 0
page_size = 50

# 根据实际情况，你可能需要循环多次来爬取所有图片
crawl_images(starting_index, page_size)