#nomor 6
from random import randint
bilanganTebak = randint (0,100)
sum =0
print("hallo... nama saya mr. compi :D")
print("saya telah memilih bilangan bulat secara acak dari 0-100")
print("silakan tebak ya!:)")

while True :
     BilAnda = int ( input("Silakan masukkan tebakkan Anda :"))

     if (BilAnda>0) and (BilAnda< bilanganTebak):
          print ("Hayoo,  Kurang tepat, bilangan anda terlalu kecil :(")
          sum += 1
     elif(BilAnda<100) and (BilAnda>bilanganTebak):
          print("Yahhh.. masih salah nih, bilangan anda terlalu besar :) ")
          sum += 1
          continue
     elif(BilAnda == bilanganTebak):
          print("Selamat tebakan anda tepat :)")
          score = 100 - sum + 2
          if(score >0):
               print("score anda =",score)
          else:
               print ("yahh, maaf score anda nol, jangan bersedih, tetaplah semangat ya :)")
          break
     else:
          print("Ingat ya, bilangan  bulat dari 0-10, hehe ")
          continue
