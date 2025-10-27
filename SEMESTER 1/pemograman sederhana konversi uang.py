nilai_tukar=15000
print("pilih opsi konversi")
print("1 usd = 1 rupiah")
print("2 usd = 2 rupiah")

pilih = input("masukan piliham mata uang 1/2: " )

if pilih == "1":
    rp = float(input("Masukan jumlah dalam rupiah (Rp): "))
    usd = rp / nilai_tukar
    print(f"{rp}) Rupiah sama dengan {usd:.2f} Dolar amerika.")
elif "2" == pilih:
    usd = float(input("Masukan jumlah dalam Amerika (USD): "))
    rp = usd * nilai_tukar
    print(f"{usd} Dolar Amerika sama dengan {rp:.2f} Rupiah,")
else:
    print("Pilihan tidak valid,")