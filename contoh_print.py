def kalikan(angka_local, pengali=5):
    angka_local = angka_local * pengali
    return angka_local


# angka_global = 10
pengali = 2
list_angka_global = [10, 20, 30]

# var = kalikan(list_angka_global)

lambda y: y * 5

print(list(map(lambda x: x * pengali, list_angka_global)))


# print("print hasil", var)
