immutable_var = 1, "Hi", True, 2
print(immutable_var)
#immutable_var[1] = 5
#не измениться по тому, что элементы кортежа нельзя изменить
mutable_list = [1, "Hi", True, 5]
mutable_list[1] = 'Buy'
print(mutable_list)