f1=open("pos_Windows41.txt","r")
f=open("pos_svm_type.txt","w")

d={"A":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"K":9,"L":10,"M":11,"N":12,"P":13,"Q":14,"R":15,"S":16,"T":17,"V":18,"W":19,"Y":20}
d["-"]=21

allseq=[]
while True:
    line=f1.readline()[:-1]
    allseq.append(line)

    if not line:
        break
allseq.pop()
seq_pool=allseq




def write_svm_code(seq):
    code_list=[0]*(21*len(seq))

    for i in range(len(seq)):
        for each_key in d:
            value = d[each_key]
            if seq[i] == each_key:
                code_list[21*i+value-1]=1

    for i in range(len(code_list)):
        if code_list[i]!=0:
            f.write("\t")
            f.write(str(i+1))
            f.write(":")
            f.write(str(code_list[i]))

for each_seq in seq_pool:
    f.write("1")
    write_svm_code(each_seq)
    f.write("\n")


    

f.close()
