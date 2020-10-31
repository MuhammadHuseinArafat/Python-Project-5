#Latihan praktikum 1

#No. 3

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
    print ("Maaf, nilai yang anda masukkan tidak valid")
    sys.exit()

elif (c>70 and c<=100) & (b>60 and b<=100) & (a>60 and a<=100):
    print ("LULUS")
elif (c<70 and c>=0) or (b<60 and b>=0) or (a<60 and a>=0):
    print (" TIDAK LULUS")
    print (" Sebab :")

if (c<70 and c>0):
    print ("- Nilai matematika harus lebih dari 70")
if (a<60 and a>0):
    print ("- Nilai bahasa indonesia harus lebih dari 60")
if (b<60 and b>0):
    print ("- Nilai IPA kurang dari 60")
    


    
