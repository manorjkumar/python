#swap two numbers
'''num1=int(input("enter your number for num1: "))
num2=int(input("enter your number for num2: "))

temp=num1
num1=num2
num2= temp

print("after swaping num1",num1)
print("after swaping num2",num2)

#second method

num1,num2=num2,num1'''



#check prime number

'''num=int(input("enter your number: "))
count=0
if(num>1):
    for i in range(1,num+1):
        if(num%i)==0:
            count=count+1
    if count ==2:
        print("it's a prime numbers")
    else:
        print("not prime")

#check factorial /first method/
fact=1
num=int(input("enter your number: "))
if(num<0):
    print("there is no factorial for +ive numbers")
elif(num==0):
    print("zero factorial is 1")
else:
    for i in range(1,num+1):
        fact=fact*i
    print("factorial of",num,"is: ",fact)  
    
#check factorial /second  method/ or return 1 if (n==0 or n==1)else  n*factorial(num)

def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
num=int(input("enter the value: "))
fact=factorial(num)
print("the factorial of ",num,"is : "fact)'''

def factorial(n):
    return 1 if(n==0 or n==1)else  n*factorial(n-1)
num=5
print("factorial of",num, "is: ",factorial(num))
