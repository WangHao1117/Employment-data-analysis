import pandas as pd
import matplotlib.pyplot as plt

# Read data from CSV file
df = pd.read_csv('job_data.csv', encoding='utf-8')

# Function to convert salary string to integer
def convert_salary(salary_str):
    salary_str = salary_str.replace(' ', '')  # Remove any spaces
    if '万' in salary_str:
        return int(float(salary_str.replace('万', '')) * 10000)
    elif '千' in salary_str:
        return int(float(salary_str.replace('千', '')) * 1000)
    else:
        return int(salary_str)

# Convert salary strings to integers
df['MinSalary'] = df['salary'].apply(lambda x: convert_salary(x.split('-')[0]))
df['MaxSalary'] = df['salary'].apply(lambda x: convert_salary(x.split('-')[1]))

# Plot box plot
plt.figure(figsize=(10, 6))
plt.boxplot([df['MinSalary'], df['MaxSalary']], labels=['Min Salary', 'Max Salary'])
plt.title('Salary Distribution (CNY)')
plt.ylabel('Salary')
plt.grid(axis='y')
plt.show()
