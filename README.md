```markdown

# 就业信息爬虫与分析项目

此项目是基于Python进行特定网站的就业数据分析，成功实现了自动化爬虫系统，定期从目标网站抓取最新的就业信息，构建就业信息的数据集，完成了薪资分布、教育程度等多个维度数据可视化，提供了直观的就业市场分析视角。

## 项目结构

```
employment_crawler/
│
├── scrape_copy.py       # 爬虫主模块
├── main.py             # 爬虫入口和流程控制
├── jobs.py             # 数据处理和分析模块
├── dump.py             # 数据存储类
├── genfromtxt读取CSV文件.py   # 使用numpy读取CSV文件
├── Bar_Chart.py        # 绘制教育程度直方图
├── 3D_plot.py          # 绘制3D工资分布图
├── Pie_Chart.py        # 绘制工资分布饼图
├── job_data.csv        # 原始爬取数据
└── preprocessed_job_data.csv  # 预处理后的数据
```

## 如何运行

1. **安装依赖**：确保已安装`selenium`、`numpy`、`pandas`、`matplotlib`、`plotly`等库。
   ```bash
   pip install selenium numpy pandas matplotlib plotly
   ```

2. **配置爬虫**：在`main.py`中设置正确的`executable_path`和其他参数。

3. **启动爬虫**：运行`main.py`文件启动爬虫。
   ```bash
   python main.py
   ```

4. **数据预处理**：运行`genfromtxt读取CSV文件.py`对原始数据进行预处理。

5. **数据分析**：运行`Bar_Chart.py`、`3D_plot.py`和`Pie_Chart.py`进行数据分析和可视化。

## 数据分析图表

- **教育程度直方图**：[Bar_Chart.py](Bar_Chart.py) 查看不同教育程度的就业信息分布。
- **3D工资分布图**：[3D_plot.py](3D_plot.py) 查看不同职位的最低和最高工资分布。
- **工资分布饼图**：[Pie_Chart.py](Pie_Chart.py) 查看最低和最高工资的占比分布。

## 贡献与反馈

欢迎对本项目提出改进意见或贡献代码。

## 许可证

本项目采用[MIT许可证]。请在遵守许可证的前提下使用和分发本项目。
