my_list = [0,1,2,3,4]
an_equal_list = [x*2 for x in range(0,6,2)]
print(an_equal_list)

print([n for n in range(20) if n%2 == 0])

people_you_know = ["Rolf","John","Anna","  GreG"]
newList = [x.strip().lower() for x in people_you_know]
print(newList)