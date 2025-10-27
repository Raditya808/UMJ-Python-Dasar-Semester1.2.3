harga_awal = int(input("masukan harga awal:"))

input_harga = harga_awal * harga_awal
harga_awal = harga_awal * harga_awal
print(f"harga awal ={harga_awal}")

harga_awal = float(input("masukan harga awal:"))

input_harga = harga_awal * harga_awal
harga_awal = harga_awal * harga_awal
print(f"harga awal ={harga_awal}")


belanja = float(input("Masukkan total belanja: "))
diskon = 20  # Diskon dalam persen

# Menghitung jumlah diskon
jumlah_diskon = (diskon / 100) * belanja

# Menghitung harga setelah diskon
harga_setelah_diskon = belanja - jumlah_diskon

# Menampilkan hasil
print(f"Diskon = {diskon}%")
print(f"Potongan harga = {jumlah_diskon:,.2f}")
print(f"Total setelah diskon = {harga_setelah_diskon:,.2f}")

