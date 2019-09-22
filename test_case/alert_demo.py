from time import sleep

from selenium import webdriver

driver = webdriver.Chrome("../chromedriver-v76/chromedriver.exe")

driver.maximize_window()

def alert_demo():
    driver.get("C:\\Users\\Administrator\\Desktop\\demo.html")
    sleep(2)
    driver.find_element_by_xpath("//input[@type='reset']").click()
    sleep(2)
    al = driver.switch_to.alert
    al.accept()

def prompt_demo():
    driver.get("C:\\Users\\Administrator\\Desktop\\demo.html")
    sleep(2)
    driver.find_element_by_xpath("//input[@type='button']").click()
    alb = driver.switch_to.alert
    alb.send_keys("hello,word")
    sleep(2)
    alb.accept()


def submit_demo():
    driver.get("C:\\Users\\Administrator\\Desktop\\demo.html")
    sleep(2)
    driver.find_element_by_xpath("//input[@type='submit']").click()
    alc = driver.switch_to.alert
    sleep(2)
    alc.accept()






if __name__ == '__main__':
    submit_demo()
    #prompt_demo()
    #alert_demo()
    sleep(2)
    driver.quit()


