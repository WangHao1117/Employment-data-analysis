import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

""" 基于工资水平绘制热图 """

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
            'MinSalary': min_salary,
            'MaxSalary': max_salary
        })

# Convert to DataFrame
df = pd.DataFrame(data)

# Calculate average salary
df['AverageSalary'] = (df['MinSalary'] + df['MaxSalary']) / 2

# Create pivot table for heatmap
heatmap_data = df.pivot_table(values='AverageSalary', index='City', aggfunc=np.mean)

# Draw heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(heatmap_data, annot=True, cmap='YlOrRd', cbar_kws={'label': 'Average Salary (CNY)'})
plt.title('Heat Map of Average Salaries by City')
plt.xlabel('City')
plt.ylabel('Average Salary (CNY)')
plt.show()
