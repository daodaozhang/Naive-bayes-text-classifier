import csv

infile=csv.reader(open('clean_train.csv','rU')) 
outfile=csv.writer(open('PercentageMatrix.csv','w'))
outfile2=csv.writer(open('FreqMatrix.csv','w'))
infile.next()

terms=['class']
for line in infile:
    for item in line[1:]:
        if item not in terms:
            terms.append(item)
outfile.writerow(terms)
outfile2.writerow(terms)

infile2=csv.reader(open('clean_train.csv','rU'))

for line in infile2:
    term_dict={}
    term_list=[line[0]] #percentage of term frequency/number of terms in document
    freq_list=[line[0]] # term frequency
    doc_size=len(line)-1
    for item in line[1:]:
        if item not in term_dict:
            term_dict[item]=1
        else:
            term_dict[item] += 1
    for value in terms:
        if value in term_dict:
            freq_list.append(term_dict[value])
            term_list.append(100.0*term_dict[value]/doc_size)
        else:
            freq_list.append(0)
            term_list.append(0)
    outfile.writerow(term_list)
    outfile2.writerow(freq_list)
