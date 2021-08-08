sum=0
num=input("Enter a number: ")
num_list=list(num)
for i in range(0, len(num_list)):
    if num_list[i]=='1':
        if i==0:
            sum=sum+8
        elif i==1:
            sum=sum+4
        elif i==2:
            sum=sum+2
        else:
            sum=sum+1
print(sum)

