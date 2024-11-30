#approach-->1
'''mylist=[55,22,41,2,3,45]
print("mylist before clearing",mylist)
mylist.clear()
print("mylist after clearing",mylist)'''



#approach 2--->initialize the list with no value
'''mylist=[55,22,41,2,3,45]
print("mylist before clearing",mylist)
mylist=[]
print("mylist after clearing",mylist)'''


#approach 3--->"*=0"
'''mylist=[55,22,41,2,3,45]
print("mylist before clearing",mylist)
mylist *=0
print("mylist after clearing",mylist)'''



#question 2 reverse the list
'''mylist=[55,22,41,2,3,45]
print("mylist before reverse",mylist)
mylist.reverse()
print("mylist after reverse",mylist)'''


#approach 2---->slicing techniqe
'''mylist=[55,22,41,2,3,45]
print("mylist before reverse",mylist)
mylist2=mylist[::-1]
print(mylist2)''' 

#question 3---->clone or copy list---approach1
'''mylist=[55,22,41,2,3,45]
copy_list=[]
copy_list.extend(mylist)
print(copy_list)'''


#approach2---->copy()method
mylist=[55,22,41,2,3,45]
copy_mylist=mylist.copy()
print(copy_mylist)
