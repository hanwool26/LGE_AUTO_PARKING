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
import os

main_url = 'https://sso.lgsp.co.kr/ikep4sp-sso/loginForm.do'
park_url = "https://portal.lgsp.co.kr:6223/ikep4-webapp/lightpack/parking/parkingCreate.do?parkType=G"
chrome_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'chromedriver')

class WebDriver:
    def __init__(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.wait = WebDriverWait(self.driver, 10)

    def login_page(self, my_id, my_pw):
        self.driver.get(main_url)
        time.sleep(1)
        id_elem = self.wait.until(EC.element_to_be_clickable((By.ID, "username")))
        pass_elem = self.driver.find_element_by_id("password")

        id_elem.send_keys(my_id)
        pass_elem.send_keys(my_pw)

        login_elem = self.driver.find_element_by_id("btnSubmit")
        login_elem.click()

    def park_page(self, visitor, building, date, phone_num, company, vehicle_num, reason):
        self.driver.get(park_url)
        time.sleep(1)
        visitor_elem = self.driver.find_element(By.NAME, "visiterName")
        visitor_elem.send_keys(visitor)

        budilding_elem = Select(self.driver.find_element_by_name('buildingId'))
        budilding_elem.select_by_visible_text(building)

        phone_elem = self.driver.find_element(By.NAME, "visiterPhone")
        phone_elem.send_keys(phone_num)

        company_elem = self.driver.find_element(By.NAME, "visiterCompany")
        company_elem.send_keys(company)

        datepicker = self.driver.find_element_by_name("startDate")
        datepicker.click()

        park_year = date[0]
        park_month = date[1]
        park_date = date[2]

        selectYear = self.driver.find_element_by_xpath('//select[@class="ui-datepicker-year"]')
        for option in selectYear.find_elements_by_tag_name('option'):
            if option.text == park_year:
                option.click()
                break

        selectMonth = self.driver.find_element_by_xpath('//select[@class="ui-datepicker-month"]')
        for option in selectMonth.find_elements_by_tag_name('option'):
            if option.text == park_month:
                option.click()
                break

        days = self.driver.find_elements_by_xpath('//a[@class="ui-state-default"]')
        for i in range(len(days)):
            if days[i].text == park_date:
                days[i].click()
                break

        vehicleNum_elem = self.driver.find_element(By.NAME, "carNo")
        vehicleNum_elem.send_keys(vehicle_num)

        reason_elem = self.driver.find_element(By.NAME, "parkingComment")
        reason_elem.send_keys(reason)

        save_elem = self.driver.find_element(By.NAME, "save")
        self.driver.implicitly_wait(10)
        ActionChains(self.driver).move_to_element(save_elem).click(save_elem).perform()

    def close_driver(self):
        self.driver.quit()