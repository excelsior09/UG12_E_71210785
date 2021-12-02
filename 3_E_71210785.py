angka = int(input("Masukkan Angka : "));
limit = angka;
for i in range (0,angka):
    for j in range (-2, limit+1):
        print(" ",end="")

    for k in range (0,i+1):
        print("* ",end="")
    limit -= 1
    print("")

limit = angka;
for i in range (1, angka):
    for j in range (-4, i):
        print(" ",end="")

    for k in range (1, limit):
        print("* ",end="")
    limit -= 1
    print("")