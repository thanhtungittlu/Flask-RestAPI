listGrages = [70, 77, 80, 95, 99, 100] #list có chỉ số, có thứ tự, có thể chỉnh sửa
tupleGrages = (70, 77, 80, 95, 99, 100,100) #tuple có chỉ số, có thứ tự, bất biến, không thể chỉnh sửa hay thay đổi, có thể trùng lặp
setGrages = {70, 77, 80, 95, 99, 100,100} #Set không cỏ chỉ số, không có thứ tự, không trùng lặp, có thể thay đổi
print(sum(listGrages)/len(listGrages))

listGrages.append(66)
# tupleGrages.append(33) sẽ xảy ra lỗi
print(tupleGrages[0])
print(tupleGrages)

###
singerTuples = (100,) # phải có dấu phẩy ở cuối
###
print("-------------")
your_lottery_numbers = {1,2,3,4,5}
winning_number = {1,3,5,7,9,11}

print( your_lottery_numbers.intersection(winning_number)) #Giao của 2 tập hợp
print( your_lottery_numbers.union(winning_number)) # Hợp của 2 tập hợp
print( your_lottery_numbers.difference(winning_number))
print( your_lottery_numbers.symmetric_difference(winning_number))

set1 = {14,5,9,21,12,77,67,8}
set2 = {5,77,9,12,34453,435345,22}
print(set1.intersection(set2))