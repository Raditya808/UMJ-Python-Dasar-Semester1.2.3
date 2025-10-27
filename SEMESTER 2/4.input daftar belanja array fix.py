# python
pilihan1 = []
pilihan2 = []
pilihan3 = []
pilihan4 = []
kembalian = []


print("masukan nama produk")

barang1 = input("Pilih produk belanjaan anda (kelompok 1): ")
harga1 = input("Masukkan harga produk (kelompok 1): ")
pilihan1.append((barang1, harga1))

barang2 = input("Pilih produk belanjaan anda (kelompok 2): ")
harga2 = input("Masukkan harga produk (kelompok 2): ")
pilihan2.append((barang2, harga2))

barang3 = input("Pilih produk belanjaan anda (kelompok 3): ")
harga3 = input("Masukkan harga produk (kelompok 3): ")
pilihan3.append((barang3, harga3))

barang4 = input("Pilih produk belanjaan anda (kelompok 4): ")
harga4 = input("Masukkan harga produk (kelompok 4): ")
pilihan4.append((barang4, harga4))

print("hasil belanjaan anda")
for i in pilihan1:
    print(f"Kelompok 1: {i[0]},  Harga: {i[1]}")
for i in pilihan2:
    print(f"Kelompok 2: {i[0]}, Harga: {i[1]}")
for i in pilihan3:
    print(f"Kelompok 3: {i[0]}, Harga: {i[1]}")
for i in pilihan4:
    print(f"Kelompok 4: {i[0]}, Harga: {i[1]}")






