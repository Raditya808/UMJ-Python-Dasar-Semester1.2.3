# Program Konversi Mata Uang sederhana

#Nilai tukar (ubah sesuai kebutuhan)
nilai_tukar =15000 # Contoh: 1 USD = 15000 IDR


print("Pilih Opsi Konversi:")
print("1. RP KE USD")
print("2.USD KE RP")

pilihan = input("Masukan Pilihan (1/2): ")

if pilihan == "1":
    rp = float(input("Masukan jumlah dalam rupiah (Rp): "))
    usd = rp / nilai_tukar
    print(f"{rp}) Rupiah sama dengan {usd:.2f} Dolar amerika.")
elif pilihan == "2":
    usd = float(input("Masukan jumlah dalam Amerika (USD): "))
    rp = usd * nilai_tukar
    print(f"{usd} Dolar Amerika sama dengan {rp:.2f} Rupiah,")
else:
    print("Pilihan tidak valid,")


