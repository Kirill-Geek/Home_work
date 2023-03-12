"""
Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они 
сделали S журавликов. Сколько журавликов сделал каждый ребенок, 
если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
k = 2 * (x + x) | k = 2 * 2x | k = 4x
sum = k + x + x | sum = 4x + x + x | sum = 6x | x = sum / 6


*Пример: *

6 -> 1  4  1
24 -> 4  16  4
60 -> 10  40  10
"""

sum_val = int(input("Введите количество журавликов "))
petya_count = sum_val // 6
cerg_count = petya_count
katya_count = 2 * (petya_count + cerg_count)
if (katya_count + cerg_count + petya_count == sum_val):
    print(f"Петя сделал = {petya_count} журавликов")
    print(f"Сережа сделал = {cerg_count} журавликов")
    print(f"Катя сделала = {katya_count} журавликов")
else:
    rest = sum_val - katya_count - cerg_count - petya_count
    print(f"Петя сделал = {petya_count} журавликов")
    print(f"Сережа сделал = {cerg_count} журавликов")
    print(f"Катя сделала = {katya_count + rest} журавликов")
