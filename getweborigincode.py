from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import re

# 输入文件路径和输出文件路径
input_file = 'urls.txt'  # 存放网址的文本文件
output_file = 'numbers.txt'  # 保存提取的数字的输出文件

# 设置 WebDriver（使用 Chrome 浏览器）
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # 无窗口模式

# 设置 Chrome 浏览器的路径（根据你的安装路径修改）
options.binary_location = r"D:\Google\Chrome\Application\chrome.exe"  # 修改为你自己的 Chrome 安装路径

# 使用 webdriver-manager 自动下载并管理 chromedriver
service = Service(ChromeDriverManager().install())

# 启动浏览器并传入 service 和 options
driver = webdriver.Chrome(service=service, options=options)

with open(input_file, 'r', encoding='utf-8') as file:
    with open(output_file, 'w', encoding='utf-8') as output:
        for line in file:
            url = line.strip()
            if url:  # 确保不处理空行
                try:
                    # 使用 Selenium 加载网页
                    driver.get(url)
                    time.sleep(3)  # 等待页面完全加载，确保动态内容加载完毕

                    # 获取页面源代码
                    page_source = driver.page_source

                    # 使用正则表达式匹配 openReactionWindow('数字','I')
                    matches = re.findall(r"openReactionWindow\('(\d+)',\s*'I'\)", page_source)
                    if matches:
                        for match in matches:
                            output.write(match + '\n')
                            print(f"提取的数字：{match} 来自 {url}")
                    else:
                        print(f"未在 {url} 找到匹配的数字")

                except Exception as e:
                    print(f"无法访问 {url} 或获取数据：{e}")

driver.quit()
print("所有网址处理完成，数字已保存到 'numbers.txt'。")
