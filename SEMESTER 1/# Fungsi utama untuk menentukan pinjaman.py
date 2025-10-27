# Fungsi utama untuk menentukan pinjaman
def cek_pinjaman():
    # Input pekerjaan tetap
    pekerjaan_tetap = input("Apakah Anda memiliki pekerjaan tetap? (Ya/Tidak): ").strip().lower()
    
    # Input pendapatan per bulan
    pendapatan = int(input("Berapa pendapatan per bulan Anda? (dalam Rp): "))
    
    # Input jenis jaminan
    jaminan = input("Jenis jaminan yang diberikan (BPKB Mobil, Sertifikat Tanah/Rumah, Sertifikat RUKO): ").strip()
    
    # Mengecek apakah pelanggan memenuhi syarat pekerjaan tetap
    if pekerjaan_tetap != "ya":
        print("Tidak memenuhi syarat pekerjaan tetap.")
    
    # Mengecek apakah pendapatan cukup untuk mengajukan pinjaman
    elif pendapatan < 4000000:
        print("Tidak dapat melakukan peminjaman.")
    
    # Jika pendapatan >= Rp 4.000.000
    elif pendapatan >= 4000000:
        # Jika pendapatan >= Rp 5.000.000
        if pendapatan >= 5000000:
            if jaminan == "BPKB Mobil":
                print("Dapat pinjam Rp 50.000.000")
            elif jaminan == "Sertifikat Tanah/Rumah":
                print("Dapat pinjam Rp 100.000.000")
            elif jaminan == "Sertifikat RUKO":
                print("Dapat pinjam Rp 200.000.000")
            else:
                print("Jaminan tidak diterima.")
        
 # Jika pendapatan >= Rp 4.000.000 dan < Rp 5.000.000
        elif pendapatan >= 4000000:
            if jaminan == "Sertifikat Tanah/Rumah":
                print("Dapat pinjam Rp 80.000.000")
            elif jaminan == "Sertifikat RUKO":
                print("Dapat pinjam Rp 120.000.000")
            else:
                print("Jaminan tidak diterima.")
                       
# Memanggil fungsi utama
cek_pinjaman()
