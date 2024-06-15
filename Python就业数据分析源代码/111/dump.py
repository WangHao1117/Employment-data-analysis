# 此为存储类代码
# 对应 scrape.py，需要先创建dump.py 再进行导入
# 是json模块的一个函数，用于将Python对象转换为JSON格式的字符串，并写入文件
import csv
class Dump:
    # 蓝色形参，橙色实参
    def __init__(self, sample_html_page = 'sample_html_page.txt',
                 job_data_file = 'job_data.csv'):
        
        self.sample_html_page = sample_html_page
        self.job_data_file = job_data_file
        self.columns = []

    def dump_sample_html_page(self, page_source):
        with open(self.sample_html_page, 'w', encoding='utf-8') as file:
            file.write(page_source)

    # 文件中的内容
    def dump_job_list(self, job_list):
        with open(self.job_data_file,'w',encoding='utf-8', newline='') as file:
            # newline=''  在写入CSV文件时，确保在写入时不插入额外的行终止
            columns = ['job','corp','city','district','corp_scale','corp_type',
                       'edu','exp','salary','keyword']
             # CSV文件写入   将数据以字典形式写入CSV
            csvwriter = csv.DictWriter(file, fieldnames=columns)
            # 创建一个写入器对象（以字典的形式写入数据，其中字典的键对应于列名）

            csvwriter.writeheader()
            csvwriter.writerows(job_list)