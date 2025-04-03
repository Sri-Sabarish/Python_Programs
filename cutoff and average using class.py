class student:
    maths=int(input("Enter your maths mark:"))
    physics=int(input("Enter your physics mark:"))
    chemistry=int(input("Enter your chemistry mark:"))
    def cutoff(self):
        cutoff= student.maths+ student.physics/2 + student.chemistry/2
        average= (student.maths + student.physics + student.chemistry)/3
        print("Your cutoff mark is ",cutoff, "out of 200")
        print("Your average mark in major subject is",round(average))
s=student()
s.cutoff()
        
