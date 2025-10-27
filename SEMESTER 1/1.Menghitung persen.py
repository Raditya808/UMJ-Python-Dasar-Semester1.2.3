print("0====================================================0")
Nama = input("Masukan Nama Anda:")
total_belanja = float(input("masukan total belanja Rp:"))
if total_belanja < 0:
    print("total belanja tidak boleh negatif")
else:
    if total_belanja < 100000:
        diskon = 0
    elif 100000 <= total_belanja <=499999:
        diskon = 0.10
    else:
        diskon = 0.20

    total_diskon = total_belanja * diskon
    total_bayar = total_belanja - total_diskon

    print(f"Nama ={Nama}")
    print(f"Total Belanja: Rp{total_belanja:,.0f}")
    print(f"Diskon: Rp{total_diskon:,.0f}")
    print(f"Total Bayar: Rp{total_bayar:,.0f}")
print("0====================================================0")