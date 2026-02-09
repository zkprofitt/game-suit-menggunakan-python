import random

print ("\n ==================================================================")
print (" Selamat Datang Pada Game Gunting Batu Kertas 👋👋")
print (" Kamu Akan Melawan Mesin Dan Lihat Apakah Kamu Akan Menang! 😁")
print (" ================================================================== \n")

while True:
    kemungkinan = ["gunting","batu","kertas"]
    pilihan_pemain = input(" masukkan pilihan kamu (gunting / batu / kertas): ")
    pilihan_mesin = random.choice(kemungkinan)
    print (f" \n pilihan kamu {pilihan_pemain}, dan pilihan mesin {pilihan_mesin} \n ")

