#latihan No 4

GA      = 10000000
potA    = 0.025
gajiA   = GA * potA
persentaseA = "{:.1%}".format(potA)

GB      = 8500000
potB    = 0.02
gajiB   = GB * potB
persentaseB = "{:.1%}".format(potB)

GC      = 7000000
potC    = 0.015
gajiC   = GC * potC
persentaseC = "{:.1%}".format(potC)

GD      = 5500000
potD    = 0.01
gajiD   = GD * potD
persentaseD = "{:.1%}".format(potD)


KodeK   = input("silakan masukkan kode karyawan :")
NamaK   = input("silakan masukkan nama karyawan :")
GK      = input("silakan masukkan golongan karyawan :")

if ( GK == 'A') :
    print ("=============================================")
    print ("STRUK GAJI KARYAWAN")
    print ("_____________________________________________")
    print ("Nama Karyawan             :", NamaK, "(Kode :", KodeK, ")")
    print ("GOLONGAN                  :", GK)
    print ("_____________________________________________")
    print ("GAJI POKOK                : Rp", GA)
    print ("POTONGAN (",persentaseA,")         : Rp", gajiA)
    print ("Gaji Bersih               : Rp", GA - gajiA)

if ( GK == 'B') :
    print ("=============================================")
    print ("STRUK GAJI KARYAWAN")
    print ("_____________________________________________")
    print ("Nama Karyawan             :", NamaK, "(Kode :", KodeK, ")")
    print ("GOLONGAN                  :", GK)
    print ("_____________________________________________")
    print ("GAJI POKOK                : Rp", GB)
    print ("POTONGAN (",persentaseB,")         : Rp", gajiB)
    print ("Gaji Bersih               : Rp", GB - gajiB)

if ( GK == 'C') :
    print ("=============================================")
    print ("STRUK GAJI KARYAWAN")
    print ("_____________________________________________")
    print ("Nama Karyawan             :", NamaK, "(Kode :", KodeK, ")")
    print ("GOLONGAN                  :", GK)
    print ("_____________________________________________")
    print ("GAJI POKOK                : Rp", GC)
    print ("POTONGAN (",persentaseC,")         : Rp", gajiC)
    print ("Gaji Bersih               : Rp", GC - gajiC)

if ( GK == 'D') :
    print ("=============================================")
    print ("STRUK GAJI KARYAWAN")
    print ("_____________________________________________")
    print ("Nama Karyawan             :", NamaK, "(Kode :", KodeK, ")")
    print ("GOLONGAN                  :", GK)
    print ("_____________________________________________")
    print ("GAJI POKOK                : Rp", GD)
    print ("POTONGAN (",persentaseD,")         : Rp", gajiD)
    print ("Gaji Bersih               : Rp", GD - gajiD)


else:
    print("\n")
    print("_______________TERIMA KASIH_________________")
