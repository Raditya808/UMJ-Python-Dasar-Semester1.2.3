# menghitung persen dalam python

jumlah_belanja = float(input("Masukkan jumlah belanja: "))

 #Menentukan diskon berdasarkan total belanja
if jumlah_belanja >= 500000:
    diskon = 20  # 20%
elif jumlah_belanja >= 200000:
    diskon = 10  # 10%
else:
    diskon = 5   # 5%

# Menghitung harga setelah diskon
potongan = (diskon / 100) * jumlah_belanja
harga_setelah_diskon = jumlah_belanja - potongan

# Menampilkan hasil
print(f"Diskon: {diskon}%")
print(f"Total yang harus dibayar: Rp{harga_setelah_diskon:,.2f}")
