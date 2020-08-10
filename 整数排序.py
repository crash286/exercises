print("————————从小到大排序————————")
number=[]                                  #建立空数组
print("输入需要排序的五个数:")
q=0
while q<5:
    a=float(input())                      #输入转化成浮点数
    number.append(a)                      #输入进入数组
    q+=1
j=0
while j<=len(number)-2:
    i=0
    while i<len(number)-1:
        if number[i]>number[i+1]: 
            temp=number[i]                #交换数组顺序
            number[i]=number[i+1]
            number[i+1]=temp
        i+=1
    j+=1
print("排序结果:")
print(number)

        
