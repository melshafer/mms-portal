import config
import time
from selenium import webdriver

driver = webdriver.PhantomJS()
#driver = webdriver.Firefox()
driver.set_window_size(1120, 550)

driver.get(config.mms_url)

driver.find_element_by_id("LoginControl1_txtUsername").send_keys(config.mms_username)
driver.find_element_by_id("LoginControl1_txtPassword").send_keys(config.mms_password)

driver.find_element_by_id("LoginControl1_btnLogin").click()
time.sleep(3)

# logged in
links = driver.find_element_by_class_name("maincontent").find_elements_by_tag_name("a")
links[1].click()
time.sleep(3)

menu = driver.find_element_by_id("ctl00_MMS_Menu1_MMSMenu3").find_element_by_tag_name("ul")
menu_list = menu.find_elements_by_tag_name("li")

current_assignments = menu_list[1].text
missing_assignments = menu_list[2].text

#print current_assignments, missing_assignments
driver.quit()
