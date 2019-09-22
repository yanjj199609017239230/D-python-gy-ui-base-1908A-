from time import sleep

from selenium import webdriver


driver = webdriver.Chrome("../chromedriver-v77/chromedriver.exe")

driver.maximize_window()

# sleep 解决网络和页面加载的等待时间,强制暂时终止执行

def scroll_windows():
    driver.get("https://www.baidu.com/")  # 获取网址
    sleep(2)
    i = driver.find_element_by_id('kw')     # 定位百度搜索输入框
    i.clear()
    i.send_keys("华为")                     # 输入内容
    sleep(2)
    driver.find_element_by_id('su').click() # 定位'百度一下'按钮并点击
    sleep(5)

    #滚动到页面底部
    # js = "var q=document.documentElement.scrollTop=10000"  # g向下滚动像素
    #
    # driver.execute_script(js)
    # sleep(5)



    # 滚动到指定元素出现
    target = driver.find_element_by_xpath('''(//h3/a/em)[8]''')

    driver.execute_script("arguments[0].scrollIntoView();", target)
    sleep(2)



if __name__ == '__main__':
    scroll_windows()
    driver.quit()
