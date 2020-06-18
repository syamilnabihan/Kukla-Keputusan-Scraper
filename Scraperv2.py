#/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from time import sleep
from textprogram import Loginlist as cred

PATH = "C:\Program Files\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("http://mrsmkualaklawang.edu.my/e-keputusan/login.asp")

# matrixnum = ""
# icnum = ""

#choose index here for choosingresult()
# exams and semesters both uses visible text locator
exams = ["Ujian Selaras 1", "Ujian Selaras 2", "Semester(Gred SPM)", "Semester(Gred PNG)", "Percubaan SPM"]
semesters = ["1", "2", "3", "4"]

def login(matrixnumber, icnumber):
    try:
        nk = driver.find_element_by_name("txtId")
        nk.send_keys(matrixnumber)
        pw = driver.find_element_by_name("txtPassword")
        pw.send_keys(icnumber)
        pw.send_keys(Keys.RETURN)
        examspage = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.CLASS_NAME, "style8")))
    except Exception:
        driver.back()
        pass


def empty():
     nk = driver.find_element_by_name("txtId")
     nk.clear()
     pw = driver.find_element_by_name("txtPassword")

def choosingresult():
    try:
        examspage = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.CLASS_NAME, "style8")))
        exam = Select(driver.find_element_by_id("cboPep"))
        exam.select_by_visible_text((exams[3]))
        semester = Select(driver.find_element_by_id("cboSem"))
        semester.select_by_visible_text((semesters[1]))
        driver.find_element_by_name("Submit").click()
        # wait for result page to load
        Result = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div/table[1]/tbody/tr/td/font[1]/b")))
    except Exception:
        pass

def resultscrape():
    try:
        name = driver.find_element_by_xpath("/html/body/div/table[3]/tbody/tr[1]/td[2]")
        print(
            name.text,
            "png is",
            driver.find_element_by_xpath("/html/body/div/table[4]/tbody/tr[30]/td[4]").text,
            "tpng is",
            driver.find_element_by_xpath("/html/body/div/table[4]/tbody/tr[31]/td[4]").text
            )
        row = 2
        for n in range(14):
            row = str(row)
            subject = driver.find_element_by_xpath("/html/body/div/table[4]/tbody/tr["+row+"]/td[1]")
            mark = driver.find_element_by_xpath("/html/body/div/table[4]/tbody/tr["+row+"]/td[4]")
            grade = driver.find_element_by_xpath("/html/body/div/table[4]/tbody/tr["+row+"]/td[5]")
            name = driver.find_element_by_xpath("/html/body/div/table[3]/tbody/tr[1]/td[2]")
            address1 = driver.find_element_by_xpath("/html/body/div/table[3]/tbody/tr[2]/td[2]")
            address2 = driver.find_element_by_xpath("/html/body/div/table[3]/tbody/tr[3]/td[2]")
            address3 = driver.find_element_by_xpath("/html/body/div/table[3]/tbody/tr[4]/td[2]")
            address4 = driver.find_element_by_xpath("/html/body/div/table[3]/tbody/tr[5]/td[2]")
            addressfull = (address1.text+address2.text+address3.text+address4.text)
            row = int(row)
            print(str(row-1)+".",subject.text, mark.text, grade.text)
            row += 1
    except Exception:
        pass

for key,value in cred.items():
    login(key, value)
    choosingresult()
    resultscrape()
    driver.back()
    driver.back()
    empty()
