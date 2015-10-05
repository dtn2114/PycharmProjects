__author__ = 'bill'

from selenium import webdriver
# import selenium
from selenium.webdriver.common.keys import Keys
import os
import time

if __name__ == '__main__':
    chromedriver = '/Users/bill/PycharmProjects/BeauSoupTest/chromedriver'
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)
    driver.get("http://brokercheck.finra.org/Individual/Summary/1259603")
    # assert "Finra" in driver.title

    # print driver.title
    # elem = driver.find_element_by_xpath("//div[@class='bcpanel-body align-center']//a")
    # print elem
    elem = driver.find_element_by_xpath("//div[div[input[@type = 'submit' and @id = "
                                        "'ctl00_phContent_TermsAndCondUC_BtnAccept']]]//input")
    # print elem.get_attribute("value")
    driver.execute_script("$(arguments[0]).click();", elem )
    # driver.execute_script("document.getElementById('1588737').style.display='table-row';")
    elem = driver.find_element_by_xpath("//tr[@id = '1588737']/preceding-sibling::tr[td[div[span[@id = "
                                        "'minus']]]]//span")
    # elem.click()elem
    driver.execute_script("$(arguments[0]).click();", elem )


    # elem = driver.find_element_by_id("document.tr['1588737'].disclosureInnerTable")

    # print elem
    # elem = driver.find_element_by_xpath("//tr[@id = '1588737']")
    # elem.send_keys(1)
    # print driver.execute_script("return arguments[0].innerHTML", elem)
    # print driver.execute_script("return arguments[0].textContent", elem)
    # print elem.get_attribute('innerHTML')
    # html = driver.page_source
    # print html
    # elem.send_keys(Keys.RETURN)
    # elem.send_keys(Keys.ENTER)
    # driver.click("xpath=//div[div[input[@type = 'submit' and @name = 'ctl00$phContent$TermsAndCondUC$BtnAccept']]]")
    # time.sleep(1)

    # elem = driver.find_element_by_name("q")
    # elem.send_keys("pycon")
    # elem.send_keys(Keys.RETURN)
    # assert "No results found." not in driver.page_source
    driver.close()

