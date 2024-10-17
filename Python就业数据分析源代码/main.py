from scrape_copy import Scrape

if __name__=="__main__":
    # 创建Scrape类的实例并调用方法
    scrape = Scrape(executable_path=r'C:\geckodriver.exe',
                    stu_id='23201013107', stu_name='王浩',
                    sample_html_page='0303.txt')
   
   # 流程控制，通过简单的流程控制语句实现爬虫的启动和数据请求
    scrape.request_jobs(2)
    print('爬取成功')
