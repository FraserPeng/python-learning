import os
import tarfile
from six.moves import urllib
import pandas as pd
import matplotlib.pyplot as plt

DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml/master/"
HOUSING_PATH = "datasets/housing"
DOWNLOAD_PATH = "scikit-learn/datasets"
HOUSING_URL = DOWNLOAD_ROOT + HOUSING_PATH + "/housing.tgz"


def fetch_housing_data(housing_url=HOUSING_URL, housing_path=HOUSING_PATH):
    '''
    下载housing csv数据
    '''
    if not os.path.isdir(housing_path):
        os.makedirs(housing_path)
        tgz_path = os.path.join(housing_path, "housing.tgz")
    urllib.request.urlretrieve(housing_url, tgz_path)
    housing_tgz = tarfile.open(tgz_path)
    housing_tgz.extractall(path=housing_path)
    housing_tgz.close()


def load_housing_data(housing_path=DOWNLOAD_PATH):
    csv_path = os.path.join(DOWNLOAD_PATH, "housing.csv")
    return pd.read_csv(csv_path)


housing = load_housing_data()
# 默认前5行数据
# print(housing.head())

# 默认后5行数据
# print(housing.tail())


# 数据表基本信息（维度、列名称、数据格式、所占空间等）
# print(housing.info())

# value_counts()一般用在统计有有限个元素的特征（如标签label，地区等） 类似 针对列 group by  并 count
# print(housing["ocean_proximity"].value_counts())

# describe()可以看实数特征的最大值、最小值、平均值、方差、总个数、25%，50%，75%小值。
'''
其中count为总个数，mean为平均值，std为标准差，min为最小值，max为最大值，25%，50%，75%为第25%，50%，75%的最小值。
'''
# print(housing.describe())


housing.hist(bins=50, figsize=(20, 15))
plt.show()
