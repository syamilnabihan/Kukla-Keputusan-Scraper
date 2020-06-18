from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from time import sleep

PATH = "C:\Program Files\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("http://mrsmkualaklawang.edu.my/e-keputusan/login.asp")


	

#Login method
nk = driver.find_element_by_name("txtId")
nk.send_keys("NK160211")
pw = driver.find_element_by_name("txtPassword")
pw.send_keys("030923101633")
pw.send_keys(Keys.RETURN)
#choosing exam and semester
examspage = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "style8"))
)
exam = Select(driver.find_element_by_id("cboPep"))
exam.select_by_visible_text("Semester(Gred PNG)")
semester = Select(driver.find_element_by_id("cboSem"))
semester.select_by_visible_text("2")
driver.find_element_by_name("Submit").click()
#Results page
Result = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div/table[1]/tbody/tr/td/font[1]/b"))
)
row = 2
for n in range(13):
    row = str(row)
    subject = driver.find_element_by_xpath("/html/body/div/table[4]/tbody/tr["+row+"]/td[1]")
    mark = driver.find_element_by_xpath("/html/body/div/table[4]/tbody/tr["+row+"]/td[4]")
    grade = driver.find_element_by_xpath("/html/body/div/table[4]/tbody/tr["+row+"]/td[5]")
    name = driver.find_element_by_xpath("/html/body/div/table[3]/tbody/tr[1]/td[2]")
    adress1 = driver.find_element_by_xpath("/html/body/div/table[3]/tbody/tr[2]/td[2]")
    adress2 = driver.find_element_by_xpath("/html/body/div/table[3]/tbody/tr[3]/td[2]")
    adress3 = driver.find_element_by_xpath("/html/body/div/table[3]/tbody/tr[4]/td[2]")
    adress4 = driver.find_element_by_xpath("/html/body/div/table[3]/tbody/tr[5]/td[2]")
    row = int(row)
    print(str(row-1)+".",subject.text, mark.text, grade.text)
    row += 1
print(name.text)    
print(
    "png is",
    driver.find_element_by_xpath("/html/body/div/table[4]/tbody/tr[30]/td[4]").text,
    "tpng is",
    driver.find_element_by_xpath("/html/body/div/table[4]/tbody/tr[31]/td[4]").text
    )
print(adress1.text, adress2.text, adress3.text, adress4.text)
driver.quit()

