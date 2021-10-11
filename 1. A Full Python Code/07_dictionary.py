my_dict = {"name": "Tung", "Age": 22}

another_dict = { 1: 15, 2:75, 3:150}

lottery_players = [
    {
    "name": "Tung",
    "numbers": (13,45,67,58,90)
    },
    {
    "name": "Nam",
    "numbers": (1,4,6,5,0)
    },
    {
    "name": "Duc",
    "numbers": (3,5,7,38,95)
    },
]

print(sum(lottery_players[0]["numbers"]))
universities = [
    { 
        "name": "ThangLong",
        "address": "Nguyen Xien"
    },
    { 
        "name": "Ngoai Thuong",
        "address": "Chua lang"
    },
]

########

# lottery_players[0].total() học Oop để biết điều tiếp theo

print("------- Ex --------")
students = {
    "name": "Jose",
    "school": "Computing",
    "grades": (66,77,88)
}

def average_grade(data):
    grades = data["grades"]
    return sum(grades) / len(grades)

def average_grade_all_students(student_list):
    total = 0
    count = 0
    for student in student_list:
        total += sum(student["grades"])
        count += len(student["grades"])
    return total/count
print(average_grade(students))