from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait  #显示等待01
from selenium.webdriver.support import expected_conditions as EC  #显示等待02
driver = webdriver.Chrome("../chromedriver-v77/chromedriver.exe")

driver.maximize_window()

driver.implicitly_wait(10) #隐式等待 10秒

def iframe_demo():
    # 打开网址
    driver.get("http://www.guoyasoft.com:8080/guoya-client/jsp/user/login.jsp")
    #sleep(2)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'userName')))  # 显示等待 这里只能放一个元素进去，元组或者列表

    #定位用户名输入框。输入用户名
    username = driver.find_element_by_id("userName")
    username.clear()
    username.send_keys("xuepl")


    #定位密码输入框。输入密码
    password = driver.find_element_by_id("password")
    password.clear()
    password.send_keys("123456")

    #定位登录按钮，点击
    driver.find_element_by_id("loginBtn").click()
    sleep(5)


    #定位面试查询连接，点击
    driver.find_element_by_xpath("//a[text()='面试查询']").click()
    sleep(5)

    #切换至iframe
    iframe = driver.find_element_by_id("iframepage")
    driver.switch_to.frame(iframe)

    #定位查询按钮，并点击
    driver.find_element_by_xpath("//button[text()='查询']").click()
    sleep(10)
    #退出当前iframe
    driver.switch_to.parent_frame()

    # 返回最外层页面
    #driver.switch_to.default_content()

    # 定位检查作业,并点击
    driver.find_element_by_xpath("//a[text()='作业检查1811A']").click()
    sleep(5)

# 超链接文本打开网页
def chao_lian_demo():
    driver.get("C:\\Users\\Administrator\\Desktop\\demo.html")
    sleep(2)
    text = driver.find_element_by_xpath("//a[text()='问问度娘']")
    # bai_du = driver.find_element_by_partial_link_text("度娘")
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL).click(text).key_up(Keys.CONTROL).perform()
    # ctrl 按下连接文本打开的组合
    actions.reset_actions()  # 重置
    sleep(2)


    dang_dang = driver.find_element_by_partial_link_text("当当")
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL).click(dang_dang).key_up(Keys.CONTROL).perform()
    actions.reset_actions()
    sleep(2)

    jd = driver.find_element_by_partial_link_text("京东")
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL).click(jd).key_up(Keys.CONTROL).perform()
    actions.reset_actions()
    sleep(2)

    # 窗口句柄  每个窗口就是一个句柄一个字符串，拿到句柄完成窗口切换
    handles = driver.window_handles  # 拿到句柄
    for b in handles:               # 循环 打开切换到各窗口
        driver.switch_to.window(b)
        sleep(2)
        if(driver.title.__contains__("当当")):  # 切换到当当停止
            break


















if __name__ == '__main__':
    chao_lian_demo()
    #iframe_demo()
    sleep(2)
    driver.quit()
