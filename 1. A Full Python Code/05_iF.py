should_continue = True
if should_continue:
    print("Hello")
know_people = ["John","Anna","Mary"]
person = input("Enter the person you know: ")
if person in know_people:
    print("You know {}!" .format(person))
else:
    print("You don't know {}!" .format(person))
print("-------------Ex-----------")
numbers = [1,2,3,4,5,6,7,8,9]
def even_numbers():
    evens = []
    for number in numbers:
        if number % 2 == 0:
            evens.append(number)
    return evens
print(even_numbers())
def user_menu(choice):
    if choice == "a":
        return "Add"
    elif choice == "q":
        return "Quit"
print(user_menu("a"))
print("-------Ex2-------")
def who_do_you_know():
    who_know = input("Nhập vào danh sách các tên: ")
    listKnow = [ x.strip() for x in who_know.split(",")]
    return listKnow
listKnow = who_do_you_know()
print(listKnow)
def ask_user():
    my_name = input("Nhập tên của bạn: ")
    if my_name in listKnow:
        print("Bạn có tên trong danh sách.")
    else:
        print("Bạn không có tên trong sanh sách")
ask_user()
