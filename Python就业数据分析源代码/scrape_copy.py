# 此文件为爬取类
# 导入selenium模块的webdriver子模块，它提供了操作浏览器的功能
# 使用Selenium进行浏览器自动化
from selenium import webdriver
# 导入selenium模块中的异常类NoSuchElementException，用于处理当尝试查找不存在的元素时抛出的异常
from selenium.common.exceptions import NoSuchElementException

# 导入dump.py
# 从time模块导入sleep函数，用于在代码中添加暂停，以便等待浏览器响应或元素加载
from time import sleep
# 尝试从当前目录下的dump.py文件导入Dump类或函数
# 这行代码假设dump.py文件位于当前工作目录中，并且Dump是一个在dump.py中定义的类或函数
from dump import Dump

class Scrape:
    # __base_url 是类属性
    # 其中的内容替换为
    __base_url = 'file:///D:/大学课程/Python/local-case/PythonDaJobsServer.htm'
    #第二种方法：__base_url = 'http://47.92.254.149:4200/jobs/23201013107/王浩'
    def __init__(self, executable_path, stu_id, stu_name, 
                 sample_html_page = 'sample_html_page.txt', 
                 job_data_file = 'job_data.csv'):
        # 初始化
        self.stu_id = stu_id
        self.stu_name = stu_name
        # 引用Dump类相当于对象的实例化 dump对象  Dump类
        self.dump = Dump(sample_html_page, job_data_file) 
        # driver初始化  
        self.driver = webdriver.Firefox(executable_path=executable_path)

    # 爬取数据    
    def request_sample_html_page(self):
        """ self.driver.get(f'{Scrape.__base_url}{self.stu_id}/{self.stu_name}')
        sleep(3)  
        self.dump.dump_sample_html_page(self.driver.page_source)
         """
                                    # 字符串拼接 网址+id+姓名
                                    # 修改成local-case，只保留Scrape.__base_url
        self.driver.get(Scrape.__base_url)

        sleep(3)
        return self.driver.page_source # 抓取并返回 page_source
    # request_sample_html_page的返回结果，被dump_sample_html_page所调用
    def dump_sample_html_page(self, page_source):    
        self.dump.dump_sample_html_page(page_source)
    
    # 20页有效数据
    def request_jobs(self, page_count=20):
        all_job_list = []
        # 循环20次，每抓一次，刷新一次
        for _ in range(page_count):
            # self.driver.get(f'http://47.92.254.149:4200/jobs/{self.stu_id}/{self.stu_name}')
            self.driver.get('file:///D:/大学课程/Python/local-case/PythonDaJobsServer.htm')
            # 第二种方法：self.driver.get('http://47.92.254.149:4200/jobs/23201013107/王浩')
            sleep(3)
            job_list = self.scrape_job_info()
            print(job_list)
            all_job_list.extend(job_list)
            self.driver.refresh()

        self.dump.dump_job_list(all_job_list)
        self.driver.close()

    def scrape_job_info(self):
        key_list =  ['job','corp','city','district','corp_scale','corp_type',
                       'edu','exp','salary','keyword']

        try:
            job_list = []
            # app_jobs = self.driver.find_element_by_tag_name('app-jobs')
            app_jobs = self.driver.find_element_by_tag_name('app-jobs')
            job_container_list = app_jobs.find_elements_by_class_name('job-container')


            for job_container in job_container_list:
                job = {}

                # 数据提取
                job_title = job_container.find_element_by_class_name('job-title')
                job[key_list[0]] = job_title.text

                job_info = job_container.find_element_by_class_name('job-info')
                span_list = job_info.find_elements_by_tag_name('span')

                for i in range(len(span_list)):
                    job[key_list[i + 1]] = span_list[i].text
                job_list.append(job)
        except NoSuchElementException as no_such_element:
            print(no_such_element.msg)
            print("运行报错")
        finally:
            return job_list
        
# append 用于添加一个元素，无论这个元素是什么类型，都会作为单个元素添加到列表末尾
# extend 用于添加多个元素，它会将可迭代对象中的每个元素分别添加到列表中，从而扩展列表
