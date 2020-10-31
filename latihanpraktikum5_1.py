#Latihan praktikum 1

#No. 1

#syarat kelulusan
#Tidak ada nilai yang kurang dari 60
#Nilai matematikanya harus di atas 70
#range  nilai 1-100

print("status kelulusan siswa")
nilaibasindo = a = int(input ("masukkan nilai bahasa Indonesia :"))
nilaiipa = b = int(input ("masukkan nilai ipa :"))
nilaimatematika = c = int(input ("masukkan nilai matematika :"))



if (a>60):
     if (b>60):
         if(c>70) :
              print ("LULUS")

else: 
    print ("TIDAK LULUS")
