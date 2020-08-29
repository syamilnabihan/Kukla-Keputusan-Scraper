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

PATH = "C:\Program Files\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("http://mrsmkualaklawang.edu.my/e-keputusan/login.asp")

"""
with open ('targetgroup.csv','a+', newline = '') as f:
            fieldnames = ['Nama', 'Kelas','Homeroom','BM','BI','SEJ','MM','AM','PHY','CHE','PJ','SIV',
                          'PAI','BIO','SENI','SENI',]
thewriter = csv.DictWriter(f, fieldnames = fieldnames)
thewriter.writeheader()
"""
# matrixnum = ""
# icnum = ""

#choose index here for choosingresult()
# exams and semesters both uses visible text locator
exams = ["Ujian Selaras 1", "Ujian Selaras 2", "Semester(Gred SPM)", "Semester(Gred PNG)",
          "Percubaan SPM"]
semesters = ["1", "2", "3", "4"]



def login(matrixnumber, icnumber):

    nk = driver.find_element_by_name("txtId")
    nk.send_keys(matrixnumber)
    pw = driver.find_element_by_name("txtPassword")
    pw.send_keys(icnumber)
    pw.send_keys(Keys.RETURN)
    examspage = WebDriverWait(driver, 2).until(
    EC.presence_of_element_located((By.CLASS_NAME, "style8")))
  

def empty():
     nk = driver.find_element_by_name("txtId")
     nk.clear()
     pw = driver.find_element_by_name("txtPassword")
     

def choosingresult():
    try:
        examspage = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.CLASS_NAME, "style8")))
        exam = Select(driver.find_element_by_id("cboPep"))
        exam.select_by_visible_text((exams[2]))
        semester = Select(driver.find_element_by_id("cboSem"))
        semester.select_by_visible_text((semesters[2]))
        driver.find_element_by_name("Submit").click()
        # wait for result page to load
        Result = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div/table[1]/tbody/tr/td/font[1]/b")))
    except Exception:
        pass


def resultscrape():
#    try:
        namepos = driver.find_element_by_xpath("/html/body/div/table[3]/tbody/tr[1]/td[2]")
        name = namepos.text
        address1pos = driver.find_element_by_xpath("/html/body/div/table[3]/tbody/tr[2]/td[2]")
        address2pos = driver.find_element_by_xpath("/html/body/div/table[3]/tbody/tr[3]/td[2]")
        address3pos = driver.find_element_by_xpath("/html/body/div/table[3]/tbody/tr[4]/td[2]")
        address4pos = driver.find_element_by_xpath("/html/body/div/table[3]/tbody/tr[5]/td[2]")
        addressfull = (address1pos.text+address2pos.text+address3pos.text+address4pos.text)
        homeroompos = driver.find_element_by_xpath("/html/body/div/table[3]/tbody/tr[3]/td[4]")
        homeroom = homeroompos.text
        kelaspos = driver.find_element_by_xpath("/html/body/div/table[3]/tbody/tr[4]/td[4]")
        kelas = kelaspos.text
        # pngpos = driver.find_element_by_xpath("/html/body/div/table[4]/tbody/tr[30]/td[4]")
        # png = pngpos.text
        #Initialise csv file
        
        pngdata = str(name +","+ kelas +","+ homeroom +",")
        print(pngdata, end=",")
        #Results scraping
        row = 2
        for n in range(14):
            row = str(row)
            subject = driver.find_element_by_xpath("/html/body/div/table[4]/tbody/tr["+row+"]/td[1]")
            # for mark,if exam is png use td4(grade is td5),if spm use td3(td4 is grade)
            mark = driver.find_element_by_xpath("/html/body/div/table[4]/tbody/tr["+row+"]/td[3]")
            grade = driver.find_element_by_xpath("/html/body/div/table[4]/tbody/tr["+row+"]/td[4]")
            
            row = int(row)
        #    print(str(row-1)+".",subject.text, mark.text, grade.text)
            print(subject.text,mark.text, end =",")
        
        #   thewriter.writerow({'Nama':name,})
            row += 1
#    except:
#        pass
        

def Program():
    
    for key,value in cred.items():
        login(key, value)
        choosingresult()
        resultscrape()
        driver.back()
        driver.back()
        empty()
              
                
Program()
driver.quit()