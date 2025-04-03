list1=list(range(1,11))
print("The list of numbers from 1 to 10 :\n",list1)
for i in list1:
    if (i%2==1):
        list1.remove(i)
print("The list of numbers after removing odd numbers:\n",list1)        
