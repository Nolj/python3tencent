"""使用seleium打开京东首页，搜索商品phone
    得到商品列表信息
    图片
    价格
    描述
    商店
    评价条数
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # 引入显式等待
from selenium.webdriver.support import expected_conditions as EC  # 期待条件 别名
from selenium.common.exceptions import TimeoutException  # 导入超时异常
from lxml import etree

# 声明浏览器对象
browser = webdriver.Chrome()
# 显式等待
wait = WebDriverWait(browser, 10)
keyword = "phone"
url = "https://www.jd.com/"

# 获取页面


def get_page():
    # 异常处理
    try:
        # 访问页面
        browser.get(url)
        # 得到搜索框与按纽
        input = wait.until(EC.presence_of_element_located((By.ID, "key")))
        button = wait.until(EC.element_to_be_clickable(
            
            (By.XPATH, "//*[@id='search']//button")))
        # 初始化输入框
        input.clear()
        input.send_keys(keyword)
        button.click()
        #如果商品列表加载完成则调用
        wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="J_goodsList"]/ul/li')))
        get_goods()
    except TimeoutException:
        print("请求超时")
        get_page()

# 解析页面


def get_goods():
    #得到源码
    html = browser.page_source
    #解析
    response = etree.HTML(html)
    data = {}
    for li in response.xpath('//*[@id="J_goodsList"]/ul/li'):
        data["dsc"] = li.xpath("string(./div/div[4]/a/em)")
        print(data)

if __name__ == "__main__":
    get_page()
