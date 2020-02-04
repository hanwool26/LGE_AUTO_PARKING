import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import pause

import macro_config as mc

driver = webdriver.Chrome('/Users/User/PycharmProjects/auto_parking_reservation/chrome_driver/chromedriver')
wait = WebDriverWait(driver, 10)

year, month, date = 0,0,0

def login_page():
    driver.get(mc.main_url)
    time.sleep(1)
    id_elem = wait.until(EC.element_to_be_clickable((By.ID, "username")))
    pass_elem = driver.find_element_by_id("password")

    id_elem.send_keys(mc.my_id)
    pass_elem.send_keys(mc.my_pw)

    login_elem = driver.find_element_by_id("btnSubmit")
    login_elem.click()

def park_page():
    driver.get(mc.park_url)
    time.sleep(1)
    visitor_elem = driver.find_element(By.NAME, "visiterName")
    visitor_elem.send_keys(mc.visitor)

    budilding_elem = Select(driver.find_element_by_name('buildingId'))
    budilding_elem.select_by_visible_text(mc.building)

    phone_elem = driver.find_element(By.NAME, "visiterPhone")
    phone_elem.send_keys(mc.phone_num)

    company_elem = driver.find_element(By.NAME, "visiterCompany")
    company_elem.send_keys(mc.company)

    datepicker = driver.find_element_by_name("startDate")
    datepicker.click()

    selectYear = driver.find_element_by_xpath('//select[@class="ui-datepicker-year"]')
    for option in selectYear.find_elements_by_tag_name('option'):
        if option.text == '2020':
            option.click()
            break

    selectMonth = driver.find_element_by_xpath('//select[@class="ui-datepicker-month"]')
    for option in selectMonth.find_elements_by_tag_name('option'):
        if option.text == '2':
            option.click()
            break

    days = driver.find_elements_by_xpath('//a[@class="ui-state-default"]')
    for i in range(len(days)):
        if days[i].text == '5':
            days[i].click()
            break

    vehicleNum_elem = driver.find_element(By.NAME, "carNo")
    vehicleNum_elem.send_keys(mc.vehicle_num)

    reason_elem = driver.find_element(By.NAME, "parkingComment")
    reason_elem.send_keys(mc.reason)

    save_elem = driver.find_element(By.NAME, "save")
    driver.implicitly_wait(10)

    ActionChains(driver).move_to_element(save_elem).click(save_elem).perform()

def close_driver():
    driver.close()
    driver.quit()

login_page()
driver.implicitly_wait(3)
park_page()
time.sleep(3)
# close_driver()

