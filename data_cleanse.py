import nltk
import string
from nltk.corpus import stopwords
import csv
import re

stemmer=nltk.PorterStemmer()

orig_file=csv.reader(open('Training.csv','rU')) #read in orignal data file
clean_file=csv.writer(open('clean_train.csv','w')) #output file
clean_file.writerow(['class','doc']) 

wordlist=[] #a list of word for every line of data
stop_f = open('stoplist.txt', 'r') #stopwords list
stopw = stop_f.read() #read stopwords into a list and strip return characters
stopw = stopw.split('\r\n')

training=[] #training is a list of all wordlists

for line in orig_file:
    s=line[1] #extract line of data
    s=s.lower() 
    for word in re.findall('@[a-z0-9_]*',s):
        word = '@'
    #remove punctuations
    out = s.translate(string.maketrans("",""), string.punctuation)
    tokens = nltk.word_tokenize(out) #tokenize string into list of words
    wordlist=[]
    wordlist.append(line[0]) #first element in the list is class (0 or 1)
    for w in tokens: #remove stopwords
        if "http" in w:
            w="http"
        if w not in stopw:
            w=stemmer.stem(w)
            wordlist.append(w)
    training.append(wordlist) #add to training list
    clean_file.writerow(wordlist) #output cleansed data to a file

