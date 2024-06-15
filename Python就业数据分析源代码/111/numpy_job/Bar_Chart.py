import csv
import matplotlib.pyplot as plt

# 从CSV文件中读取数据
edu_levels = []

with open('job_data.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        edu_levels.append(row['edu'])

# 定义要在直方图中显示的教育层次
edu_levels_list = ['大专', '本科', '硕士', '博士', '其它']

# 统计每个教育层次的频率
edu_counts = {level: edu_levels.count(level) for level in edu_levels_list}

# 绘制数据的直方图
fig, ax = plt.subplots()

ax.bar(edu_counts.keys(), edu_counts.values(), color='skyblue')

ax.set_xlabel('教育层次')
ax.set_ylabel('频率')
ax.set_title('教育程度的直方图')

plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体
plt.show()