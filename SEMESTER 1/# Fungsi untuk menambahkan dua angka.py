# Harga per malam berdasarkan jenis kamar
harga_standard = 300000
harga_deluxe = 500000
harga_suite = 1000000

# Input data pelanggan
jenis_kamar = input("Masukkan jenis kamar (Standard, Deluxe, Suite): ")
lama_menginap = int(input("Masukkan lama menginap (dalam malam): "))
pelanggaran = input("Apakah ada pelanggaran (merokok, menurunkan kasur, merusak perabotan)? (ya/tidak): ").lower()

if jenis_kamar == "Standard":
    harga_permalam = harga_standard
elif jenis_kamar == "Deluxe":
    harga_permalam = harga_standard
elif jenis_kamar == "Suite":
    harga_permalam = harga_suite
else:
    print("jenis kamar tidak valid!")
    harga_permalam = 0

if harga_permalam > 0:
    total_harga = harga_permalam * lama_menginap
    diskon = 0.25
    if lama_menginap > 7:
        diskon = 0.25
    elif lama_menginap >= 4:
        diskon = 0.15
    else:
        diskon = 0
    total_harga -= total_harga * diskon 
    if jenis_kamar == "suite" and lama_menginap > 5:
        total_harga -= total_harga * 0.05  # Tambahan diskon 5%

    # Biaya tambahan jika ada pelanggaran
    if pelanggaran == "ya":
        total_biaya_pelanggaran = 0
        pelanggaran_jenis = input("Masukkan jenis pelanggaran (merokok, menurunkan kasur, kasur, tv, seprei, selimut, bantal, handuk) atau 'selesai' untuk selesai: ").lower()

        # Biaya pelanggaran sesuai dengan input
        if pelanggaran_jenis == "merokok":
            total_biaya_pelanggaran += 1000000
        elif pelanggaran_jenis == "menurunkan kasur":
            total_biaya_pelanggaran += 500000
        elif pelanggaran_jenis == "kasur":
            total_biaya_pelanggaran += 15000000
        elif pelanggaran_jenis == "tv":
            total_biaya_pelanggaran += 5000000
        elif pelanggaran_jenis == "seprei":
            total_biaya_pelanggaran += 1000000
        elif pelanggaran_jenis == "selimut":
            total_biaya_pelanggaran += 1000000
        elif pelanggaran_jenis == "bantal":
            total_biaya_pelanggaran += 500000
        elif pelanggaran_jenis == "handuk":
            total_biaya_pelanggaran += 500000
        
        # Menambahkan biaya pelanggaran ke total harga
        total_harga += total_biaya_pelanggaran

    # Menampilkan hasil akhir
    print(f"Total pembayaran yang harus dibayar: Rp {total_harga:,.0f}")