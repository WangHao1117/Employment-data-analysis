import csv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt     # pip install seaborn pandas matplotlib

""" 基于工资水平 """

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

# Melt the DataFrame to have a long format for seaborn
df_melted = df.melt(id_vars=["Job", "City"], value_vars=["Min Salary", "Max Salary"], var_name="Salary Type", value_name="Salary")

# Create violin plot
plt.figure(figsize=(14, 8))
sns.violinplot(x="Job", y="Salary", hue="Salary Type", data=df_melted, split=True, inner="quart", palette="Set3")
plt.xticks(rotation=90)
plt.title('Violin Plot of Salary Levels by Job Position')
plt.xlabel('Job Position')
plt.ylabel('Salary (CNY)')
plt.legend(title="Salary Type", loc='upper left')
plt.tight_layout()

# Show plot
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.show()
