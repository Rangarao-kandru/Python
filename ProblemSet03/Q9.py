9.Write a function called is_sorted that takes a list as a parameter and returns True if the list is sorted in ascending order and False otherwise. You can assume (as a precondition) that the elements of the list can be compared with the relational operators <, >, etc. For example, is_sorted([1,2,2]) should return True and is_sorted(['b','a']) should return False.


def is_sorted(mylist):
   list1=mylist.copy()
   list1.sort()
   if mylist==list1:
       return True
   else:
       return False

print(is_sorted(['b','a']))
print(is_sorted([1,1,2]))

def is_sorted(mylist):
    flag=True
    for i in range(len(mylist)):
        for j in range(i+1,len(mylist)):
            if mylist[i]<=mylist[j]:
                continue
            else:
                flag=False
                break
    if flag:
        return True
    else:
        return False
    
print(is_sorted(['b','a']))
print(is_sorted([1,1,2]))

Output:

False
True
False
True

