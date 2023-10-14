from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import time



chromedriver = "C:\soft\driver\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
option = webdriver.ChromeOptions()
chrome_options = Options()
# chrome_options.add_argument('--headless')

driver = webdriver.Chrome(options=chrome_options)
#
# driver.set_page_load_timeout(3)
#
#
# driver.get('https://quote.eastmoney.com/concept/sz000413.html')

# 将页面滚动到底部
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# time.sleep(1)
# # 设置浏览器宽度和高度
# width = driver.execute_script(
#   "return document.documentElement.scrollWidth"
# )
# height = driver.execute_script(
#   "return document.documentElement.scrollHeight"
# )
# driver.set_window_size(width, height)
# time.sleep(1)
#main_time_chart > div > div.quotechart2022_c_pkyd
# specific_section = driver.find_element(By.CLASS_NAME, '//*[@id="main_time_chart"]/div/div[2]/quotechart2022_c_pk')

# screenshot_path = "screenshot1.png"  # 保存截图的文件路径
# driver.save_screenshot(screenshot_path)



# 打开百度网站

driver.get("https://www.baidu.com")

# 定位搜索框元素
search_box = driver.find_element(By.ID,"s_lg_img")  # 这里假设搜索框的id为"kw"

# 获取搜索框的位置和大小
location = search_box.location
size = search_box.size

# 执行JavaScript代码，隐藏页面上的其他元素，只显示搜索框位置的内容
js_code = f'''
var elements = document.body.children;
for (var i = 0; i < elements.length; i++) {{
    if (elements[i] !== arguments[0]) {{
        elements[i].style.display = 'none';
    }}
}}
'''
driver.execute_script(js_code, search_box)

# 保持窗口打开
input("Press Enter to close the browser...")

# 关闭浏览器驱动器
driver.quit()

# print(f"成功截取网页固定区域并保存为：{screenshot_path}")