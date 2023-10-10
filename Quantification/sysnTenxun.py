from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 设置Chrome浏览器驱动器的路径
# chrome_driver_path = '/path/to/chromedriver'

# 创建一个Chrome浏览器对象
# driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver = webdriver.ChromiumEdge()
# driver = webdriver.Chrome(executable_path=r"C:\Users\73699\vuedemo\node_modules\chromedriver\lib\chromedriver\chromedriver.exe")

# 打开腾讯文档网页
url = 'https://docs.qq.com/'
driver.get(url)

# 等待页面加载（你可能需要根据实际情况添加等待时间）
driver.implicitly_wait(10)

# 找到文档输入框，并输入内容
document_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="text"]'))
)
# document_input.send_keys('你的文档链接')
# document_input = driver.find_element(By.CSS_SELECTOR, 'input[type="text"]')
document_input.send_keys('https://docs.qq.com/sheet/DQ0dVaWpFV05SekVr?tab=BB08J2')  # 替换成你的文档链接

# 模拟回车键，进入文档
document_input.send_keys(Keys.RETURN)

# 等待文档页面加载
driver.implicitly_wait(10)

# 找到文档内容输入框，并输入内容
content_input = driver.find_element_by_css_selector('div[contenteditable="true"]')
content_input.send_keys('你要写入的内容')

# 提交内容（你可能需要根据实际情况找到对应的提交按钮并模拟点击）
# content_input.submit()

# 关