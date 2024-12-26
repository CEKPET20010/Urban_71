immutable_var = 1, 2, 'a', 'b'
print(immutable_var)
#immutable_var[2] = 'b'
#print(immutable_var) # Изменить кортеж не получается. Пишет ошибку.
mutable_list = [1, 2, 'a', 'b', 'Modified']
print(mutable_list)
mutable_list[2] = 'b'
print(mutable_list)
