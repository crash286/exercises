print("————————从小到大排序————————")
print("            欢迎           ")
number=[]                                  
print("请输入需要排序的七个数:")
count=0
while count<7:
    initial_input=float(input())                      
    number.append(initial_input)                      
    count+=1
rounds=0
while rounds<=len(number)-2:
    times=0
    while times<len(number)-1:
        if number[times]>number[times+1]: 
            temp=number[times]                
            number[times]=number[times+1]
            number[times+1]=temp
        times+=1
    rounds+=1
print("排序结果:")
print(number)

        
