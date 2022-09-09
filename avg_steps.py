from audioop import avg
import csv
from locale import MON_1, MON_10, MON_11, MON_12, MON_2, MON_3, MON_4, MON_5, MON_6, MON_7, MON_8, MON_9

infile = open('steps.csv','r')

csvfile1 = csv.reader(infile,delimiter=',')

next(csvfile1)
currentRow = 0
list = []
for row in csvfile1:
    list.append(row)
    currentRow += 1

sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0
sum5 = 0
sum6 = 0
sum7 = 0
sum8 = 0
sum9 = 0
sum10 = 0
sum11 = 0
sum12 = 0
counter1 = 0
counter2 = 0
counter3 = 0
counter4 = 0
counter5 = 0
counter6 = 0
counter7 = 0
counter8 = 0
counter9 = 0
counter10 = 0
counter11 = 0
counter12 = 0
for i in range(currentRow-1):
    # prfloat(float(list[i][0]))
    if float(list[i][0]) == 1:
        sum1 += float(list[i][1])
        counter1 += 1

    elif float(list[i][0]) == 2:
        sum2 += float(list[i][1])
        counter2 += 1

    elif float(list[i][0]) == 3:
        sum3 += float(list[i][1])
        counter3 += 1
       
    elif float(list[i][0]) == 4:
        sum4 += float(list[i][1])
        counter4 += 1

    elif float(list[i][0]) == 5:
        sum5 += float(list[i][1])
        counter5 += 1

    elif float(list[i][0]) == 6:
        sum6 += float(list[i][1])
        counter6 += 1

    elif float(list[i][0]) == 7:
        sum7 += float(list[i][1])
        counter7 += 1

    elif float(list[i][0]) == 8:
        sum8 += float(list[i][1])
        counter8 += 1

    elif float(list[i][0]) == 9:
        sum9 += float(list[i][1])
        counter9 += 1

    elif float(list[i][0]) == 10:
        sum10 += float(list[i][1])
        counter10 += 1
    
    elif float(list[i][0]) == 11:
        sum11 += float(list[i][1])
        counter11 += 1

    elif float(list[i][0]) == 12:
        sum12 += float(list[i][1])
        counter12 += 1

avg1 = sum1/counter1
avg2 = sum2/counter2
avg3 = sum3/counter3
avg4 = sum4/counter4
avg5 = sum5/counter5
avg6 = sum6/counter6
avg7 = sum7/counter7
avg8 = sum8/counter8
avg9 = sum9/counter9
avg10 = sum10/counter10
avg11 = sum11/counter11
avg12 = sum12/counter12

header = ['Month','AVG']
MON_1 = ['January',avg1]
MON_2 = ['Febuary',avg2]
MON_3 = ['March',avg3]
MON_4 = ['April',avg4]
MON_5 = ['May',avg5]
MON_6 = ['June',avg6]
MON_7 = ['July',avg7]
MON_8 = ['August',avg8]
MON_9 = ['September',avg9]
MON_10 = ['October',avg10]
MON_11 = ['Novemeber',avg11]
MON_12 = ['December',avg12]

with open("avg_steps.csv",'w',newline="") as csvfile2:
    writer = csv.writer(csvfile2)

    writer.writerow(header)
    writer.writerow(MON_1)
    writer.writerow(MON_2)
    writer.writerow(MON_3)
    writer.writerow(MON_4)
    writer.writerow(MON_5)   
    writer.writerow(MON_6)
    writer.writerow(MON_7)
    writer.writerow(MON_8)
    writer.writerow(MON_9)
    writer.writerow(MON_10)
    writer.writerow(MON_11)
    writer.writerow(MON_12)


