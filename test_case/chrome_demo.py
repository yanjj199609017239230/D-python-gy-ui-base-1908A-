from time import sleep

from selenium import webdriver

driver = webdriver.Chrome("../chromedriver-v76/chromedriver.exe")

#关闭浏览器


#sleep(1)

# driver.close()
# driver.quit() #退出的干净

# 调整浏览器窗口的大小
driver.maximize_window()
# 分辨率 不常用
#driver.set_window_size(1600,900)
# 打开网址
driver.get("https://www.taobao.com/")
sleep(1)
driver.get("https://www.jd.com/")
sleep(1)
driver.get("https://www.baidu.com/")

# 后退
driver.back()
sleep(2)


# 前进
driver.forward()
sleep(2)

# 刷新
driver.refresh()
sleep(2)

# 安装pip install selenium
#pip install pytest
#pip install allure-pytest==2.7.0
#pip install pymysql
# pip install autoit-win64



# ActionChains方法列表
#click(on_element=None) ——单击鼠标左键
# click_and_hold(on_element=None) ——点击鼠标左键，不松开
# context_click(on_element=None) ——点击鼠标右键
#
# double_click(on_element=None) ——双击鼠标左键
#
# drag_and_drop(source, target) ——拖拽到某个元素然后松开
#
# drag_and_drop_by_offset(source, xoffset, yoffset) ——拖拽到某个坐标然后松开   drag 拖曳   drop 终止
#
# key_down(value, element=None) ——按下某个键盘上的键
#
# key_up(value, element=None) ——松开某个键    (key up键盘键松开)
#
# move_by_offset(xoffset, yoffset) ——鼠标从当前位置移动到某个坐标
#
# move_to_element(to_element) ——鼠标移动到某个元素
#
# move_to_element_with_offset(to_element, xoffset, yoffset) ——移动到距某个元素（左上角坐标）多少距离的位置
#
# perform() ——执行链中的所有动作
# actions.reset_actions()
#
# release(on_element=None) ——在某个元素位置松开鼠标左键

# send_keys(*keys_to_send) ——发送某个键到当前焦点的元素
#
# send_keys_to_element(element, *keys_to_send) ——发送某个键到指定元素

3.
# ActionChains的其他操作：移动鼠标、右击、双击、结合键盘按键的操作等。。。
#
# context_click(element):
#
# 右击element元素
#
# double_click(element)：
#
# 双击element元素
#
# move_by_offset(xoffset，yoffset)：
#
# 移动鼠标到指定的x，y位置（相对于浏览器的绝对位置）
#
#
#
# move_to_element_with_offset(element, xoffset, yoffset):
#
# 相对element元素, 移动鼠标到指定的x，y位置(相对于element元素的相对位置)
#
# click_and_hold(element1=None)：
#
# 在element1元素上按下鼠标左键，并保持按下动作（元素默认为空）
#
#
#
# release(element2=None):
#
# 在element2元素上松开鼠标左键（元素默认为空）



# key_down(key, element1=None)：
#
# 在element1元素上，按下指定的键盘key（ctrl、shift等）键，并保持按下动作（元素默认为空）
#
#
#
# key_up(key, element2=None)：
#
# 在element2元素上，松开指定的键盘key（元素默认为空）
#
#
#
# send_keys(key):
#
# 向当前定位元素发送某个key键
#
# send_keys_to_element(element ，key)：
#
# 向element元素发送某个key键



