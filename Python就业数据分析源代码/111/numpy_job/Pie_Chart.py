import csv
import matplotlib.pyplot as plt

# 最高工资和最低工资占比-饼图

# 将薪资字符串转换为整数的函数
def convert_salary(salary_str):
    salary_str = salary_str.replace(' ', '')  # 移除任何空格
    if '万' in salary_str:
        return int(float(salary_str.replace('万', '')) * 10000)
    elif '千' in salary_str:
        return int(float(salary_str.replace('千', '')) * 1000)
    else:
        return int(salary_str)

# 从CSV文件中读取数据
jobs = []
min_salaries = []
max_salaries = []

with open('job_data.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        jobs.append(row['job'])
        salary_range = row['salary'].split('-')
        min_salaries.append(convert_salary(salary_range[0]))
        max_salaries.append(convert_salary(salary_range[1]))

# 绘制数据为饼图
fig, axs = plt.subplots(1, 2, figsize=(14, 7))

# 最低工资的饼图
axs[0].pie(min_salaries, labels=jobs, autopct='%1.1f%%', startangle=90)
axs[0].axis('equal')  # 等比例保证饼图是圆形的
axs[0].set_title('最低工资分布')

# 最高工资的饼图
axs[1].pie(max_salaries, labels=jobs, autopct='%1.1f%%', startangle=90)
axs[1].axis('equal')  # 等比例保证饼图是圆形的
axs[1].set_title('最高工资分布')

plt.rcParams['font.sans-serif'] = ['SimHei']  # 为中文字符使用SimHei字体
plt.show()