'''#----------'sum of natural number 1 to 5'-----------
sum =0;
for i in range(1,6):
    sum=sum+i
    #print(sum)
    #sum=sum
print(sum)'''

'''-----take some number find sum of all digite and average------
sum=0
a=[]

numbers=int(input("enter how many numbers: "))
for i in range(numbers):
    a.append(int(input("enter number"+str(i)+": ")))
print(a)
sum=0
for i in a:
    sum=sum+i
print("sum of every digite",sum)
avg =sum/numbers
print("average of sum of every number",avg)'''
    

j=0
numbers = int(input("enter how many integers"))
for i in range(numbers):
    j=i
    i=i*i*i
    print("qube of ",j,"is: ",i)












