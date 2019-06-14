from student import Student  
from school import School

sc = School()

s = Student("pinsi", "F")
s.add_score(100)
sc.add_student(s)

s = Student("prmge", "M")
s.add_score(98)
sc.add_student(s)


sc.print()


while(True):
    cmd = int(input("1 = add student\ 2 = print all\ 3 = add score "))
    if cmd == 1:
        name = input("name:")
        sex = input("sex:")
        s = Student(name, sex)
        sc.add_student(s)
    elif cmd == 2:
        sc.print()
    elif cmd == 3:
        name = input("name:")
        score = int(input("score:"))
        s = sc.get_student(name)
        s.add_score(score)



