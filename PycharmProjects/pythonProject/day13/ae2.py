import os


def rename_files_sequential(directory, prefix='thumb'):
    """
    将指定目录中的文件按照顺序重新命名。

    :param directory: 包含文件的目录路径。
    :param prefix: 新文件名的前缀。
    """
    # 确保目录存在
    if not os.path.exists(directory):
        print(f"目录 {directory} 不存在。")
        return

        # 获取目录中的所有文件
    files = os.listdir(directory)

    # 过滤出jpg文件
    jpg_files = [f for f in files if f.endswith('.jpg')]

    # 对文件进行顺序重命名
    for i, file in enumerate(jpg_files, start=0):
        # 构造新的文件名
        new_filename = f"{prefix}{i}.jpg"
        # 构造原文件和新文件的完整路径
        old_path = os.path.join(directory, file)
        new_path = os.path.join(directory, new_filename)

        # 检查新文件名是否与旧文件名相同，避免不必要的重命名
        if old_path != new_path:
            # 重命名文件
            os.rename(old_path, new_path)
            print(f"已重命名 {file} 为 {new_filename}")

        # 使用示例


if __name__ == "__main__":
    directory = '/home/zme/图片/dog_poop0422/1'  # 替换为您的图片所在目录
    prefix = 'thumb'  # 新文件名的前缀
    rename_files_sequential(directory, prefix)