import argparse
from collections import Counter
parser = argparse.ArgumentParser(description="filter the interproscan output.")
parser.add_argument("--inter_result",help="interproscan result input")
#parser.add_argument("--filter_result",help="fitered interproscan output")
args=parser.parse_args()
file_in=args.inter_result
#file_out=args.filter_result
print("            "+"<<"+str(file_in)+"  result"+">>")
tx="Acyr_pis,Arma_nasa,Dap_pul,ESIN,Hamer,Macro_nip,Pe_van,Pmonodon,Por_tri,Pvir,Scyl,Str_mar,Zoo_nev".split(",")
def output(seq_name_list,function_list,function_tuple_list):
    tt,tb=long(seq_name_list)
    if tt == 0 and tb ==0 :
        pass
    else:
        print(function_tuple_list[tb])
        print('  """  '.join(function_tuple_list))
        for i in seq_name_list:
            spe_num=[]
            ta=set(i)
            for x  in ta:
                spe_num.append(x.split("|")[0])
            num_spe=counter(spe_num)
            for t in tx:
                if t not in counter(spe_num).keys():
                    num_spe[t]=0
            if len(ta) == tt:
                print(len(ta),num_spe)
                for i in sorted(num_spe.keys()):
                    print(num_spe[i],end="\t")
                print("")
                print("\t".join(sorted(num_spe.keys())))
            else:
                print(len(ta),num_spe)
def counter(arr):
    return Counter(arr)
def long(ta):
    x=[]
    for i in ta:
        x.append(len(set(i)))
    if len(x)!= 0:
        return max(x),x.index(max(x))
    else:
        return 0,0

panther=[]
pfam=[]
for i in open(file_in,'r'):
    s=i.split("\t")
    if s[3] == "PANTHER":
        panther.append(s[5])
    if s[3] == "Pfam":
        pfam.append(s[5])
pant=list(set(panther))
pfam2=list(set(pfam))
pan_num=len(pant)
pfam_num=len(pfam2)
pfam_list=[]
panther_list=[]
for i in range(pan_num):
    panther_list.append([])
for i in range(pfam_num):
    pfam_list.append([])
for i in open(file_in,'r'):
    s=i.split("\t")
    if s[3] == "PANTHER":
        posi=pant.index(s[5])
        panther_list[posi].append(s[0])
    if s[3] == "Pfam":
        posi=pfam2.index(s[5])
        pfam_list[posi].append(s[0])

print("                                             ---------------------------Pfam  Result-------------------------------")
output(pfam_list,pfam,pfam2)
#print(pfam2)
#for i in pfam_list:
#    print(len(set(i)),end="\t")
print("")
print("                                                     ------------------PATHER Result-------------------                      ")
output(panther_list,panther,pant)
print("")
print("")
