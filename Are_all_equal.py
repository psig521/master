first = input("Введите число для сравнения: ")
second = input("Введите число для сравнения: ")
third = input("Введите число для сравнения: ")

if first == second == third:
    print("3")
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)
