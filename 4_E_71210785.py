def nilai_terbesar(daftar):
    nilai_besar = daftar[0]
    for nilai in daftar:
      if nilai > nilai_besar:
        nilai_besar = nilai
    return nilai_besar
def nilai_terkecil(daftar):
    nilai_kecil = daftar[0]
    for nilai in daftar:
      if nilai < nilai_kecil:
        nilai_kecil = nilai
    return nilai_kecil

a = [3, 20, 100, -35, 50]
b = [3, 20, 90, 35, 75]

print (a)
print ("nilai terbesar:", nilai_terbesar(a))
print ("nilai terkecil:", nilai_terkecil(a))

print ("")

print (b)
print ("nilai terbesar:", nilai_terbesar(b))
print ("nilai terkecil:", nilai_terkecil(b))