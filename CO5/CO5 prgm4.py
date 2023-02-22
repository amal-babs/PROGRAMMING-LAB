import csv
filename = "details.csv"
ff=open(filename, 'r') 
data = csv.DictReader(ff)
print("No. Brand Model")
for x in data:
    print(x['No'], x['Brand'], x[‘Model'])
