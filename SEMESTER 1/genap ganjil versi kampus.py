nama =input("Nama Lengkap:")
umur =input("Umur:")
kode=input("kode jekel l/p:")
jekel=str
if(kode=="l"):
    jekel="laki laki"
elif(kode=="p"):
    jekel="perempuan"
else:
    jekel="tidak diketahui"
print("jenis kelamin:",jekel)

nilai_angka=int(input("nilai angka: "))
if(nilai_angka>=80):
    nilai_huruf="A"
elif(nilai_angka>=75):
    nilai_huruf="B+"
elif(nilai_angka>=70):
    nilai_huruf="B"
elif(nilai_angka>=65):
    nilai_huruf="C+"
elif(nilai_angka>=60):
    nilai_huruf="C"
elif(nilai_angka>=50):
    nilai_huruf="D"
else:
    nilai_huruf="E"
print("nilaimu sangat bagus:",nilai_huruf)