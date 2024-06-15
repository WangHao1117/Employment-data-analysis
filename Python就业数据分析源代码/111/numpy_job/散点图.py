import csv
import plotly.express as px
import pandas as pd         # pip install pandas

# 绘制基于城市的散点图，并根据薪资

# Function to convert salary string to integer
def convert_salary(salary_str):
    salary_str = salary_str.replace(' ', '')  # Remove any spaces
    if '万' in salary_str:
        return int(float(salary_str.replace('万', '')) * 10000)
    elif '千' in salary_str:
        return int(float(salary_str.replace('千', '')) * 1000)
    else:
        return int(salary_str)

# Read data from CSV file
data = []
with open('job_data.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        salary_range = row['salary'].split('-')
        min_salary = convert_salary(salary_range[0])
        max_salary = convert_salary(salary_range[1])
        data.append({
            'Job': row['job'],
            'City': row['city'],
            'Min Salary': min_salary,
            'Max Salary': max_salary
        })

# Convert to DataFrame
df = pd.DataFrame(data)

# Create scatter plot
fig = px.scatter(
    df,
    x='City',
    y='Min Salary',
    size='Max Salary',
    color='City',
    hover_name='Job',
    title='Scatter Plot of Job Salaries by City',
    labels={'City': 'City', 'Min Salary': 'Minimum Salary (CNY)'}
)

# Show plot
fig.show()
