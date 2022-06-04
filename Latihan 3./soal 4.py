gelombang = float(input("Panjang gelombang cahaya (nm) :"))
if (380 <= gelombang < 450):
    print("Spektrum yang terlihat adalah violet")
elif (450 <= gelombang < 495):
    print ("Spektrum yang terlihat adalah Blue")
elif (495 <= gelombang < 570):
    print ("Spektrum yang terlihat adalah Green")
elif (570 <= gelombang < 590):
    print ("Spektrum yang terlihat adalah Yellow")
elif (590 <= gelombang < 620):
    print ("Spektrum yang terlihat adalah Orange")
elif (620 <= gelombang <= 750):
    print ("Spektrum yang terlihat adalah Red")
else:
    print("Input kamu diluar spektrum yang di ketahui !!")
    
