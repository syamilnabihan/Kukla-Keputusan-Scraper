
"""
Nama,Kelas,Homeroom,BM,BI,SEJ,MM,AM,PHY,CHE,PJ,SIV,PAI,BIO,SENI,SENI
"""
"""
import csv


with open ('mycsv.csv','a+', newline = '') as f:
    fieldnames = ['Nama', 'Kelas','Homeroom','BM','BI','SEJ','MM','AM','PHY','CHE','PJ','SIV',
                   'PAI','BIO']
    thewriter = csv.DictWriter(f, fieldnames = fieldnames)
    
    
    
    
    thewriter.writeheader()
    thewriter.writerow(pngdata)
"""
name = "name"
kelas = "Class"
homeroom = "Homeroom"
for i in range(5):
    print(name,",",kelas,",",homeroom,end=",")
    for i in range(5):
        print(i, end =",")
    print("")
    