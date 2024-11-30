#fibonacci--->0, 1, 1, 2, 3, 5, 8, 13, 21....
#              n1 n2 n1 n2
'''n1=0
n2=1
print(n1)
print(n2)

for i in range (2,10):
    sum=n1+n2
    print(sum)'''

#sum of digites
'''arr=[1,2,3,4,5]
#print(sum(arr))
print(sum(arr,10))'''

#min and max number

'''arr=[10,2,50,30,24,98]

max=arr[0]
n=len(arr)

for i in range(1,n):
    if arr[i]>max:
        max=arr[i]
        
print("maximum number is: ",max)'''

#max number
'''arr=[10,2,50,30,24,98]

min=arr[0]
n=len(arr)

for i in range(1,n):
    if arr[i]<min:
        min=arr[i]

print("minimum numberof arr is: ",min)'''

#find length of list

arr=[10,2,50,30,24,98]

count=0
for i in arr:
    count=count+1
print("length of given list is : ",count)



print("length of given list is: ",len(arr))






