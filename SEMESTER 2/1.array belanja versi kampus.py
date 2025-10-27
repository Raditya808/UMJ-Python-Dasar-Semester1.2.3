belanja = []

batas= int(input("Masukkan batas belanja: "))

for i in range(batas):
    barang = input(f"Masukkan nama barang ke - {i+1}: ")
    belanja.append(barang)


print()
print("--daftar belanja--")
for i in range(batas):
    print(f"Barang ke - {i+1}: {belanja[i]}")