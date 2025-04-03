word=input("Enter a string :")
def rev(a):
    b=''
    for i in a:
       b= i + b
       return b

print("The reverse of the string is :",rev(word))
