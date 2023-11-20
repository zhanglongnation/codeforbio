import re
filein=open("TGS_pol3.fasta.masked_trans",'r')
for line in filein:
    if line.startswith(">"):
        name=line[1:]
    else:
        a=[substr.start() for substr in re.finditer("[ATCG]+",line)]
        b=[substr.end() for substr in re.finditer("[ATCG]+",line)]
        length=len(a)
        for i in range(0,length):
            if b[i] -a[i] > 10:
                print(">"+name.strip()+":"+str(a[i]+1)+"-"+str(b[i]))
                print(line[a[i]:b[i]])
filein.close()
