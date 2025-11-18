data = []


def barang(barang1,barang2,barang3):
    gabungan = barang1,barang2,barang3
    return gabungan

def hitung_belanja(harga_untuk_b1,harga_untuk_b2,harga_untuk_b3):
    hitung = harga_untuk_b1 + harga_untuk_b2 + harga_untuk_b3
    return hitung

batas = int(input('Masukan batas data: '))
for i in range(batas):
    nama = input("Masukan nama: ")
    barang1 = input('Masukan barang belanja ke 1: ')
    barang2 = input('Masukan barang belanja ke 2: ')
    barang3 = input('Masukan barang belanja ke 3: ')
    harga_untuk_b1 = int(input('Masukan harga belanja ke 1: '))
    harga_untuk_b2 = int(input('Masukan harga belanja ke 2: '))
    harga_untuk_b3 = int(input('Masukan harga belanja ke 3: '))

    # menyimpan seluruh data menggunakan data = []
    data.append((nama, barang1, barang2, barang3, harga_untuk_b1,harga_untuk_b2, harga_untuk_b3))



for i in range(batas):
    data_nama = data[i][0] # mengambil indexing pertama di data append maka yang diambil dulu adalah nama jika angka nya 1 dll maka akan mengambil data yang lain / dan tentunya harus menggunakan data[i][0] agar dapat dipanggil
    data_barang1 = data[i][1] # data [1] maka akan mengambil data barang1
    data_barang2 = data[i][2] # data [2] mengambil data_barang2
    data_barang3 = data[i][3]
    hitung_harga = data[i][4] + data[i][5] + data[i][6] # data untuk harga_untuk_b1 , harga_untuk_b2, harga_untuk_b3 yang tidak perlu menggunakan variabel lagi karena sudah termasuk data list kosong

 # data[i] berfungsi untuk mengambil/mengakses elemen data yang berada pada posisi indeks 'i' dalam list 'data'.

# dan karena khasus nya menggunakan for i in range
    print("========Struuk belanja anda========")
    print(f"data_nama ke {i+1} {data_nama}") # menampilkan angka dari 1 sampai angka kesekian dari datanya
    print(f"data_barang ke {i+1} = {data_barang1}") # {i+1} berfungsi membuat data berurutan
    print(f"data_barang ke {i+1} = {data_barang2}")
    print(f"data barang ke {i+1} = {data_barang3}")
    print(f"harga gabungan dari b1 + b2 + b3 = {hitung_harga}")
    print("="*40)
    
    
