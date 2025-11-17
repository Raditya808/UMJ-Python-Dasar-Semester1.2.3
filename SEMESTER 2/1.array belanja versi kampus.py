belanja = []

batas= int(input("Masukkan batas belanja: "))

for i in range(batas):
    barang = input(f"Masukkan nama barang ke - {i+1}: ") # fungsi i + 1 yaitu penamaan data dimulai dari 1 dan bukan dari 0
    belanja.append(barang)


print()
print("--daftar belanja--")
for i in range(batas):
    print(f"Barang ke - {i+1}: {belanja[i]}")
