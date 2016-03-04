f1=open("output1600.txt","r")
f=open("output1600-forROC.txt","w")

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



for j in range(10):
    start=j*n
    end=j*n+1031
    print j,start,end
    for i in range(start,end):
        f.write(str(seq_pool[i][1]))
        f.write("\t")
        f.write(str(seq_pool[i][0]))
        f.write("\t")
        #pos label
        if j%2==0:
            f.write("+1")
        else:
            f.write("-1")
        f.write("\n")






        


f1.close()
f.close()
