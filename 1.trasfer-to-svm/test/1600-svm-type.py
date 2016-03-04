f1=open("pos_5155_41frame.txt","r")
f=open("pos_train_1600.txt","w")


d={"A":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"K":9,"L":10,"M":11,"N":12,"P":13,"Q":14,"R":15,"S":16,"T":17,"V":18,"W":19,"Y":20}



#dictionary for 2 amino acid
dict_list=[]
for key1, value1 in d.items():
    for key2, value2 in d.items():
        each_list=[]
        frame = key1+key2
        num = (value1-1)*20+ value2
        each_list.append(frame)
        each_list.append(num)
        dict_list.append(each_list)


seq1="ALTGTHVLGEAGTSVARIVNKIPQATRDITRDLEALEQHMN"

#read data
allseq=[]
while True:
    line=f1.readline()[:-1]
    flag=line.find("\t")
    sequence=line[:flag]

    allseq.append(sequence)

    if not line:
        break
allseq.pop()
seq_pool=allseq


def count1(seq): #20 dimension
    space_list=[]
    count_list=[]
    
    for i in range(len(seq)):
        space_list.append(seq[i:i+1])
    for key in d:
        count_list.append(space_list.count(key))
    num=sum(count_list)
    for i in range(len(count_list)):
        count_list[i]=count_list[i]/float(num)
    return count_list

def count2(seq): #20*20 400 dimension
    space_list=[]
    count_list=[]
    
    for i in range(len(seq)-1):
        space_list.append(seq[i:i+2])

    for key in dict_list:

        count_list.append(space_list.count(key[0]))
    num=sum(count_list)
    for i in range(len(count_list)):
        count_list[i]=count_list[i]/float(num)
    return count_list


    


def write_svm_code(seq):

    #get 10 20 30 40 frame in 41 window
    f_10=seq[15:20]+seq[21:26]
    f_20=seq[10:20]+seq[21:31]
    f_30=seq[5:20]+seq[21:36]
    f_40=seq[:20]+seq[21:]
    #code_list_1:
    code_list1=count2(f_10)
    code_list2=count2(f_20)
    code_list3=count2(f_30)
    code_list4=count2(f_40)

    
    for i in range(len(code_list1)):
        if code_list1[i]!=0:
            f.write("\t")
            f.write(str(i+1))
            f.write(":")
            f.write(str(code_list1[i]))
    for i in range(len(code_list2)):
        if code_list2[i]!=0:
            f.write("\t")
            f.write(str(i+401))
            f.write(":")
            f.write(str(code_list2[i]))
    for i in range(len(code_list3)):
        if code_list3[i]!=0:
            f.write("\t")
            f.write(str(i+801))
            f.write(":")
            f.write(str(code_list3[i]))
    for i in range(len(code_list4)):
        if code_list4[i]!=0:
            f.write("\t")
            f.write(str(i+1201))
            f.write(":")
            f.write(str(code_list4[i]))
        
for each_seq in seq_pool:
    f.write("1")
    write_svm_code(each_seq)
    f.write("\n")


f1.close()
f.close()
