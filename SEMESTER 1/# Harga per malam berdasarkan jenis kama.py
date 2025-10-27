import os

total_denda = int(0)
kamar = input("Masukan jenis kamar (standard, deluxe, suite): ")
lama_inap = int(input("Masukan lama menginap (Dalam malam):"))

if kamar == 'standard':
    harga_per_malam = 300000
elif kamar == 'deluxe':
    harga_per_malam_malam = 500000
elif kamar == 'suite':
    harga_per_malam_malam = 1000000
else:
    print("Jenis kamar tidak valid.")
    harga_per_malam = 0
total_harga = harga_per_malam * lama_inap

if lama_inap > 7:
    diskon = 0.25 #diskon 25% jika lama menginap lebih dari 7 malam
elif lama_inap >=4:
    diskon = 0.15 #diskon 15% jika lama inap antara 4 sampai 7 
else:
    diskon = 0 

if kamar == 'suite':
    if lama_inap > 5:
        diskon += 0.05
harga_akhir = total_harga * (1-diskon)

merokok = input("Apakah anda merokok di dalam kamar (yes/no) : ")
if merokok == "yes" :
    merokok = True
    denda_merokok = 1000000
    total_denda += denda_merokok
else :
    merokok = False
    total_denda += 0

menurunkan_kasur = input("Apakah anda menurukan kasur (yes/no) : ")
if menurunkan_kasur == "yes" :
    denda_menurunkan_kasur = 500000
    total_denda += denda_menurunkan_kasur
    menurunkan_kasur = True
else :
    menurunkan_kasur = False

barang = {
    "kasur" : 15000000,
    "tv" : 5000000,
    "sprei" : 1000000,
    "selimut" : 1000000,
    "bantal" : 500000,
    "handuk" : 500000,
    "tidak_ada" : 0
}

list_barang_hilang = []

barang_hilang = input("Sebutkan barang hilang / rusak : kasur, tv, sprei, selimut, bantal, handuk, tidak_ada (tambahkan comma jika lebih dari 1 barang) = ")
list_barang_hilang = barang_hilang.split(',')


if len(list_barang_hilang) > 0:
   for x in list_barang_hilang :
       total_denda += barang[x]

if harga_per_malam > 0:
    os.system('cls') # clear console / terminal
    print(f"Harga total untuk menginap : {lama_inap} \nmalam di kamar : {kamar} \nadalah:Rp {harga_akhir:,.0f} ")


if harga_per_malam > 0 and total_denda > 0 :
      os.system("cls")
      harga_akhir += total_denda
      print(f"Harga total untuk menginap : {lama_inap} \nmalam di kamar : {kamar} ")
      print("\n")
      if  merokok == True :
        print(f"Denda merokok dikamar : {denda_merokok}")
      else :
        print(f"Denda merokok dikamar : {0}")
      if menurunkan_kasur == True :
        print(f"Denda menurunkan kasur : {denda_menurunkan_kasur}")
      else :
        print(f"Denda menurunkan kasur : {0}")

      if len(list_barang_hilang) > 0 :
        print("Denda barang rusak/hilang")
        for x in list_barang_hilang :
            print(f"{x} : {barang[x]}")
        print(f"denda : {total_denda}")
        print(f"total harga : {harga_akhir}")

