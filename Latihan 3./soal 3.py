gempa = float(input("kekuatan gempa (Magnitude) :"))
if (gempa < 2.0):
    print("Gempa tersebut adalah gempa jenis Micro")
elif (gempa < 3.0):
    print ("Gempa tersebut adalah gempa jenis Very minor")
elif (gempa < 4.0):
    print ("Gempa tersebut adalah gempa jenis Minor")
elif (gempa < 5.0):
    print ("Gempa tersebut adalah gempa jenis Light")
elif (gempa < 6.0):
    print ("Gempa tersebut adalah gempa jenis Moderate")
elif (gempa < 7.0):
    print ("Gempa tersebut adalah gempa jenis Strong")
elif (gempa < 8.0):
    print ("Gempa tersebut adalah gempa jenis Major")
elif (gempa < 10.0):
    print ("Gempa tersebut adalah gempa jenis Great")
else:
    print("Gempa tersebut adalah gempa jenis Meteoric")
