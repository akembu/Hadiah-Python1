print("## Program Python Menghitung Gaji Karyawan ##")
print("=============================================")
print("")

x = (input("Nama Karyawan : "))
y = (input("Golongan : "))
z = int(input("Jumlah Jam Kerja : "))


if y == "A":
    upah = 5000
elif y == "B":
    upah = 7000
elif y == "C":
    upah = 8000
elif y == "D":
    upah = 10000
else:
    upah = 0
    print ("Maaf, tidak ada golongan tersebut")

if 1 <= z <= 48:
    total = z * upah
elif z > 48:
    uanglembur = (z-48)*4000
    total = (48*upah)+uanglembur
else:
    print("Jumlah Jam Kerja tidak Valid")

print("{} Menerima Upah Rp. {} per minggu".format(x, total))