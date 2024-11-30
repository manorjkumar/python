#swapping first and last  number in list--->approach 1
'''arr1=[5,2,3,4,1]
print("before swapping : ",arr1)
size=len(arr1)

temp=arr1[0]
arr1[0]=arr1[size-1]
arr1[size-1]=temp
print(arr1)'''

#swapping first and last  number in list--->approach 2

'''arr1[0],arr1[-1]=arr1[-1],arr1[0]

print("after swapping",arr1)'''

#swapping first and last  number in list--->approach 3

'''get=(arr1[0],arr1[-1])
arr1[-1],arr1[0]=get
print("after swapping",arr1)'''

#swapping two number in any position---->approach1

'''arr1=[5,2,3,4,1]
print("before swapping ",arr1)
#arr1[0],arr1[2]=arr1[2],arr1[0]
arr1[0],arr1[-1]=arr1[-1],arr1[0]

print("after swapping ",arr1)'''

#swapping two number in any position---->approach1
arr1=[5,2,3,4,1]
print("before swappinf",arr1)
first_element=arr1.pop(arr1[1])
print("first_element",first_element)
second_element=arr1.pop(arr1[3])
print("second_element",second_element)

arr1.insert(arr1[0],second_element)
arr1.insert(arr1[2],first_element)
print("after swapping",arr1)
