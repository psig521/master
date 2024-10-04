my_dict = {'User1': 1234, 'User2': 1111, "User3": 987645}
print(my_dict)
print(my_dict.get('User1'))
print(my_dict.get('User5'))
my_dict.update({'User4': 5546,
                "User5": 5497})
print(my_dict.pop('User1'))
print(my_dict)

my_set = {1, 9, 'Hi', True, 11.25, 1, 1, 11.25, 'Hi', 8, 9}
print(my_set)
my_set.add(5.55)
my_set.add("World")
my_set.discard(11.25)
print(my_set)
