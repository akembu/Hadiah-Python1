print("## Program Python Diskon Potongan Harga ##")
print("==========================================")
print("")

x = int(input("Total Belanja : Rp. "))


if x < 100000:
    print("Maaf, anda tidak mendapatan diskon")
elif 100000 <= x < 500000:
    diskon = 0.1
    print ("Selamat, anda mendapat diskon 10%")
elif 500000 <= x <= 1000000:
    diskon = 0.2
    print ("Selamat, anda mendapat diskon 20%")
else:
    diskon = 0.3
    print ("Selamat, anda mendapat diskon 30%")

hasdis = x * diskon
totbay = x - hasdis
print("Total Bayar : Rp. {}".format(totbay))