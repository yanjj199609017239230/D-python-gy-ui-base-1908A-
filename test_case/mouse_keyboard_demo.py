from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome("../chromedriver-v77/chromedriver.exe")


driver.maximize_window()

# 滑块
def hua_kuai():
    driver.get("http://ui.yansl.com/#/slider")
    sleep(2)
    silder = driver.find_element_by_xpath("(//label[text()='普通滑块']/../div//div)[last()]")
    actions = ActionChains(driver)
    # actions.drag_and_drop_by_offset(silder,100,0).release().perform()
    actions.click_and_hold(silder).move_by_offset(99,0).release().perform()


    # 竖向
    silder = driver.find_element_by_xpath("(//label[text()='竖向选择']/../div//div)[last()]")
    actions.click_and_hold(silder).move_by_offset(0, -100).release().perform()
if __name__ == '__main__':
    hua_kuai()
    sleep(2)
    driver.quit()




