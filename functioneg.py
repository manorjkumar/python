'''def add():
    c=a+b
    print(c)
def multiplay():
    d=a*b
    print(d)
   

a=int(input("enter a value: "))
b=int(input("enter b value: "))
add()
multiplay()

def findevenorodd(a):
   if(a%2==0):
       print("it's a even number")
   else:
       print("it's a odd number")

findevenorodd(int(input("enter the value: ")))'''

def printrange(a,b):
    for i in range(a,b):
        print(i,end="")
    
printrange(1,11)    
