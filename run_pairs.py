import subprocess
import os

list_combos=open("combifile","r+").readlines()
cds_file = 'Malus_domestica_golden.ASM211411v1.cds.all.fa'
cds=open(cds_file,"r+").readlines()
prot_file = 'Malus_domestica_golden.ASM211411v1.pep.all.fa'
prot=open(prot_file,"r+").readlines()

KAKs = open('KAKs.file.txt','w')

import fileinput

def replace_in_file(file_path, old_str, new_str):
    for line in fileinput.input(file_path, inplace=True):
        print(line.replace(old_str, new_str), end='')


for pairs in list_combos:
    ids = pairs.split(';')[:2]
    print(ids)
    cds_sequences = []
    # Make file with pair of CDS
    cds_out=open('cds_pair.fa',"w+")
    for id in ids:
        if '.' in id:
            id = id.split('.')[0]
        if ':' in id:
            id = id.split(':')[1]
        # print(id)
        seq = ''
        for i in range(len(cds)):
            line = cds[i]
            if id in line:
                cds_out.write(line)
                i+=1
                while '>' not in cds[i]:
                    cds_out.write(cds[i])
                    # seq += cds[i][:-1]
                    i+=1

    cds_out.close()
    # Make file with pair of proteins
    prot_out=open('prot_pair.fa',"w+")
    for id in ids:
        if '.' in id:
            id = id.split('.')[0]
        if ':' in id:
            id = id.split(':')[1]
        # print(id)
        seq = ''
        for i in range(len(prot)):
            line = prot[i]
            if id in line:
                prot_out.write(line)
                i+=1
                while '>' not in prot[i]:
                    prot_out.write(prot[i])
                    # seq += cds[i][:-1]
                    i+=1
    prot_out.close()
    # for each pair extracted do:
    # print(cmd)
    # subprocess.run([ cmd], shell=True)

    # os.system('ls')

    cmd = 'clustalw2 -quiet -align -infile=' + os.getcwd() + '/prot_pair.fa -outfile=' + os.getcwd() + '/prot_pair.ali.fa' 
    os.system(cmd)
    
    cmd2 = './pal2nal.pl prot_pair.ali.fa cds_pair.fa -output paml > paml_input.phy'
    os.system(cmd2)


    replace_in_file('yn00.ctl_master.txt', 'XXXXX', 'paml_input.phy')

    # cmd3 = """awk -v file=paml_input.phy '{gsub("paml_input.phy",XXXXX); print $0}' yn00.ctl_master.txt > yn00.ctl"""
    os.system('cp yn00.ctl_master.txt yn00.ctl')

    os.system('./paml4.9h/bin/yn00 > yn00_file')

    with open("yn") as f:
        for i, line in enumerate(f):
            if i == 90:
                print(line.split()[6], line.split()[7], line.split()[10])
                newline = "\t".join([ ids[0] , ids[1], line.split()[6], line.split()[7], line.split()[10]])
    KAKs = open('KAKs.file.txt','a+')
    KAKs.write(newline + '\n')
    KAKs.close()
    # sed -i "1i gene1\tgene2\ka/ks\tka\tks KAKs.txt

