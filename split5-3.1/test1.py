f1=open("pn_train_80.txt","r")
f=[]
for i in range(5):
    fname="train"+str(i+1)+"_80.txt"
    f.append(open(fname,"w"))
    print fname



allseq=[]
while True:
    line=f1.readline()
    allseq.append(line)

    if not line:
        break

    
allseq.pop()
seq_pool=allseq


N= len(allseq)
n=N/10

pos_pool=seq_pool[:N/2]
neg_pool=seq_pool[N/2:]
print len(pos_pool)
print len(neg_pool)


#write pos
for i in range(5):
    start=i*n
    end=(i+1)*n
    print start,end
    f[i].writelines(pos_pool[start:end])
    #neg
    f[i].writelines(neg_pool[start:end])  
    f[i].write("DONE") 
    print "done"


