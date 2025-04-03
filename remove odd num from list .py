number=[]
for i in range(1,11):
    number.append(i)
print("Numbers from 1 to 10 :\n",number)
    
for j in number:
    if j%2==1:
        number.remove(j)
print("The values after removing odd numbers from the list : \n",number)        
