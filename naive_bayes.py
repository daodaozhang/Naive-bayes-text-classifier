import nltk
import csv
import math

infile = csv.reader(open('clean_train.csv','rU'))
infile.next()
testfile=csv.reader(open('sample_test1.csv','rU'))

outfile=csv.writer(open('nb_result.csv','w'))

terms_neg={}  #unique vocalbulary and occurances of term in training data in class 0
terms_pos={}

N=0 #number of doc
N0=0 #number of doc in class 0
N1=0 #number of doc in class 1

for line in infile:
    N+=1
    if line[0] == '0':
        N0+=1
        for item in line[1:]:
            if item not in terms_neg:
                terms_neg[item]=1
            else:
                terms_neg[item]+=1


    elif line[0] == '1':
        N1+=1
        for item in line[1:]:
            if item not in terms_pos:
                terms_pos[item]=1
            else:
                terms_pos[item]+=1

sum_t_neg = sum(terms_neg.values())  #sum of occurances of all terms in class neg
sum_t_pos = sum(terms_pos.values())

cond_prob_neg={}
cond_prob_pos={}

for index, value in terms_neg.items():
    V=0
    if index in terms_pos:
        V = value+terms_pos[index]
    else:
        V=value
    prob_t_neg = (value+1)*1.0/(sum_t_neg+V) #conditional probability p(t|c)
    cond_prob_neg[index]=prob_t_neg

for index, value in terms_pos.items():
    V=0
    if index in terms_neg:
        V = value+terms_neg[index]
    else:
        V=value
    prob_t_pos = (value+1)*1.0/(sum_t_pos+V) #conditional probability p(t|c)
    cond_prob_pos[index]=prob_t_pos

pos_feature=[]  #positive feature selection
neg_feature=[]

for key, value in cond_prob_pos.iteritems():
    temp = [key,value]
    pos_feature.append(temp)
for key, value in cond_prob_neg.iteritems():
    temp = [key, value]
    neg_feature.append(temp)

pos_feature= sorted(pos_feature, key=lambda x: x[1], reverse=True)
pos_feature= pos_feature[1:101]
neg_feature=sorted(neg_feature, key=lambda x: x[1], reverse=True)
neg_feature= neg_feature[1:101]

cond_prob_neg = dict(neg_feature)
cond_prob_pos = dict(pos_feature)

prior0=N0*1.0/N  #prior probability of class negative
prior1=N1*1.0/N

print prior0

c=[]   #predicted class for negative

for line in testfile:
    p_neg=math.log(prior0) #log of prior probability
    p_pos=math.log(prior1)
    for item in line[1:]:
        if item in cond_prob_neg:
            p_neg+=math.log(cond_prob_neg[item])
        if item in cond_prob_pos:
            p_pos+=math.log(cond_prob_pos[item]) #probability of test document being class positive
    

    if p_neg >=  p_pos:
         c.append(0)   #list c of predicted class of test documents
    else:
         c.append(1)

testfile2=csv.reader(open('sample_test1.csv','rU'))

for idx, line in enumerate(testfile2):
    if line[0] == '0' or line[0] == '1':
        outfile.writerow([line[0],c[idx]])






