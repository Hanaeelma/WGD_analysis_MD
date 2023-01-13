fileout=open("combifile","w")
import itertools
from itertools import combinations
filein=open("MCSdata","r")
filein.readline()
l=[]
listeachfam=[]
for line in filein:
	line.rstrip()
	line=line.split("\t")
	l.append(line)   #liste for all the genes with their family: list of a liste composed of gene name and its family infront of it (transform th file into a list)
key_func = lambda x: x[1]
for key, group in itertools.groupby(l, key_func):
	a=list(group) 
	listeachfam.append(a) #list of a list the interior list is compsed of genes+fam appartenant à la même famille 


for fam in listeachfam:
 for i in fam:
    del(i[1])
#print(listeachfam)

def rSubset(arr, r):
	return list(combinations(arr, r))
r=2
for i in listeachfam:
	a=rSubset(i,2)
	print(a)
	
	for i in a:
		for j in i:
			str2 = ''.join(''.join(j))
			#print(str2)
			fileout.write(str2+";")
		fileout.write("\n")
	