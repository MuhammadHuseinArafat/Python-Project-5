#Praktikum 2

#nomor 3

i = 0
while (i<10):
    print('hello world')
    i += 1

#nomor 5

i = 2
while (i <=20):
    print('Hello world')
    i += 2

#nomor 6
 i = 0
while True:
    print('Hello world')
    i += 1
    if (i == 10):
        break

#nomor  8   
    
#kotak bintang ajaib
kolom = 5
baris = 5

i = 0
while (i<baris):
    j=0
    while (j<kolom):
        print ('*', end='')
        j += 1
    print('')
    i += 1

#nomor 10

i=0

while (i<5):
    i += 1
    print ('*' * i)

#nomor 11

from random import randint
while True:
    bil = randint(0,10)
    print(bil)
    if bil == 5:
        break
#nomor 13

i=0
from random import randint
while True:
    bil = randint(0,10)
    i += 1
    print(bil)
    if bil == 5:
        print ("jumlah perulangan =", i)
        break
    
  
