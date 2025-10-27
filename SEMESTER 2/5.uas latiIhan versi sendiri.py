
mahasiswa = []

batas = int(input("Masukkan jumlah mahasiswa: "))

for i in range(batas):
    nama = input("masukan nama mahasiswa: ")
    tugas = int(input("masukan nilai tugas: "))
    uts = int(input("masukan nilai uts: "))
    uas = int(input("masukan nilai uas: "))
    sikap = int(input("masukan nilai sikap: "))

    rata_rata = (tugas + uts + uas + sikap) / 4

    if rata_rata >= 80:
        print(f"Nilai {nama} adalah A")
    elif rata_rata >= 70:
        print(f"Nilai {nama} adalah B")
    elif rata_rata >= 60:
        print(f"Nilai {nama} adalah C")
    elif rata_rata >= 50:
        print(f"Nilai {nama} adalah D")
    else:
        print(f"Nilai {nama} adalah E")


    print(tugas)
    print(uts)
    print(uas)
    print(sikap)
    print(f"Rata-rata {nama}: {rata_rata}")

