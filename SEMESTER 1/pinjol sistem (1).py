#tampilan loby
print("-----------SISTEM PINJOL MAHABARATA-----------")
print("Selamat datang disistem pinjol mahabarata")
nama = input("masuakan nama anda: ").upper()
pekerjaan = input("masukan pekerjaan tetap anda: ").upper()
pendapatan = int(input("masukan nominal angka pendapatan perbulan anda: "))

#sistem kerja pinjaman
if pendapatan >= 5000000:
    print("jaminan yang dapat diterima: ")
    print("1.BPKB Mobil")
    print("2.Sertifikat Tanah / Rumah")
    print("3.Sertifikat Ruko")
    jaminan = input("masukan nomor jaminan yang anda pilih: ")

    if jaminan == "1":
        keputusan = "anda berhak mendaatkan pinjaman sejumlah Rp 50.000.000"
    elif jaminan == "2":
        keputusan = "anda berhak mendaatkan pinjaman sejumlah Rp 100.000.000"
    elif jaminan == "3":
        keputusan = "anda berhak mendaatkan pinjaman sejumlah Rp 200.000.000"
    else:
        keputusan = "jaminan tidak dapat diterima"

elif pendapatan >= 4000000:
    print("jaminan yang dapat diterima:")
    print("1.Sertifikat Tanah / Rumah")
    print("2.Sertifikat RUKO")
    jaminan = input("masukan nomor jamianan yang anda pilih: ")

    if jaminan == "1":
        keputusan = "anda berhak mendaatkan pinjaman sejumlah Rp 80.000.000"
    elif jaminan == "2":
        keputasan = "anda berhak mendaatkan pinjaman sejumlah Rp 120.000.000"
    else:
        keputusan = "jamianan tidak dapat diterima"

else:
    keputusan = "pendapatan anda belum memenuhi persyaratan"

#tampilan akhir
print("========INFO KEPUTUSAN PEMINJAMAN========")
print(f"NAMA PELANGGAN : {nama}")
print(f"PEKERJAAN : {pekerjaan}")
print(f"PENDAPATAN PERBULAN : {pendapatan}")
print(f"KEPUTUSAN PINJAMAN : {keputusan}")

print("----------TERIMA KASIH TELAH MELAKUKAN TRANSAKSI PINJAMAN DI PINJOL MAHABARATA----------")