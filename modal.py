from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os

def init():
    # 创建 FirefoxOptions 对象
    firefox_options = webdriver.FirefoxOptions()

    # 创建 FirefoxDriver 实例
    driver = webdriver.Firefox(options=firefox_options)
    
    # 打开网页
    driver.get('https://oc.sjtu.edu.cn/profile/settings')

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

def modal(driver, fo):

    button  = driver.find_element(By.CSS_SELECTOR, '.add_contact_link')
    button.click()
    sleep(3)
    element =driver.find_element(By.CSS_SELECTOR,'.ui-dialog-titlebar-close')
    element.click()
    
    
    
def test_modal():
    fo = open("modal.txt", "w")
    fo.write('上海交通大学Canvas模态框功能测试开始...\n')
    # 获取 driver
    driver = init()
    login(driver, fo)
    modal(driver, fo)
    fo.write('\n所有测试全部通过！\n')
    fo.close()


if __name__ == '__main__':
    test_modal()