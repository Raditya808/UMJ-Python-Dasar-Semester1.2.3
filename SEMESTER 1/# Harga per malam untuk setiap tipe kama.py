def hitung_total(harga_kamar, jenis_kamar, lama_menginap):
    diskon = 0
    
    # Mengecek kondisi untuk diskon 5% menggunakan if-else-elif
    if jenis_kamar.lower() == "suite" and lama_menginap > 5:
        diskon = 0.05  # 5% diskon
    elif jenis_kamar.lower() == "suite" and lama_menginap <= 5:
        diskon = 0  # Tidak ada diskon jika lama menginap 5 malam atau kurang
    else:
        diskon = 0  # Tidak ada diskon jika bukan jenis kamar Suite
    
    total_harga = harga_kamar * lama_menginap
    total_harga_setelah_diskon = total_harga * (1 - diskon)
    
    return total_harga_setelah_diskon

# Contoh penggunaan
harga_kamar = 1000  # Harga per malam
jenis_kamar = "Suite"  # Jenis kamar
lama_menginap = 6  # Lama menginap dalam malam

total = hitung_total(harga_kamar, jenis_kamar, lama_menginap)
print(f"Total harga setelah diskon: {total}")
