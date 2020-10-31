#nomor5

from random import randint
bilanganTebak = randint (0,100)

print("hallo... nama saya mr. compi :)")
print("saya telah memilih bilangan bulat secara acak dari 0-100")
print("silakan tebak ya!")

while True :
     BilAnda = int ( input("Silakan masukkan tebakkan Anda :"))

     if (BilAnda>0) and (BilAnda< bilanganTebak):
          print ("Hayooo, Kurang tepat, bilangan anda terlalu kecil :( ")
     elif(BilAnda<100) and (BilAnda>bilanganTebak):
          print("Yahhh.. masih salah nihh, bilangan anda terlalu besar :( ")
          continue
     elif(BilAnda == bilanganTebak ):
          print("Selamat tebakan anda tepat :>")
          break
     else:
          print("Ingat ya, bilangan bulat dari 0-100 :D ")
          continue
