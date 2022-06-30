n = int(input("Banyak angka dalam List : "))
list = []
for i in range(n):
    angka = int(input("angka = "))
    list.append(angka)

list.sort()

print(list[1])
print(list[2])
print(list[3])
