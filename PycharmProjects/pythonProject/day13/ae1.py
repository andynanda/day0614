import os
import re


def rename_to_sequential(directory, prefix='thumb'):
    """
    将指定目录中的图片文件按照顺序重新命名。

    :param directory: 包含图片文件的目录路径。
    :param prefix: 新文件名的前缀。
    """
    # 确保目录存在
    if not os.path.exists(directory):
        print(f"目录 {directory} 不存在。")
        return

        # 获取目录中的所有文件
    files = os.listdir(directory)

    # 提取文件名中的数字并排序
    numbers = []
    for file in files:
        match = re.search(r'thumb\((\d+)\).jpg', file)
        if match:
            numbers.append(int(match.group(1)))

            # 对数字进行排序
    numbers.sort()

    # 对文件进行重命名
    for i, num in enumerate(numbers, start=1041):
        old_filename = f"thumb({num}).jpg"
        old_path = os.path.join(directory, old_filename)
        new_filename = f"{prefix}{i}.jpg"
        new_path = os.path.join(directory, new_filename)

        # 重命名文件
        os.rename(old_path, new_path)
        print(f"已重命名 {old_filename} 为 {new_filename}")

    # 使用示例


if __name__ == "__main__":
    directory = '/home/zme/图片/dog_poop0422/2'  # 替换为您的图片所在目录
    prefix = 'thumb'  # 新文件名的前缀
    rename_to_sequential(directory, prefix)