tahun = int(input("Masukan tahun :"))
if ( tahun%400 == 0):
    print("tahun",tahun,"adalah tahun kabisat")
elif (tahun%100 ==0):
    print("tahun",tahun, "bukan tahun kabisat")
elif (tahun%4 == 0):
    print("tahun",tahun,"adalah tahun kabisat")
else :
    print("tahun",tahun, "bukan tahun kabisat")
