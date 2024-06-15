import csv
import plotly.graph_objs as go
import plotly.io as pio  # 需要先安装plotly库，在终端输入 pip install plotly --user

# 3D图
# 按照职位和职位对应的最高，最低工资绘制三维数据图

# 将薪资字符串转换为整数的函数
def convert_salary(salary_str):
    salary_str = salary_str.replace(' ', '')  # 移除空格
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

# 为职位创建数值表示
job_indices = list(range(len(jobs)))

# 创建一个3D散点图
trace = go.Scatter3d(
    x=job_indices,
    y=min_salaries,
    z=max_salaries,
    text=jobs,
    mode='markers+text',  # 点和文本模式
    marker=dict(
        size=8,
        color=min_salaries,  # 根据最低工资上色
        colorscale='Viridis',  # 颜色渐变
        opacity=0.8
    ),
    textposition='top center'  # 文本位置
)

layout = go.Layout(
    title='不同职位最低和最高工资的3D图',
    scene=dict(
        xaxis=dict(title='职位索引', tickvals=job_indices, ticktext=jobs),
        yaxis=dict(title='最低工资（CNY）'),
        zaxis=dict(title='最高工资（CNY）')
    ),
    margin=dict(l=0, r=0, b=0, t=40),  # 布局边距
)

#  #####
fig = go.Figure(data=[trace], layout=layout)

# 显示图表
pio.show(fig)