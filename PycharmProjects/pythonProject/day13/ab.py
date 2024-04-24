import requests
from bs4 import BeautifulSoup
import os

# 设置基础URL和分页参数
base_url = 'https://universe.roboflow.com/benito/dog-excrements/browse'
params = {
    'queryText': '',
    'pageSize': 50,
    'startingIndex': 0,
    'browseQuery': True
}

# 创建保存图片的文件夹
images_folder = 'downloaded_images'
os.makedirs(images_folder, exist_ok=True)


# 爬取图片的函数
def crawl_images(start_index):
    # 构建完整的URL
    url = base_url + '?' + '&'.join([f'{k}={v}' for k, v in params.items()])
    params['startingIndex'] = start_index

    # 发送请求并获取响应
    response = requests.get(url, params=params)
    response.raise_for_status()

    # 解析HTML内容
    soup = BeautifulSoup(response.text, 'html.parser')

    # 定位包含图片的div元素（这里需要根据实际网页结构调整选择器）
    image_divs = soup.select('div.your-specific-class-or-id')  # 替换为你的CSS选择器

    # 提取并下载图片
    for image_div in image_divs:
        img_tag = image_div.find('img')  # 假设图片在img标签中
        if img_tag:
            img_url = img_tag['src']
            img_response = requests.get(img_url)
            img_response.raise_for_status()

            # 构造图片文件名并保存
            img_filename = os.path.join(images_folder, img_url.split('/')[-1])
            with open(img_filename, 'wb') as img_file:
                img_file.write(img_response.content)
            print(f'Downloaded: {img_filename}')

        # 循环处理分页内容


for i in range(0, 50 * 50, 50):  # some_total_pages 是你估计的总页数，需要根据实际情况调整
    crawl_images(i)