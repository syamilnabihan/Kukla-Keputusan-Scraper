import csv


with open ('mycsv.csv','w', newline = '') as f:
    fieldnames = ['Nama', 'Kelas','Homeroom','BM','BI','SEJ','MM','AM','PHY','CHE','PJ','SIV',
                   'PAI','BIO']
    thewriter = csv.DictWriter(f, fieldnames = fieldnames)
    
    
    
    
    thewriter.writeheader()
    for key in cred():
        thewriter.writerow({'Nama': name, 'Kelas': kelas,'Homeroom': homeroom,'BM':mark,'BI',
                            'SEJ','MM','AM','PHY','CHE','PJ','SIV','PAI','BIO'})