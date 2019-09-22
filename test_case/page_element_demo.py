from time import sleep

import autoit
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("../chromedriver-v77/chromedriver.exe")

driver.maximize_window()

def input_demo():
    # 查找元素的方法 ： id（选择使用） ,name ,class , tag_name ,xpath(推荐) ,css_selector
    driver.get("http://ui.yansl.com/#/input")
    sleep(2)
    text = driver.find_element_by_name("t1")
    # 清空
    text.clear()
    # 填值
    text.send_keys("hello,word")

def input_demo2():
    driver.get("http://ui.yansl.com/#/input")
    sleep(2)
    text = driver.find_element_by_name("t2")
    # 清空
    text.clear()
    # 填值
    text.send_keys("待会付款133")

def input_demo5():
    driver.get("http://ui.yansl.com/#/input")
    sleep(2)
    text = driver.find_element_by_name("t1")
    # 清空
    text.clear()

    # 填值
    text.send_keys("hello,word")
    sleep(2)
    actions = ActionChains(driver)
    actions.click(text).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).pause(5).send_keys(Keys.BACKSPACE).perform()

    text = driver.find_element_by_name("t2")
    #清空
    text.clear()
    #填值
    text.send_keys("待会付款133")
    sleep(2)
    text = driver.find_element_by_xpath("//textarea[@cols ='40']")
    #清空
    text.clear()
    #填值
    text.send_keys("长安十二时辰")

def rdio_demo1():
    driver.get("http://ui.yansl.com/#/radio")
    sleep(2)
    sex = driver.find_element_by_xpath("//input[@value='0']")
    sex.click()



    check_box = driver.find_element_by_xpath("//input[@value='1']")
    check_box.click()
    sleep(2)

    check_box = driver.find_element_by_xpath("//input[@value='2']")
    check_box.click()
    sleep(2)
    check_box = driver.find_element_by_xpath("//input[@value='3']")
    check_box.click()
    sleep(2)
    if(not check_box.is_selected()):
        check_box.click()

def check_box_demo1():
    driver.get("http://ui.yansl.com/#/checkbox")
    sleep(2)
    check_box = driver.find_element_by_xpath("//input[@value='mysql']/../span")
    check_box.click()
    sleep(2)
    if(not check_box.is_selected()):
        check_box.click()

    attribute = check_box.get_attribute("class")
    print(attribute)


def check_box_demo2():
    driver.get("http://ui.yansl.com/#/checkbox")
    sleep(2)
    check_box = driver.find_element_by_xpath("")
    check_box.click()
    sleep(2)
    # if(not check_box.is_selected()):
    #     check_box.click()
def select_demo1():
    driver.get("http://ui.yansl.com/#/select")
    sleep(2)
    select = driver.find_element_by_xpath("//select/option[3]")
    select.click()




def select_demo():
    driver.get("http://ui.yansl.com/#/select")
    sleep(2)
    select1 = driver.find_element_by_xpath("//input[@name='item2']")
    select1.click()
    sleep(2)
    select2 = driver.find_element_by_xpath("(//span[text()='蚵仔煎'])[last()]")
    select2.click()
    sleep(2)



def select1_demo():
    driver.get("http://ui.yansl.com/#/select")
    sleep(2)
    select1 = driver.find_element_by_xpath("//input[@style='flex-grow: 1; width: 0.108108%; max-width: 175px;']")
    select1.click()
    sleep(2)
    select2 = driver.find_element_by_xpath("(//span[text()='双皮奶'])[last()]")
    select2.click()
    sleep(2)
    select3 = driver.find_element_by_xpath("(//span[text()='蚵仔煎'])[last()]")
    select3.click()

def time_demo():
    driver.get("http://ui.yansl.com/#/dateTime")
    sleep(2)

    times = driver.find_element_by_xpath("//input[@placeholder='任意时间']")
    times.clear()
    sleep(2)
    times.send_keys("16:41:01")




def cascader_demo():
    driver.get("http://ui.yansl.com/#/cascader")
    sleep(2)
    driver.find_element_by_xpath("//label[text()='hover触发']/../div//input").click()
    sleep(2)

    zu_jian = driver.find_element_by_xpath("(//span[text()='组件'])[last()]")
    actions = ActionChains(driver)
    actions.move_to_element(zu_jian).perform()

def uplode_demo():
    driver.get("http://ui.yansl.com/#/upload")
    sleep(2)
    #file = driver.find_element_by_xpath("//(//span[text()='点击上传'])[1]")
    #file.send_keys("D:\\1.png")
    file = driver.find_element_by_xpath("(// span[text() = '点击上传'])[1]")
    file.click()
    autoit.win_wait("打开",10)
    sleep(2)
    # autoit.control_send("打开", "Edit1", os.path.abspath(file_path))
    autoit.control_set_text("打开", "Edit1","D:\\1.png")
    autoit.control_click("打开", "Button1")












if __name__ == '__main__':
    #uplode_demo()
    #time_demo()
    input_demo5()
    #cascader_demo()
    #select1_demo()
    #rdio_demo1()
    sleep(2)
    driver.quit()
