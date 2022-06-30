n = int(input("Banyak angka dalam List : "))
list = []
for i in range(n):
    angka = int(input("angka = "))
    list.append(angka)

list.sort(reverse=True)

print(list[0])
print(list[1])
print(list[2])
