print("Program Menghitung kalori yang terbakar berdasarkan langkah kaki")
berat_badan = float(input("Masukkan berat badan (kg): "))
jumlah_langkah = int(input("Masukkan jumlah langkah kaki: "))

kalori_per_langkah = berat_badan * 0.00057
total_kalori = jumlah_langkah * kalori_per_langkah

print("======================================")
print("Jumlah kalori yang terbakar berdasarkan langkah kaki")
print(f"Berat badan Anda adalah: {berat_badan} kg")
print(f"jumlah langkah kaki yang diambil adalah: {jumlah_langkah} langkah")
print("Langkah kaki yang diambil adalah:", jumlah_langkah)
print("Jumlah kalori yang terbakar adalah:", total_kalori, "kalori")
print("Diatas adalah hasil perhitungan kalori yang terbakar berdasarkan langkah kaki")
print("======================================")
