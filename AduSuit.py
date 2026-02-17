import random

print ("\n ==================================================================")
print (" Selamat Datang Pada Game Gunting Batu Kertas 👋👋")
print (" Kamu Akan Melawan Mesin Dan Lihat Apakah Kamu Akan Menang! 😁")
print (" ================================================================== \n")
skor_pemain = 0
skor_mesin = 0
while True:
    
    kemungkinan = ["gunting","batu","kertas"]
    pilihan_pemain = input(" masukkan pilihan kamu (gunting / batu / kertas): ")
    pilihan_mesin = random.choice(kemungkinan)
    print (f" \n pilihan kamu {pilihan_pemain}, dan pilihan mesin {pilihan_mesin} \n ")

    if pilihan_pemain == pilihan_mesin:
        print(f" Kedua Pemain sama-sama memilih {pilihan_pemain}. kalian seri💪")
        skor_mesin += 1
        skor_pemain += 1
    elif pilihan_pemain == "gunting":
        if pilihan_mesin == "kertas":
            print(" gunting mengalahkan kertas, kamu menang!😁")
            skor_pemain += 1
        else:
            print(" batu mengalahkan gunting, kamu kalah!😅")
            skor_mesin += 1
    elif pilihan_pemain == "batu":
        if pilihan_mesin == "gunting":
            print(" batu mengalahkan gunting, kamu menang!😁")
            skor_pemain += 1
        else:
            print(" kertas mengalahkan batu, kamu kalah!😅")
            skor_mesin += 1
    elif pilihan_pemain == "kertas":
        if pilihan_mesin == "batu":
            print(" kertas mengalahkan batu, kamu menang!😁")
            skor_pemain += 1
        else:
            print(" gunting mengalahkan kertas, kamu kalah!😅")
            skor_mesin += 1

    main_lagi = input(" \n mau main lagi? (y/n):")
    if main_lagi.lower() != "y":
        print("\n terimakasih sudah bermain. kapan kapan coba lagi ya 👋👋👋")
        print(f"\n skor kamu : {skor_pemain} skor mesin : {skor_mesin}")
        if skor_pemain > skor_mesin:
            print("\n selamat kamu menang!")
        else:
            print("\n yah kamu kalah, jangan patah semangat yuk coba lagi! ")
        break

    