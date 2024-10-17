# Python 就业数据分析项目

该项目基于Python进行特定网站的就业数据分析，成功实现了自动化爬虫系统，定期从目标网站抓取最新的就业信息，构建就业信息的数据集，完成了薪资分布、教育程度等多个维度数据可视化，提供了直观的就业市场分析视角。

## 项目结构

```
project/
│
├── job_data.csv             # 原始爬取的就业数据
├── preprocessed_job_data.csv # 预处理后的数据
│
├── jobs.py                  # 使用 numpy 读取 CSV 文件的脚本
├── main.py                  # 爬虫主程序，用于启动爬虫和计算爬取时间
├── dump.py                  # 数据存储类，负责将爬取的数据写入 CSV 文件
├── scrape_copy.py           # 爬虫类，负责网页内容的爬取
├── genfromtxt读取CSV文件.py # 使用 pandas 和 numpy 处理 CSV 文件的脚本
├── 3D_plot.py               # 绘制 3D 图表的脚本
├── Bar_Chart.py             # 绘制柱状图的脚本
├── Pie_Chart.py             # 绘制饼图的脚本
│
└── README.md                # 项目说明文件
```



### 环境要求

- Python 3.x
- Selenium
- pandas
- numpy
- matplotlib
- plotly

### 运行爬虫

1. 确保你已经安装了 GeckoDriver，并且将其路径设置在 `main.py` 中的 `executable_path`。
2. 运行 `main.py` 脚本，爬虫将自动爬取数据并保存到 CSV 文件中。


### 数据预处理

运行 `genfromtxt读取CSV文件.py` 脚本，对原始数据进行预处理，并将结果保存到新的 CSV 文件中。


### 数据可视化

- **3D 图**：[3D_plot.py](Python就业数据分析源代码/111/numpy_job/3D_plot.py)
- **柱状图**：[Bar_Chart.py](Python就业数据分析源代码/111/numpy_job/Bar_Chart.py)
- **饼图**：[Pie_Chart.py](Python就业数据分析源代码/111/numpy_job/Pie_Chart.py)
