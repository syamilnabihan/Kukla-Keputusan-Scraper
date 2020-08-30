#/usr/bin/python3
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from time import sleep
from textprogram import targetlist as cred


# START
# initialising variables
exams = [None,"Ujian Selaras 1", "Ujian Selaras 2", "Semester(Gred SPM)", "Semester(Gred PNG)",
          "Percubaan SPM"]
semesters = [None,"1", "2", "3", "4"] 
confirmation = False

# choosing exams, semester
while confirmation == False:
    examchoice = int(input("Choose exam:\n 1:Ujian Selaras 1\n 2:Ujian Selaras 2\n 3:Semester(Gred SPM)\n 4:Semester(Gred PNG)\n 5:Percubaan SPM \nyour exam choice: "))
    semesterchoice = int(input("Choose semester:\n 1:Semester 1\n 2:Semester 2\n 3:Semester 3\n 4:Semester 4\nyour semester choice: "))
    print("exam choice is:", exams[(examchoice)], "semester choice is semester:", semesters[(semesterchoice)])
    confirmation = input("confirm: y/n ?")
    if confirmation == "y":
        print("opening browser...")
        break
    elif confirmation == "n":
        confirmation = False
    else:
        print("couldn't quite catch that :/")
        confirmation = False


PATH = "C:\Program Files\chromedriver.exe"
driver = webdriver.Chrome(PATH)
# getting to e-semakan
driver.get("http://mrsmkualaklawang.edu.my/e-keputusan/login.asp")

#Login method
def login(matrixnumber, icnumber): 
    nk = driver.find_element_by_name("txtId")
    nk.send_keys(matrixnumber)
    pw = driver.find_element_by_name("txtPassword")
    pw.send_keys(icnumber)
    pw.send_keys(Keys.RETURN)
    examspage = WebDriverWait(driver, 2).until(
    EC.presence_of_element_located((By.CLASS_NAME, "style8")))
  
  
#Choosing exam and semester
def choosingresult():
    try:
        examspage = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.CLASS_NAME, "style8")))
        exam = Select(driver.find_element_by_id("cboPep"))
        exam.select_by_visible_text((exams[(examchoice)]))
        semester = Select(driver.find_element_by_id("cboSem"))
        semester.select_by_visible_text((semesters[(semesterchoice)]))
        driver.find_element_by_name("Submit").click()
        # wait for result page to load
        Result = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div/table[1]/tbody/tr/td/font[1]/b")))
    except Exception:
        pass


driver.quit()