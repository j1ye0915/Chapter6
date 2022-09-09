import csv
from unicodedata import name


infile = open('customers.csv','r')

csvfile1 = csv.reader(infile,delimiter=',')


data_list = []
for record in csvfile1:
    a = record[1] + " " + record[2],record[4]
    data_list.append(a)

data_list.pop(0)


header_list = ["FullName","Country"]

with open("customer_country.csv",'w',newline="") as csvfile2:
    writer = csv.writer(csvfile2)

    writer.writerow(header_list)
    for j in data_list:
        writer.writerow(j)
    

