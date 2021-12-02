awal = int(input("Masukan awal deret : "))
akhir = int(input("Masukan akhir deret : "))

for i in range (awal, akhir):
    if (i % 2 == 0) and (i % 5 != 0) and (i % 9 != 0):
        print (i, " ", end="")