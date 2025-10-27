masukan_nama_anda = input("masukan nama:").lower()
kamar = input("Pilih jenis kamar standard, deluxe, suite:").lower()
harga = int(input("Masukkan harga kamar: "))
lama_inap = int(input("Masukkan lama inap (dalam malam):"))
if kamar == "standard":
    if harga == 300000:
        if lama_inap >= 7:
            print("Anda berhak menerima diskon 25%")
        elif lama_inap <= 4:
            print("Maaf, tidak ada diskon untuk menginap kurang dari 4 malam")
        else:
            print("Anda memasukkan jumlah malam inap yang tidak sesuai.")

elif kamar == "deluxe":
    if harga == 500000:
        if lama_inap >= 7:
            print("Anda mendapatkan diskon 25%")
        elif lama_inap <= 4:
            print("Maaf, tidak ada diskon untuk menginap kurang dari 4 malam")
        else:
            print("Anda memasukkan jumlah malam inap yang tidak sesuai.")

elif kamar == "suite":
    if harga == 1000000:
        if lama_inap >= 7:
            print("Anda berhak mendapatkan diskon 25%")
        elif lama_inap <= 4:
            print("Tidak ada diskon untuk menginap kurang dari 4 malam")
        elif lama_inap >= 5:
            print("Anda berhak mendapatkan diskon 5%")
        else:
            print("Anda memasukkan jumlah malam inap yang tidak sesuai.")
else:
    print("Jenis kamar yang Anda masukkan tidak valid.")