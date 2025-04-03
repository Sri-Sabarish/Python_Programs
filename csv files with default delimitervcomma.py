import csv
with open("D:\\csv files\\Fruits.csv",'r')as f:
    reader=csv.reader(f)
for row in reader:
    print(row)

