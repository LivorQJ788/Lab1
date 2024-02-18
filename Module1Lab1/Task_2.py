# TODO Найдите количество книг, которое можно разместить на дискете
size_ = 4
symbols = 25
pages = 50
strs = 100
book = size_ * symbols * pages * strs
disk = 1.44 * 1024**2
count_of_book = int(disk//book)

print("Количество книг, помещающихся на дискету:", count_of_book)
