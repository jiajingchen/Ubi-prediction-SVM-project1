f1=open("pn_train_1600.txt","r")
f=[]



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



#write traink test k file k=1:5


f_train=[]
f_test=[]
for i in range(5):
    train_name="train"+str(i+1)+".txt"
    test_name="test"+str(i+1)+".txt"

    f_train.append(open(train_name,"w"))
    f_test.append(open(test_name,"w"))

#write train
for j in range(5):
    print j
    train_list=[1,2,3,4,5]
    train_list.pop(j)
    for i in train_list:
                
        start=(i-1)*n
        end=i*n
        print start,end
        #write pos
        f_train[i-1].writelines(pos_pool[start:end])

        #neg
        f_train[i-1].writelines(neg_pool[start:end])  



#write test

for i in range(5):

    start=i*n
    end=(i+1)*n
    #write pos
    for j in range(start,end):
        f_test[i].write(pos_pool[j])
    for j in range(start,end):
        f_test[i].write(neg_pool[j])

    















