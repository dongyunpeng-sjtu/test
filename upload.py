from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pywinauto
from pywinauto.keyboard import send_keys
from selenium.common.exceptions import NoSuchElementException
import os

def init():
    # 创建 FirefoxOptions 对象
    firefox_options = webdriver.FirefoxOptions()

    # 创建 FirefoxDriver 实例
    driver = webdriver.Firefox(options=firefox_options)
    
    # 打开网页
    driver.get('https://oc.sjtu.edu.cn/files')

    return driver

# ---- 以下为登录代码 ----
def useJaccount(driver, fo):
    inputBox_id = driver.find_element(By.ID, 'jaccount')
    inputBox_css = driver.find_element(By.CSS_SELECTOR, '#jaccount')
    inputBox_xpath = driver.find_element(By.XPATH, '//*[@id="jaccount"]')
    
    assert inputBox_id == inputBox_css
    assert inputBox_id == inputBox_xpath
    
    # 跳转到jaccount登录
    inputBox_id.click()
    
def get_input_box(driver, fo):
    inputBox_id = driver.find_element_by_id('user')
    pwdBox_id = driver.find_element(By.ID, 'pass')

    user = ''
    pwd = ''

    inputBox_id.send_keys(user)
    inputBox_id.send_keys(Keys.ENTER)
    pwdBox_id.send_keys(pwd)
    pwdBox_id.send_keys(Keys.ENTER)
    sleep(5)
    return inputBox_id


def test_login_button(driver, fo):
    searchButton_xpath = driver.find_element(By.XPATH, '//*[@id="submit-button"]')
    searchButton_id = driver.find_element(By.ID, 'submit-button')
    searchButton_id.click()
    return searchButton_xpath


def login(driver, fo):
    useJaccount(driver, fo)
    get_input_box(driver, fo)
    test_login_button(driver, fo)
    
# ---- 以上为登录代码 ----    


def upload(driver, fo):
    element = driver.find_element(By.CSS_SELECTOR, 'button.btn:nth-child(2)')
    element.click()
    sleep(3)

    # 使用pywinauto来选择文件
    app = pywinauto.Desktop()
    # 选择文件上传的窗口
    fo.write('打开文件上传窗口准备上传文件\n')
    dlg = app["文件上传"]

    # 选择文件地址输入框，点击激活
    dlg["Toolbar3"].click()
    # 键盘输入上传文件的路径
    send_keys("D:/")
    # 键盘输入回车，打开该路径
    send_keys("{VK_RETURN}")

    # 选中文件名输入框，输入文件名
    dlg["文件名(&N):Edit"].type_keys("config")

    # 点击打开
    dlg["打开(&O)"].click()

    # 判断文件是否存在
    if not os.path.exists("D:/config"):
        fo.write('上传文件失败！\n')
        assert False

    # 输出上传文件成功的信息
    fo.write('上传文件成功！\n')
    
    
    
def test_upload():
    fo = open("upload.txt", "w")
    fo.write('上海交通大学Canvas上传功能测试开始...\n')
    # 获取 driver
    driver = init()
    login(driver, fo)
    upload(driver, fo)
    fo.write('\n所有测试全部通过！\n')
    fo.close()


if __name__ == '__main__':
    test_upload()