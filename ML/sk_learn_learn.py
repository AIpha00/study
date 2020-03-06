# -*- coding: utf-8 -*-
"""
 author: lvsongke@oneniceapp.com
 data:2019/09/11
"""
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.preprocessing import MinMaxScaler
import jieba


def dictvec():
    _dict = DictVectorizer(sparse=False)
    data = _dict.fit_transform(
        [{'city': '北京', 'temperature': 100}, {'city': '上海', 'temperature': 80}, {'city': '深圳', 'temperature': 30}])

    print(_dict.get_feature_names())
    print(data)


def textvec():
    cv = CountVectorizer()
    data = cv.fit_transform(['人生苦短，我用python', '人生漫长，我不想用python'])
    print(cv.get_feature_names())
    print(data.toarray())
    '''
    ['dislike', 'is', 'life', 'like', 'long', 'python', 'short', 'too']  // 统计所有文章当中的所有词，重复的只做一次。      词的列表
    [[0 2 1 1 0 1 1 0]    // 对每片文章，在词的列表里面进行统计每个词出现的次数
    [1 1 1 0 1 1 0 1]]    // 单个字母不做统计
    
    '''
    pass


def hanzivec():
    cv = CountVectorizer()
    tf_itd = TfidfVectorizer()
    text = '如果您还没有安装 NumPy 或 SciPy，还可以使用 conda 或 pip 来安装它们。 当使用 pip 时，请确保使用了 binary wheels，并且 NumPy 和 SciPy 不会从源重新编译，这可能在使用操作系统和硬件的特定配置（如 Raspberry Pi 上的 Linux）时发生。 从源代码构建 numpy 和 scipy 可能是复杂的（特别是在 Windows 上），并且需要仔细配置，以确保它们与线性代数程序的优化实现链接。而是使用如下所述的第三方发行版。'
    con1 = jieba.cut(text)
    # print(list(con1))
    con1_list = list(con1)
    data = cv.fit_transform([' '.join(con1_list)])
    data_tf = tf_itd.fit_transform([' '.join(con1_list)])
    print(data_tf)
    print(data_tf.toarray())

    print(cv.get_feature_names())
    print(data.toarray())
    pass


def mm():
    '''
    归一化
    :return:
    '''
    mm_ = MinMaxScaler(feature_range=(2, 3))
    data = mm_.fit_transform([[90, 2, 10, 40], [60, 4, 15, 45], [75, 3, 13, 46]])
    print(data)


if __name__ == '__main__':
    # dictvec()
    # textvec()
    # hanzivec()
    mm()
