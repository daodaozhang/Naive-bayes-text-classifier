import csv

infile=csv.reader(open('nb_result.csv','rU'))

n1=0
n0=0
e1=0
e0=0
n=0
e=0

for line in infile:
    n+=1
    if line[0].strip() == '0':
        n0+=1
        if line[0] != line[1]:
            e0 +=1
            e+=1
    elif line[0].strip() == '1':
        n1+=1
        if line[0] != line[1]:
            e1+=1
            e+=1
    else:
        print line[0]

error_rate=e*1.0/n
error0=e0*1.0/n0
error1=e1*1.0/n1

print e, n
print "error rate: ", error_rate
print e1, n1
print "misclassification for positive: ", error1
print e0, n0
print "misclassification for negative: ", error0
