'''for i in range(1,11):
    print(i,"X3=",i*3)
a=3
b=5
c=a//5
print(c)
d=a/b
print(d)'''

#s=int(input())
#e=int(input())
'''count=0
count1=0
for i in range(1,11):
   if(i%2==0):
      count=count+1
   elif(i%2!=0):
       count1=count1+1
   else:
       print("nothing")
      
print("odd count",count1)
print("even count",count)'''

count=0
elsecount=0
for i in range(1,101):
   if(i%3==0 and i%5==0):
      count=count+1
      print("that numbers",i)
   else:
      #print("not divisible by 3,5")
      elsecount=elsecount+1
print(count)
print(elsecount)

   
      




