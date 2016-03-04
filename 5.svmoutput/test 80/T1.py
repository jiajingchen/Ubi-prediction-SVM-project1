f1=open("test_80output2.txt","r")
f=open("test80output2-forROC.txt","w")

n=1031
#read data
allseq=[]
while True:
    line=f1.readline()[:-1]

    sequence=line.split(" ")
    

    allseq.append(sequence)

    if not line:
        break
allseq.pop()
seq_pool=allseq

#print seq_pool



for i in range(len(seq_pool)):
    f.write(str(seq_pool[i][1]))
    f.write("\t")
    f.write(str(seq_pool[i][0]))
    f.write("\t")
    #pos label
    if i<5155:
        f.write("+1")
    else:
        f.write("-1")
    f.write("\n")






        


f1.close()
f.close()
