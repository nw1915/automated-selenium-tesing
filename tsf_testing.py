from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time


PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.thesparksfoundationsingapore.org")
print(driver.title)

time.sleep(10)


print("\nCase 1: Logo Verification\n")
try:
    driver.find_element_by_xpath("//img[@src='/images/logo_small.png']")
    time.sleep(3)
    print("Result: Logo exists\n")
except NoSuchElementException:
    print("Result: Logo Does Not Exist\n")
print("="*55)

print("Case 2: Navigation Bar Appearance\n")
try:
    driver.find_element_by_id("link-effect-3")
    time.sleep(3)
    print("Result: Navigation Bar Appears\n")
except NoSuchElementException:
    print("Result: Navigation Bar Does Not Appear\n")
print("="*55)

print("Case 3: Expert Mentors Page Content Verification\n")
try:
    driver.find_element_by_link_text("About Us").click()
    time.sleep(3)
    driver.find_element_by_link_text("Expert Mentors").click()
    time.sleep(3)
    driver.find_element_by_tag_name('h3')
    print("Result: Expert Mentors Page Is Undone\n")

except NoSuchElementException:
    print("Result: Expert Mentors Page Is Done\n")
print("="*55)

print("Case 4: Workshops Page Verification\n")
try:
    driver.find_element_by_link_text("Programs").click()
    time.sleep(3)
    driver.find_element_by_link_text("Workshops").click()
    time.sleep(3)
    print("Result: Workshops Page Exists\n")

except NoSuchElementException:
    print("Result: Workshops Page Does Not Exist\n")
print("="*55)

print("Case 5: LINKS App Page Verification\n")
try:
    driver.find_element_by_link_text("LINKS App").click()
    time.sleep(3)
    print("Result: LINKS App Page Exists\n")

except NoSuchElementException:
    print("Result: LINKS App Page Does Not Exist\n")
time.sleep(3)
print("="*55)


print("Case 6: Map Authentication\n")
try:
    driver.find_element_by_link_text("Contact Us").click()
    time.sleep(3)
    driver.find_element_by_class_name("map-agileits")
    time.sleep(6)
    print("Result: Map Exists\n")

except NoSuchElementException:
    print("Result: Map Does Not Exist\n")
print("="*55)


print("Case 7: Student Externships Program Verification\n")
try:
    driver.find_element_by_link_text("Student Externships Program").click()
    time.sleep(3)
    driver.find_element_by_tag_name('h3')
    time.sleep(3)
    print("Result: Student Externships Page Is Undone\n")

except NoSuchElementException:
    print("Result: Student Externships Page Is Done\n")
print("="*55)

print("Case 8: Facebook Widget Authemtication\n")
try:
    driver.find_element_by_link_text("About Us").click()
    time.sleep(3)
    driver.find_element_by_link_text("News").click()
    time.sleep(3)
    driver.find_element_by_class_name('fb-page')
    time.sleep(5)
    print("Result: Facebook Widget Exists\n")


except NoSuchElementException:
    print("Result: Facebook Widget Does Not Exist")
print("="*55)

print("Case 9: Copyright Notice Appearance\n")
try:
    driver.find_element_by_class_name('copyright-wthree')
    time.sleep(3)
    print("Result: Copyright Notice Appears\n")

except NoSuchElementException:
    print("Result: Copyright Notice Does Not Appear\n")
print("="*55)


print("Case 10: Visit Now Button Functioning\n")
try:
    driver.find_element_by_xpath("//img[@src='/images/logo_small.png']").click()
    time.sleep(3)
    driver.find_element_by_link_text("VISIT NOW").click()
    time.sleep(5)
    print("Result: Visit Now Button Is Working\n")

except NoSuchElementException:
    print("Result: Visit Now Button Is Not Working\n")
print("="*55)

time.sleep(3)
driver.quit()
