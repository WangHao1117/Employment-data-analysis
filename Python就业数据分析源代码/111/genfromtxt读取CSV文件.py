import pandas as pd
import numpy as np
import os

# 定义一个预处理薪资的函数
def preprocess_salary(salary):
    # 将中文数字字符替换为它们的数值等价物
    salary = salary.replace('千', '000').replace('万', '0000').replace(' ', '')
    return salary

file_path = r'E:\王浩\job_data.csv'

# 检查文件是否存在
if os.path.exists(file_path):
    """ Pandas数据处理，使用pd.read_csv读取CSV文件，并利用apply方法应用预处理函数 """
    # 使用 pandas 读取 CSV 文件
    df = pd.read_csv(file_path, encoding='utf-8')

    # 预处理薪资列
    df['salary'] = df['salary'].apply(preprocess_salary)

    # 把处理后的数据保存到新的 CSV 文件
    preprocessed_fname = r'E:\王浩\preprocessed_job_data.csv'
    df.to_csv(preprocessed_fname, index=False, encoding='utf-8')

    # 使用 numpy 加载预处理后的数据
    data = np.genfromtxt(preprocessed_fname, delimiter=',', names=True, dtype=None, encoding='utf-8')

    # 打印数据
    print()
    print(data)
    print()


    # 访问列名称
    print("列名称:", data.dtype.names)
    print()

    # 访问数据形状
    print("数据形状:", data.shape)
    print()

    # 访问特定列
    print("城市列:", data['city'])
    print()

    # 访问特定行
    print("第一行:", data[0])
    print()
else:
    print(f"文件未找到: {file_path}")