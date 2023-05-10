import fileinput,sys
import argparse
parser = argparse.ArgumentParser(description="Genetics marker blast result filtering")
parser.add_argument("--input",help="Genetics marker blast input")
parser.add_argument("--output",help="filtered blast output")
args=parser.parse_args()
filein=args.input
fileout=args.output
q=[]
b=[]
dic={}
for line in fileinput.input(filein):
    line=line.strip().split("\t")
    if fileinput.lineno() == 1 :
        b.append(line[0])
        if line[11].isdigit():
            q.append(int(line[11]))
        else:
            q.append(float(line[11]))
    elif fileinput.lineno() != 1 and  line[0] not in b :
        num=q.count(max(q))
        if num >1 :
            q=[]
            b=[]
            if line[11].isdigit():
                q.append(int(line[11]))
            else:
                q.append(float(line[11]))
            b.append(line[0])
        else:
            #print(b[-1]+"      "+str(max(q)))
            dic[b[-1]]=str(max(q))
            q=[]
            b=[]
            if line[11].isdigit():
                q.append(int(line[11]))
            else:
                q.append(float(line[11]))
            b.append(line[0])
    elif line[0] in b:
        if line[11].isdigit():
            q.append(int(line[11]))
        else:
            q.append(float(line[11]))
num=q.count(max(q))
if num == 1 :
    #print(b[-1]+"      "+str(max(q)))
    dic[b[-1]]=str(max(q))
#print(dic)

filein3 = open(fileout,'w')
filein2=open(filein,'r')
for line in filein2:
    line1=line.strip()
    line2=line.strip().split("\t")
    if line2[0] in dic and line2[11] == dic[line2[0]]:
        filein3.write(line1+"\n")
