print('Все ли числа равны')
first = int(input('1 число: '))
second = int(input('2 число: '))
third = int(input('3 число: '))
print('Одинаковые числа')
if first == second and first == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)
