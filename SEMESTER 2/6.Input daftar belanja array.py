pilihan = []
pilihan2 = []
pilihan3 = []
pilihan4 = []
print("masukan nama produk")

barang1 = input("Pilih produk belanjaan anda (kelompok 1): ")
pilihan.append(barang1)
harga1 = input("Masukkan harga produk (kelompok 1): ")

barang2 = input("Pilih produk belanjaan anda (kelompok 2): ")
pilihan.append(barang2)
harga2 = input("Masukkan harga produk (kelompok 2): ")

barang3 = input("Pilih produk belanjaan anda (kelompok 3): ")
pilihan.append(barang3)
harga3 = input("Masukkan harga produk (kelompok 3): ")

barang4 = input("Pilih produk belanjaan anda (kelompok 4): ")
pilihan.append(barang4)
harga4 = input("Masukkan harga produk (kelompok 4): ")

print("hasil belanjaan anda")
for i in pilihan:
    print(f"Kelompok 1: {i[0]}")

for o in pilihan2:
    print(f"Kelompok 2: {o}")

for p in pilihan3:
    print(f"Kelompok 3: {p}")

for v in pilihan4:
    print(f"Kelompok 4: {v}")


print("Harga produk")
for i in harga1:
    print(f"Kelompok 1: {i}")

for i in harga2:
    print(f"Kelompok 2: {i}")

for i in harga3:
    print(f"Kelompok 3: {i}")

for i in harga4:
    print(f"Kelompok 4: {i}")
