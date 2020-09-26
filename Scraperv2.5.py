#/usr/bin/python3
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from time import sleep
from Login_dict import trylist as cred


# START
# initialising variables
exams = [None,"Ujian Selaras 1", "Ujian Selaras 2", "Semester(Gred SPM)", "Semester(Gred PNG)",
          "Percubaan SPM"]
semesters = [None,"1", "2", "3", "4"] 
confirmation = False



            
# choosing exams, semester
while confirmation == False:
    examchoice = int(input("Choose exam:\n 1:Ujian Selaras 1\n 2:Ujian Selaras 2\n 3:Semester(Gred SPM)\n 4:Semester(Gred PNG)\n 5:Percubaan SPM \nyour exam choice: "))
    semesterchoice = int(input("\nChoose semester:\n 1:Semester 1\n 2:Semester 2\n 3:Semester 3\n 4:Semester 4\nyour semester choice: "))
    print("\nexam choice is:", exams[(examchoice)], "semester choice is semester:", semesters[(semesterchoice)])
    confirmation = input("\nconfirm y/n ?: ")
    if confirmation == "y" or "Y":
        print("opening browser. . .")
        break
    elif confirmation == "n" or "N":
        confirmation = False
    else:
        print("couldn't quite catch that :/")
        confirmation = False
sleep(2)
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


# Choosing exam and semester on the website
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
        Result = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div/table[1]/tbody/tr/td/font[1]/b")))
    except Exception:
        print("error choosing result")
        pass


# Scraping function for SPM marks or Selaras marks
def resultscrapeSPM():
#     try:
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
    
    iddata = str(name +","+ kelas +","+ homeroom +",")
    #Results scraping
    subject1 = (driver.find_element_by_xpath("/html/body/div/table[4]/tbody/tr[2]/td[1]")).text
    subject2 = (driver.find_element_by_xpath("/html/body/div/table[4]/tbody/tr[3]/td[1]")).text
    subject3 = (driver.find_element_by_xpath("/html/body/div/table[4]/tbody/tr[4]/td[1]")).text
    subject4 = (driver.find_element_by_xpath("/html/body/div/table[4]/tbody/tr[5]/td[1]")).text
    subject5 = (driver.find_element_by_xpath("/html/body/div/table[4]/tbody/tr[6]/td[1]")).text
    subject6 = (driver.find_element_by_xpath("/html/body/div/table[4]/tbody/tr[7]/td[1]")).text
    subject7 = (driver.find_element_by_xpath("/html/body/div/table[4]/tbody/tr[8]/td[1]")).text
    subject8 = (driver.find_element_by_xpath("/html/body/div/table[4]/tbody/tr[9]/td[1]")).text
    subject9 = (driver.find_element_by_xpath("/html/body/div/table[4]/tbody/tr[10]/td[1]")).text
    subject10 = (driver.find_element_by_xpath("/html/body/div/table[4]/tbody/tr[11]/td[1]")).text
        
    mark1 = (driver.find_element_by_xpath("/html/body/div/table[4]/tbody/tr[2]/td[3]")).text
    mark2 = (driver.find_element_by_xpath("/html/body/div/table[4]/tbody/tr[3]/td[3]")).text
    mark3 = (driver.find_element_by_xpath("/html/body/div/table[4]/tbody/tr[4]/td[3]")).text
    mark4 = (driver.find_element_by_xpath("/html/body/div/table[4]/tbody/tr[5]/td[3]")).text
    mark5 = (driver.find_element_by_xpath("/html/body/div/table[4]/tbody/tr[6]/td[3]")).text
    mark6 = (driver.find_element_by_xpath("/html/body/div/table[4]/tbody/tr[7]/td[3]")).text
    mark7 = (driver.find_element_by_xpath("/html/body/div/table[4]/tbody/tr[8]/td[3]")).text
    mark8 = (driver.find_element_by_xpath("/html/body/div/table[4]/tbody/tr[9]/td[3]")).text
    mark9 = (driver.find_element_by_xpath("/html/body/div/table[4]/tbody/tr[10]/td[3]")).text
    mark10 = (driver.find_element_by_xpath("/html/body/div/table[4]/tbody/tr[11]/td[3]")).text
    
    grade1 = (driver.find_element_by_xpath("/html/body/div/table[4]/tbody/tr[2]/td[4]")).text
    grade2 = (driver.find_element_by_xpath("/html/body/div/table[4]/tbody/tr[3]/td[4]")).text
    grade3 = (driver.find_element_by_xpath("/html/body/div/table[4]/tbody/tr[4]/td[4]")).text
    grade4 = (driver.find_element_by_xpath("/html/body/div/table[4]/tbody/tr[5]/td[4]")).text
    grade5 = (driver.find_element_by_xpath("/html/body/div/table[4]/tbody/tr[6]/td[4]")).text
    grade6 = (driver.find_element_by_xpath("/html/body/div/table[4]/tbody/tr[7]/td[4]")).text
    grade7 = (driver.find_element_by_xpath("/html/body/div/table[4]/tbody/tr[8]/td[4]")).text
    grade8 = (driver.find_element_by_xpath("/html/body/div/table[4]/tbody/tr[9]/td[4]")).text
    grade9 = (driver.find_element_by_xpath("/html/body/div/table[4]/tbody/tr[10]/td[4]")).text
    grade10 = (driver.find_element_by_xpath("/html/body/div/table[4]/tbody/tr[11]/td[4]")).text
    
    with open ('test.csv','a+', newline = '') as f:
        fieldnames = ['Nama', 'Kelas','Homeroom','  Bahasa Melayu','  Bahasa Inggeris','  Sejarah','  Mathematics',
                        '  Additional Mathematics','  Physics','  Chemistry','  Pendidikan Agama Islam','  Biology',
                        '  Prinsip Akaun','  Pendidikan Seni Visual']
        thewriter = csv.DictWriter(f, fieldnames = fieldnames, extrasaction='ignore')    
        thewriter.writerow({'Nama': name,
                        'Kelas': kelas,
                        'Homeroom': homeroom,
                        subject1 : mark1,
                        subject2 : mark2,
                        subject3 : mark3,
                        subject4 : mark4,
                        subject5 : mark5,
                        subject6 : mark6,
                        subject7 : mark7,
                        subject8 : mark8,
                        subject9 : mark9,
                        subject10 : mark10,
                                
                    })
    driver.back()
    driver.back()
#    except:
#        pass


# Scraping function for PNG marks
def resultscrapePNG():
    pass

# Clearing the login box
def empty():
    nk = driver.find_element_by_name("txtId")
    nk.clear()
    pw = driver.find_element_by_name("txtPassword")
    pw.clear()


def program():
    
    # examchoice 4 is for PNG values
    if examchoice == 4:
        for key,value in cred.items():
            login()
            choosingresult(key,value)
            resultscrapePNG()
            empty()
        # examchoice other than 4 uses SPM values
    elif examchoice == 1 or 2 or 3 or 5:
        with open ('test.csv','w', newline = '') as f:
            fieldnames = ['Nama', 'Kelas','Homeroom','  Bahasa Melayu','  Bahasa Inggeris','  Sejarah','  Mathematics',
                  '  Additional Mathematics','  Physics','  Chemistry','  Pendidikan Agama Islam','  Biology',
                  '  Prinsip Akaun','  Pendidikan Seni Visual']
            thewriter = csv.DictWriter(f, fieldnames = fieldnames, extrasaction='ignore')
            thewriter.writeheader()
        for key,value in cred.items():
            login(key,value)
            choosingresult()
            resultscrapeSPM()
            empty()
        
    
program()
print("--Finished")            
driver.quit()