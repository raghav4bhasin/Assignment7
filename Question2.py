Stu_Dict = {}
Marks_Dict = {}

for i in range(1, 4):
    key = input("Enter name of Student: ")
    val = Marks_Dict = \
          { input("\tEnter First Subject: ") : int(input("\t\tEnter Marks:")), \
            input("\tEnter Second Subject: ") : int(input("\t\tEnter Marks:")),\
            input("\tEnter Third Subject: ") : int(input("\t\tEnter Marks:")) }

    print(" ")
    Stu_Dict[key] = val
print(" ")
name = input("Enter Name of the student to view their marks: ")
if name in Stu_Dict:
    print("Marks:", Stu_Dict[name])
