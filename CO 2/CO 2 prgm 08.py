l=['Where','there','is','a','will','there','is','a','way']
long=0
for i in l:
    if len(i)>long:
        long=len(i)
print("Length of longest word",long)
