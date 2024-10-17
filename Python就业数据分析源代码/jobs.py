import numpy as np


job_csv =  np.genfromtxt('job_data.csv',   # 文件名
                         delimiter=',',    # 逗号分割
                         names=True,       # 要表头名字
                         dtype=None,       # 不指定类型
                         encoding='utf-8'
                         )

print(job_csv)
