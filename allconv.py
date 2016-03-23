import os
f=open('files.txt')
l=f.readlines()
f.close()
for i in l:
    fil=i.strip('\n')
    os.system('bash ssf2conll.sh ~/ltrc/sum2015/treebank/code/ff3/'+fil+' new/'+fil+'.out new/'+fil+'.log intra')
