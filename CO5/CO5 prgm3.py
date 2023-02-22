import csv
df=open("student.csv")
csv_reader=csv.reader(df)
for line in df:
    print(line)
