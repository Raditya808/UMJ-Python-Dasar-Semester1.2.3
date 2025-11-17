# belajar array
# array adalah kumpulan data yang memiliki tipe data yang sama
# array dapat digunakan untuk menyimpan data yang berurutan
buah = ['apple' , 'jeruk' ,'durian' ]

buah.append('duku')
buah.append('nangka')
buah.append('semangka')
buah.append('nag')
# fungsi append adalah penamabahan data dalam bentuk list / digabung dalam bentuk list[]
# harus dalam bentuk sebuah list jika tidak maka data tersebut tidak akan tergabung

print("===========================") # output garis pemisah
print(buah) # output keluar tetapi outputnya keluar semua

print(len(buah)) # fungsi len adalah menghitung jumlah elemen dalam array

print(buah[0]) # mengakses elemen pertama dalam array

print(buah[1]) # mengakses elemen kedua dalam array

print(buah[2]) # mengakses elemen ketiga dalam array

print(buah[3]) # mengakses elemen keempat dalam array

print(buah[4]) # mengakses elemen kelima dalam array

print(buah[5]) # mengakses elemen keenam dalam array

print(buah[6]) # mengakses elemen ketujuh dalam array
print("===========================")

for i in buah:
    print(f"Buah: {i}") # fungsi for i in buah adalah untuk mencetak semua elemen dalam array

# fungsi for i in range adalah untuk mencetak semua elemen dalam array

# append dalam khasus penambahan data
a = ['radit']
a.append('nigga') # Membuat data dalam list string radit dan menambahkan sebuah data bernama nigga maka hasil nya kedua data akan tergabung
print(a) # ['radit','nigga']
