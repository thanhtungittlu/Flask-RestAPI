
lottery_players = {
    "name": "Tung",
    "numbers": (13,45,67,58,90)
}

class LotteryPlayer:
    def __init__(self,name):
        self.name = name
        self.numbers = (13,45,67,58,90)
    def total(self):
        return sum(self.numbers)
player1 = LotteryPlayer("Tung")
print(player1.name)
print(player1.total())

player2 = LotteryPlayer("Hung")

player2.numbers = (1,3,5,7,9)
print(player2.name)
print(player2.total())

print("----- Ví dụ 2 -----")

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []
    def average(self):
        return sum(self.marks) / len(self.marks)

    @classmethod
    def go_to_school(cls):
        print("I'm going to school")
        print("I'm a {}." .format(cls))
    @staticmethod
    def go_to_school_static():
        print("I'm going to school static")
        
       

anna = Student("Anna","MIT")
rolf = Student("rols","ThangLong")


anna.marks = [3,4,5,6]

print(anna.average())
anna.go_to_school()
anna.go_to_school_static()
Student.go_to_school_static()
