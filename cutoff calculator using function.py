print("\t\tCUT OFF CALCULATOR")
math_mark=int(input("Enter your maths mark     :"))
chem_mark=int(input("Enter your chemistry mark :"))
phys_mark=int(input("Enter your physics mark   :"))
def cutoff(math_mark,chem_mark,phys_mark):
    mark= math_mark + chem_mark/2 + phys_mark/2
    print("\n")
    print("your cut off mark : ",mark,"/200")
cutoff(math_mark,chem_mark,phys_mark)    
    
