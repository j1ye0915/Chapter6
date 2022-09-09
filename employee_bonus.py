import csv

infile = open('EmployeePay.csv','r')

csvfile = csv.reader(infile,delimiter=',')


next(csvfile)
data_list = []
for record in csvfile:
   data_list = [record[1]+ ' ' + record[2],int(record[3]) * (1 + float(record[4]))]
   print(data_list,sep='')

infile.close()