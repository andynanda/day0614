from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer
import jieba


def datasets_demp():
    # 对鸢尾花数据集的练习
    # 获取数据集
    iris = load_iris()
    # print("鸢尾花数据集：\n",iris)
    # print("鸢尾花数据集描述：\n", iris["DESCR"])
    # print("查看特征值的名字：\n", iris.feature_names)
    # print("查看特征值：\n", iris.data,"\n",iris.data.shape)

    # 数据集划分
    x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=22)

    print("训练集的特征值：\n", x_train, "\n", x_train.shape)

    return None


def dict_demo():
    """
    字典特征提取

    :return:
    """
    data = [{'city': '北京', 'temperature': 100},
            {'city': '上海', 'temperature': 60},
            {'city': '深圳', 'temperature': 30}]

    # 1.实例化一个转换器类
    transfer = DictVectorizer(sparse=False)
    # 2.调用fit_transfrom()
    data_new = transfer.fit_transform(data)
    # print(data)
    print("data_new:\n", data_new)
    print("特征名字：\n", transfer.get_feature_names_out())

    return None


def count_demo():
    """
    文本特征抽取 CountVecotrizer
    :return:
    """
    data = ["life is short,i like python",
            "life is too long,i dislike python"]

    # 1。 实例化一个转换器
    transfer = CountVectorizer()

    # 2,调用fit_transfrom
    data_new = transfer.fit_transform(data)
    print("data_new:\n", data_new.toarray())
    print("特征名字：\n", transfer.get_feature_names_out())
    return None


def count_chinese_demo():
    """
    文本特征抽取 CountVecotrizer
    :return:
    """
    data = ["不仅提供了大量的基本图像处理函数",
            "还为深度学习领域提供了强大的支持"]

    # 1。 实例化一个转换器
    transfer = CountVectorizer()

    # 2,调用fit_transfrom
    data_new = transfer.fit_transform(data)
    print("data_new:\n", data_new.toarray())
    print("特征名字：\n", transfer.get_feature_names_out())
    return None


def cut_word(text):
    """
    进行中文的分词
    :param text:
    :return:
    """
    a = " ".join(jieba.cut(text))
    print(a)

    return text


def count_chinese_demo2():
    """
    文本特征抽取 CountVecotrizer 自动分词
    :return:
    """
    data = ["数据科学与大数据技术是两个紧密相关但又有一定区别的学科领域。",
            "数据科学是一个跨学科领域，它利用科学方法、流程、算法和系统从数据中提取价值。",
            "数据科学家需要综合利用一系列技能，包括统计学、计算机科学和业务知识，来分析从各种来源（如网络、智能手机、客户、传感器等）收集的数据。",
            "通过揭示趋势并产生见解，数据科学为企业提供了做出更好决策和推出更多创新产品和服务的可能性。",
            "数据科学侧重于数据相关的理论和方法，主要关注数据的获取、处理、分析和可视化等方面。",
            "还为深度学习领域提供了强大的支持"]

    data_new = []

    for sent in data:
        data_new.append(cut_word(sent))
    print(data_new)

    # 1。 实例化一个转换器
    transfer = CountVectorizer(stop_words=["传感器等"])

    # 2,调用fit_transfrom
    data_final= transfer.fit_transform(data_new)
    print("data_new:\n", data_final.toarray())
    print("特征名字：\n", transfer.get_feature_names_out())
    return None


# print(a)

if __name__ == "__main__":
    # 代码1：skearn数据集使用
    # datasets_demp()
    # 代码2：字典特征抽取
    # dict_demo()
    # 代码3：文本特征抽取
    # count_demo()
    # 代码4：中文文本特征抽取
    # count_chinese_demo()
    # 代码5：中文文本特征抽取 自动分词
    count_chinese_demo2()
    # 代码6：中文自动分词
    # cut_word("我爱北京天安门")
