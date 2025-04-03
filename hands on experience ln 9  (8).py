A=[]
for i in range(1,21):
    A.append(i)
    for j in A:
        if j%3==0:
            A.remove(j)
print(A)        
