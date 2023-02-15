#6. Store a list of first names. Count the occurrences of ‘a’ within the list
names=['Ashik','Lishan','Abdullah','Liyona','Aardhra']
count=0
for name in names:
    count=count+name.count('a')
print("Occurence of 'a' in list:",count)  