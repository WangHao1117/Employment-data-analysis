import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata

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

# Create dummy coordinates for cities
cities = df['City'].unique()
city_coords = {city: (np.random.uniform(-180, 180), np.random.uniform(-90, 90)) for city in cities}
df['Latitude'] = df['City'].apply(lambda city: city_coords[city][0])
df['Longitude'] = df['City'].apply(lambda city: city_coords[city][1])

# Add small random noise to latitude and longitude to avoid Qhull error
df['Latitude'] += np.random.uniform(-0.01, 0.01, size=len(df))
df['Longitude'] += np.random.uniform(-0.01, 0.01, size=len(df))

# Create grid data for contour plot
xi = np.linspace(df['Latitude'].min(), df['Latitude'].max(), 100)
yi = np.linspace(df['Longitude'].min(), df['Longitude'].max(), 100)
zi = griddata((df['Latitude'], df['Longitude']), df['AverageSalary'], (xi[None, :], yi[:, None]), method='cubic')

# Plot the data
plt.figure(figsize=(12, 8))
contour = plt.contourf(xi, yi, zi, levels=15, cmap='YlOrRd')
plt.colorbar(contour, label='Average Salary (CNY)')
plt.title('Contour Map of Average Salaries')
plt.xlabel('Latitude')
plt.ylabel('Longitude')

# Scatter plot for city locations
plt.scatter(df['Latitude'], df['Longitude'], c='black', marker='o')
for i, row in df.iterrows():
    plt.text(row['Latitude'], row['Longitude'], row['City'], fontsize=9)

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.show()
