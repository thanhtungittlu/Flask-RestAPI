#tính kế thừa

class Student:
    def __init__(self,name,school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    @classmethod
    def friends(cls,origin,friend_name,*salary):  
        return cls(friend_name,origin.school,*salary)

# student1 = Student("Tung","ThangLong")
# student2 = Student.friends(student1,"Hung")
# print(student2.name)
# print(student2.school)

####
#Khi dùng tính kế thừa
class WorkingStudent(Student):
    def __init__(self,name,school,salary,job_title):
        super().__init__(name,school)
        self.salary = salary
        self.job_title = job_title

student1 = WorkingStudent("Tung","ThangLong", 50,"Sale")

friend = WorkingStudent.friends(student1,"Nam",60,"IT")
friend2 = Student.friends(student1,"Hung")

print(student1.salary)
print(friend.name,friend.salary,friend.job_title)
print(friend2.name)