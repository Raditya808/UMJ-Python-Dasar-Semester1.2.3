#input informasi jabatan apakah memiliki pinjaman
jabatan = input("manager,ass manager,supervisor,kepala gudang,sales lapangan,sales kantor:")
manager = 10000000 + 2000000
ass_manager = 8000000 + 1000000
supervisor  = 5000000 + 1000000
kepala_gudang = 4500000 + 1000000
sales_lapangan = 2000000
sales_kantor = 1500000  
potongan_pinjaman = 500000

if jabatan == "manager":
    pinjaman = input("apakah jabatan tersebut memiliki pinjaman (ya/tidak) : ")
    if pinjaman == "ya":
        gabungan = manager - potongan_pinjaman
    else:
        gabungan = manager
    print("gaji total jabatan anda sebesar : Rp.", gabungan)

elif jabatan == "ass manager":
    pinjaman = input("apakah jabatan tersebut memiliki pinjaman (ya/tidak) : ")
    if pinjaman == "ya":
        gabungan = ass_manager - potongan_pinjaman
    else:
        gabungan = ass_manager
    print("gaji total jabatan anda sebesar : Rp.", gabungan)

elif jabatan == "supervisor":
    pinjaman = input("apakah jabatan tersebut memiliki pinjaman (ya/tidak) : ")
    if pinjaman == "ya":
        gabungan = supervisor - potongan_pinjaman
    else:
        gabungan = supervisor
    print("gaji total jabatan anda sebesar : Rp.", gabungan )

elif jabatan == "kepala gudang":
  pinjaman = input("apakah jabatan tersebut memiliki pinjaman (ya/tidak) : ")
  if pinjaman == "ya":
    gabungan = kepala_gudang - potongan_pinjaman
  else:
    gabungan = kepala_gudang
  print("gaji total jabatan anda sebesar : Rp.", gabungan)

elif jabatan == "sales lapangan":
  pinjaman = input("apakah jabatan tersebut memiliki pinjaman (ya/tidak) : ")
  if pinjaman == "ya":
    gabungan = sales_lapangan - potongan_pinjaman
  else:
    gabungan = sales_lapangan

  penjualan = int(input("Masukkan jumlah barang yang dijual: "))
  insentif = 0
  if penjualan >= 100:
           insentif = 2500000
  elif penjualan >= 50:
           insentif = 1500000
  elif penjualan >= 30:
           insentif = 700000
  else:
      print("penjualan tidak memenuhi target")
  print("gaji total jabatan anda sebesar : Rp.", gabungan + insentif)

elif jabatan == "sales kantor":
  pinjaman = input("apakah jabatan tersebut memiliki pinjaman (ya/tidak) : ")
  if pinjaman == "ya":
    gabungan = sales_kantor - potongan_pinjaman
  else:
    gabungan = sales_kantor
  print("gaji total jabatan anda sebesar : Rp.", gabungan)