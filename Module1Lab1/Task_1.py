numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

num_1 = numbers[0:4]
num_2 = numbers[5:21]
len_ = len(numbers)
numbers[4] = (sum(num_1) + sum(num_2)) / len_
print("Измененный список:", numbers)
