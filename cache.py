import math
def direct(tag,index,offset,tagar,dataar,data,ch,tags):
    tagch=tagar[index]
    if(tag==int(tagch,2)):
        if(ch==1):#write
            if(dataar[index][offset]==0):
                dataar[index][offset]=data
            else:
                print("Replacing "+str(dataar[index][offset])+" with "+ str(data))
                dataar[index][offset]=data
        if(ch==2):#read
            print("Data: "+ str(dataar[index][offset]))
    else:
        print("MISS")
        print("Replacing "+tagar[index]+" with "+tags)
        tagar[index]=tags
        for j in range(len(dataar[0])):
                dataar[index][j]=0
        dataar[index][offset]=data


def fa(tag,tagar,offset,dataar,ch,data,cl,tags,counter):
    c=0
    for i in range(cl):
        if(int(tagar[i],2)==tag):
            if(ch==1):
                if(dataar[i][offset]==0):
                    dataar[i][offset]=data
                    c=1
                    counter[i]=1000
                    for j in range(len(counter)):
                        if(j!=i):
                            counter[j]-=1
                    break
                else:
                    print("Replacing "+str(dataar[i][offset])+" with "+ str(data))
                    dataar[i][offset]=data
                    c=1
                    counter[i]=1000
                    for j in range(len(counter)):
                        if(j!=i):
                            counter[j]-=1
                    break

            if(ch==2):
                print("Data: "+ str(dataar[i][offset]))
                c=1
                counter[i]=1000
                for j in range(len(counter)):
                        if(j!=i):
                            counter[j]-=1
                break
    if(c==0): 
        print("MISS")
        if(ch==1):
            minpos=counter.index(min(counter))
            print("Replacing "+ tagar[minpos]+" with "+ tags)
            #print(counter)
            tagar[minpos]=tags
            for j in range(len(dataar[0])):
                dataar[minpos][j]=0
            #print(tagar)
            dataar[minpos][offset]=data
            counter[minpos]=1000
    return(counter,dataar)

def sa(tag,tagar,offset,index,dataar,data,cl,n,ch,tags,counter):
    c=0
    j=n
    if(index>cl-n-1):
        j=cl-n-index
    for i in range(n*index,n*(index+1)):
        if(int(tagar[i],2)==tag):
            if(ch==1):
                if(dataar[i][offset]==0):
                    dataar[i][offset]=data
                    c=1
                    counter[i]=1000
                    for j in range(len(counter)):
                        if(j!=i):
                            counter[j]-=1
                    break
                else:
                    print("Replacing "+str(dataar[i][offset])+" with "+ str(data))
                    dataar[i][offset]=data
                    c=1
                    counter[i]=1000
                    for j in range(len(counter)):
                        if(j!=i):
                            counter[j]-=1
                    break
            if(ch==2):
                print("Data: "+ str(dataar[i][offset]))
                c=1
                counter[i]=1000
                for j in range(len(counter)):
                    if(j!=i):
                        counter[j]-=1
                break
    if(c==0):
        mini=counter[n*index] 
        minpos=n*index
        print("MISS")
        for j in range(n*index,n*(index+1)):
            if(counter[j]<mini):
                mini=counter[j]
                minpos=j
        print("Replacing "+ tagar[minpos]+" with "+ tags)
        #print(counter)
        tagar[minpos]=tags
        for j in range(len(dataar[0])):
            dataar[minpos][j]=0
        #print(tagar)
        dataar[minpos][offset]=data
        counter[minpos]=1000
    return(counter,dataar)
        

def disp(ar):
    for i in ar:
        print(i)


#test address for direct mapping=10101000100101100111101010000110
#test address for fully associative=01011001111101101111011010100100
#test address for set associative=11000000100000101001000011101011
tagar=[]
cl=int(input(("Enter Cache Lines: ")))
for i in range(cl):
    tagar.append("0")
dataar=[]
bitsize=int(math.log(cl,2))
# print(bitsize)
bs=int(input("Enter block size: "))
bitsize2=int(math.log(bs,2))
for i in range(cl):
    dataar.append([])
for i in range(cl):
    for j in range(bs):
        dataar[i].append(0)
# tagar[106]="1010100010010110011"
# tagar[90]="01011001111101101111011010"
# tagar[7]="1100000010000010100"
tagindex=0
ask=True
print("Cache Size: " + str(cl*bs*4)+" bytes")
print("Cache Mapping Choice:")
print("1. Direct Mapping")
print("2. Fully Associated Mapping")
print("3. Set Association Mapping")
print("4. Exit")
a=int(input())
run=True
counter=[]
for i in range(len(tagar)):
    counter.append(0)
while(run):
    wrong=True
    if(a==1):
        no=True
        add=input("Enter Address ")
        ch=int(input("Enter 1 for write ; 2 for read ; 3 to exit ; 4 to print cache "))
        if(ch==1):
            data=int(input("Enter data "))
        elif(ch==2):
            data=0
        elif(ch==3):
            run=False
            data=0
        elif(ch==4):
            disp(dataar)
            data=0
        else:
            print("Choice error")
            #run=False
            wrong=False
            data=0
        # tags=add[0:19]
        # tag=int(add[0:19],2)
        # index=int(add[19:19+bitsize],2)
        # offset=int(add[19+bitsize:19+bitsize+bitsize2],2)
        offset=int(add[-bitsize2:],2)
        index=int(add[-bitsize2-bitsize:-bitsize2],2)
        tag=int(add[0:32-bitsize-bitsize2],2)
        tags=add[0:32-bitsize-bitsize2]
        if(tagar[index]==tags):
            no=False
        if(no and ch==1):
            if(tagar[index]=="0" and index<cl):
                tagar[index]=tags
            
        if(run and ch!=4 and wrong and ch!=3):
            direct(tag,index,offset,tagar,dataar,data,ch,tags)
    if(a==2):
        no=True
        wrong=True
        add=input("Enter Address ")
        ch=int(input("Enter 1 for write ; 2 for read ; 3 to exit ; 4 to print cache "))
        if(ch==1):
            data=int(input("Enter data "))
        elif(ch==2):
            data=0
        elif(ch==3):
            run=False
            data=0
        elif(ch==4):
            disp(dataar)
            data=0
        else:
            print("Choice error")
            #run=False
            data=0
            wrong=False
        # tag=int(add[0:26],2)
        # tags=add[0:26]
        # offset=int(add[26:26+bitsize2],2)
        offset=int(add[-bitsize2:],2)
        tag=int(add[0:32-bitsize2],2)
        tags=add[0:32-bitsize2]
        for i in tagar:
            if(tags==i):
                no=False
        if(no and ch==1):
            if(tagindex<cl):
                tagar[tagindex]=tags
                tagindex+=1
        if(run and ch!=4 and wrong and ch!=3):
            counter,dataar=fa(tag,tagar,offset,dataar,ch,data,cl,tags,counter)
    if(a==3):
        no=True
        wrong=True
        if(ask):
            n=int(input("Enter n "))
            ask=False
        add=input("Enter Address ")
        ch=int(input("Enter 1 for write ; 2 for read ; 3 to exit 4 ; to print cache "))
        if(ch==1):
            data=int(input("Enter data "))
        elif(ch==2):
            data=0
        elif(ch==3):
            run=False
            data=0
        elif(ch==4):
            disp(dataar)
            data=0
        else:
            print("Choice error")
            #run=False
            data=0
            wrong=False
        # tags=add[0:19]
        # tag=int(add[0:19],2)
        # index=int(add[19+int(math.log(n,2)):19+bitsize],2)
        # offset=int(add[19+bitsize:19+bitsize+bitsize2],2)
        offset=int(add[-bitsize2:],2)
        index=int(add[-bitsize2-bitsize+int(math.log(n,2)):-bitsize2],2)
        tag=int(add[0:32-bitsize-bitsize2],2)
        tags=add[0:32-bitsize-bitsize2]
        if(tagar[index]==tags):
            no=False
        if(no):
            try:
                if(ch==1):
                    for i in range(n*(index),n*(index+1)):
                        if(tagar[i]=="0" and i<cl):
                            tagar[i]=tags
                            break
            except(IndexError):
                pass
        if(run and ch!=4 and wrong and ch!=3):
            counter,dataar=sa(tag,tagar,offset,index,dataar,data,cl,n,ch,tags,counter)
    if(a==4):
        run=False
        
        





