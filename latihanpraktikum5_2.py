#Latihan praktikum 1

#No. 2

#syarat kelulusan
#Tidak ada nilai yang kurang dari 60
#Nilai matematikanya harus di atas 70
#range tidak diantara nilai 1-100




import sys
print("status kelulusan siswa")
nilaibasindo = a = int(input ("masukkan nilai bahasa Indonesia :"))
nilaiipa = b = int(input ("masukkan nilai ipa :"))
nilaimatematika = c = int(input ("masukkan nilai matematika :"))

if (a<0 or a>100) or (b<0 or b>100) or (c<0 or c>100):
    print ("Maaf, nilai yang anda masukkad tidak valid")
    sys.exit()

elif (c>70 and c<=100) & (b>60 and b<=100) & (a>60 and a<=100):
    print ("LULUS")
elif (c<70 and c>=0) or (b<60 and b>=0) or (a<60 and a>=0):
    print (" TIDAK LULUS")
