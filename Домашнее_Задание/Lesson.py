# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример: *

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) 

val_char = int(input("Введите трехзначное число "))
sum_char = 0
while val_char > 0 :
    sum_char += val_char % 10
    val_char //= 10 
print(f"{sum_char}")
