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

    if pilihan_pemain == pilihan_mesin:
        print(f" Kedua Pemain sama-sama memilih {pilihan_pemain}. kalian seri💪")
    elif pilihan_pemain == "gunting":
        if pilihan_mesin == "kertas":
            print(" gunting mengalahkan kertas, kamu menang!😁")
        else:
            print(" batu mengalahkan gunting, kamu kalah!😅")
    elif pilihan_pemain == "batu":
        if pilihan_mesin == "gunting":
            print(" batu mengalahkan gunting, kamu menang!😁")
        else:
            print(" kertas mengalahkan batu, kamu kalah!😅")
    elif pilihan_pemain == "kertas":
        if pilihan_mesin == "batu":
            print(" kertas mengalahkan batu, kamu menang!😁")
        else:
            print(" gunting mengalahkan kertas, kamu kalah!😅")

    main_lagi = input(" \n mau main lagi? (y/n):")
    if main_lagi.lower() != "y":
        print("\n terimakasih sudah bermain. kapan kapan coba lagi ya 👋👋👋")
        break

    