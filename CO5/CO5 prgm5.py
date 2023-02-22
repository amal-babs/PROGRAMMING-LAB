import csv
student=[{'no.':1,'name':'ab','sec':'mca'},{'no.':2,'name':'abn','sec':'mba'},{'no.':3,'name':'aan','sec':'mca'}]
csvfile=open('names.csv','w')
field_names=list(student[0].keys())
writer=csv.DictWriter(csvfile,fieldnames=field_names)
writer.writeheader()
writer.writerows(student)
csvfile.close()
csv_file=open('names.csv','r')
reader=csv.reader(csv_file)
for x in csv_file:
    print(x,end="")

