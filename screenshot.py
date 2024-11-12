from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import os

# 输入文件路径和截图保存文件夹
input_file = 'urls.txt'  # 存放网址的文本文件
output_folder = 'screenshots'  # 保存截图的文件夹

# 创建保存截图的文件夹（如果文件夹不存在）
os.makedirs(output_folder, exist_ok=True)

# 初始化 WebDriver（使用 Chrome 浏览器）
options = Options()
options.add_argument('--headless')  # 无窗口模式
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# 指定 Chrome 浏览器的路径
options.binary_location = r'D:\Google\Chrome\Application\chrome.exe'  # 修改为你的实际路径

# 使用 webdriver-manager 自动下载和安装 ChromeDriver
service = Service(ChromeDriverManager().install())

# 创建 WebDriver 实例并传递 service 和 options
driver = webdriver.Chrome(service=service, options=options)

# 从文本文件中读取网址并逐个截图
with open(input_file, 'r', encoding='utf-8') as file:
    for index, line in enumerate(file, start=1):
        url = line.strip()
        if url:  # 确保不处理空行
            try:
                # 打开网页并等待加载
                driver.get(url)
                time.sleep(2)  # 根据需要调整加载时间
                
                # 设置截图窗口大小
                driver.set_window_size(1920, 1080)

                # 获取截图并保存为 PNG
                output_path = os.path.join(output_folder, f"screenshot_{index}.png")
                screenshot = driver.get_screenshot_as_png()
                with open(output_path, "wb") as file:
                    file.write(screenshot)

                print(f"截图已保存：{output_path}")
            
            except Exception as e:
                print(f"无法截取 {url}：{e}")

# 关闭 WebDriver
driver.quit()
print("所有网址的截图已完成。")
