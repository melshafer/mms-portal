# File: extract_data.py
# Melanie Shafer, 2015

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

def get_assignment_number(assignment_text):
  for s in assignment_text:
    if s.isdigit():
      return s

current_assignments_num = get_assignment_number(current_assignments)
missing_assignments_num = get_assignment_number(missing_assignments)

def get_current_assignments():
  if current_assignments_num > 0:
    # go to current assignments page
    menu_list[1].find_element_by_tag_name("a").click()
    time.sleep(5)

    table = driver.find_element_by_id("ctl00_ContentPlaceHolder1_GridView1")
    assignments_rows = table.find_element_by_tag_name("tbody").find_elements_by_tag_name("tr")
    assignments_rows.pop(0)

    assignments_list = []
    for assignment_row in assignments_rows:
      columns = assignment_row.find_elements_by_tag_name("td")
      assignment_data = []
      # get rid of class id number, we only need the name
      assignment_data.append(columns[0].text.split("\n")[0])
      assignment_data.append(columns[1].text)
      assignment_data.append(columns[2].text)
      assignment_data.append(columns[4].text)
      assignment_data.append(columns[5].text)
      assignment_data.append(columns[7].text)
      assignments_list.append(assignment_data)

    return assignments_list

assignments_list = get_current_assignments()

#print current_assignments, missing_assignments
driver.quit()
