mahasiswa = []

batas = int(input("Masukkan jumlah mahasiswa: "))

for i in range(batas):
    nama = input("masukan nama mahasiswa: ")
    tugas = int(input("masukan nilai tugas: "))
    uts = int(input("masukan nilai uts: "))
    uas = int(input("masukan nilai uas: "))
    sikap = int(input("masukan nilai sikap: "))
    
for i in range(batas):
    mahasiswa.append((nama,tugas,uts,uas,sikap))
    

    data_nama = mahasiswa[i][0]
    data_tugasdata_utsdata_uasdata_sikap = mahasiswa[i][1] + mahasiswa[i][2] + mahasiswa[i][3] + mahasiswa[i][4]
    print("========data diri============")
    print(data_nama)
    print(f'''
              nilai tugas = {tugas} 
              nilai uts   = {uts}
              nilai uas   = {uas}
              nilai sikap = {sikap}
    
    ''')
    print("=========================")

    rata_rata = (tugas + uts + uas + sikap) / 4
    if rata_rata >= 80:
        print(f"\nNilai {nama} adalah A\n")
    elif rata_rata >= 70:
        print(f"\nNilai {nama} adalah B\n")
    elif rata_rata >= 60:
        print(f"\nNilai {nama} adalah C\n")
    elif rata_rata >= 50:
        print(f"\nNilai {nama} adalah D\n")
    else:
        print(f"\nNilai {nama} adalah E\n")
    



  
