import csv
import plotly.express as px
import pandas as pd

""" 根据“公司规模”绘制气泡图，其中按公司规模划分人数
使用 Plotly Express 绘制气泡图，其中气泡大小与公司规模相对应，并按城市着色 """

# Function to convert salary string to integer
def convert_salary(salary_str):
    salary_str = salary_str.replace(' ', '')  # Remove any spaces
    if '万' in salary_str:
        return int(float(salary_str.replace('万', '')) * 10000)
    elif '千' in salary_str:
        return int(float(salary_str.replace('千', '')) * 1000)
    else:
        return int(salary_str)

# Function to convert company size to a numerical range
def convert_company_size(size_str):
    if '-' in size_str:
        return int(size_str.split('-')[1].replace('人', ''))
    elif '以上' in size_str:
        return int(size_str.replace('人以上', ''))
    else:
        return int(size_str.replace('人', ''))

# Read data from CSV file
data = []
with open('job_data.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        salary_range = row['salary'].split('-')
        min_salary = convert_salary(salary_range[0])
        max_salary = convert_salary(salary_range[1])
        company_size = convert_company_size(row['corp_scale'])
        data.append({
            'Job': row['job'],
            'City': row['city'],
            'Company Size': company_size,
            'Min Salary': min_salary,
            'Max Salary': max_salary
        })

# Convert to DataFrame
df = pd.DataFrame(data)

# Create bubble chart
fig = px.scatter(
    df,
    x='City',
    y='Company Size',
    size='Company Size',
    color='City',
    hover_name='Job',
    title='Bubble Chart of Company Size by City',
    labels={'City': 'City', 'Company Size': 'Company Size (Number of People)'},
    size_max=60  # Adjust the size of bubbles
)

# Show plot
fig.show()
