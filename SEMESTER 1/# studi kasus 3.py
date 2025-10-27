
masukan_nama_anda = input("Masukan Nama:").lower()
kamar = input("Pilih jenis kamar standard, deluxe, suite:").lower()
harga = int(input("Masukkan harga kamar: "))
lama_inap = int(input("Masukkan lama inap (dalam malam):"))
if kamar == "standard":
    if harga == 300000:
        if lama_inap >= 7:
            print("Anda berhak menerima diskon 25%")
        elif lama_inap <= 4:
            print("Maaf, tidak ada diskon untuk menginap kurang dari 4 malam")
        elif lama_inap >= 5:
            print("anda berhak mendapatkan diskon sebesar 5%")
        elif lama_inap <= 4:
             print("Maaf, tidak ada diskon untuk menginap kurang dari 4 malam")
        else:
            print("Anda memasukkan jumlah malam inap yang tidak sesuai.")


elif kamar == "deluxe":
    if harga == 500000:
        if lama_inap >= 7:
            print("Anda mendapatkan diskon 25%")
        elif lama_inap <= 4:
            print("Maaf, tidak ada diskon untuk menginap kurang dari 4 malam")
        elif 4 <= lama_inap < 7:
            print("Anda berhak mendapatkan diskon sebesar 5%")
        else:
            print("Anda input malam yang tidak sesuai.")


elif kamar == "suite":
    if harga == 1000000:
        if lama_inap >= 7:
            print("Anda berhak mendapatkan diskon 25%")
        elif lama_inap <= 4:
            print("Tidak ada diskon untuk menginap kurang dari 4 malam")
        elif lama_inap >= 5:
            print("Anda berhak mendapatkan diskon 5%")
        elif lama_inap <= 4:
            print("Maaf, tidak ada diskon untuk menginap kurang dari 4 malam")
        else:
            print("anda input jumlah malam yang tidak sesuai.")



denda_merokok          = 1000000
denda_menurunkan_kasur = 500000
harga_kasur            = 15000000
tv                     = 5000000
seprei                 = 1000000
selimut                = 1000000
bantal                 = 500000
handuk                 = 500000
# Input
merokok =   input("Apakah merokok di dalam kamar? (ya/tidak):").lower()
kasur1  =   input("Apakah menurunkan kasur?       (ya/tidak):").lower()
kasur2  =   input("Apakah membawa/merusak kasur?  (ya/tidak):").lower()
tv3     =   input("Aapakah membawa/merusak tv?    (ya/tidak):").lower()
seprei4 =   input("apakah membawa/merusak seprei? (ya/tidak):").lower()
selimut5=   input("apakah membawa/merusak selimut?(ya/tidak):").lower()
bantal6 =   input("apakah membawa/merusak bantal? (ya/tidak):").lower()
handuk7 =   input("apakah membawa/merusak handuk? (ya/tidak):").lower()

if merokok == "ya":
    print(f"Anda memiliki denda sebesar Rp{denda_merokok:} karena merokok di dalam kamar.")

if kasur1== "ya":
    print(f"Anda memiliki denda sebesar Rp{denda_menurunkan_kasur:} karena menurunkan kasur.")

if kasur2 == "ya":
    print(f"Anda memiliki denda sebesar Rp{harga_kasur:} karena membawa/merusak kasur.")

if tv3 == "ya":
    print(f"Anda memiliki denda sebesar Rp{tv:} karena membawa/merusak tv.")

if seprei4 =="ya":
    print(f"Anda memiliki denda sebesar Rp{seprei} karena membawa/merusak seprei")

if selimut5 =="ya":
    print(f"Anda memiliki denda sebesar Rp{selimut} karena membawa/merusak selimut")

if bantal6 =="ya":
    print(f"Anda memiliki denda sebesar Rp{bantal} karena membawa/merusak bantal")

if handuk7 =="ya":
    print(f"Anda memiliki denda sebesar Rp{handuk} karena membawa/merusak handuk")

print("================================")
print(f"Nama           = {masukan_nama_anda}")
print(f"Denda ngerokok = {merokok}")
print(f"kasur 1        = {kasur1}")
print(f"kasur 2        = {kasur2}")
print(f"tv             = {tv3}")
print(f"seprei 4       = {seprei4}")
print(f"selimut 5      = {selimut5}")
print(f"bantal         = {bantal6}")
print(f"handuk 7       = {handuk7}")
print("================================")

if merokok == "tidak":
        if kasur1 == "tidak":
            if kasur2 == "tidak":
                if tv3 ==  "tidak":
                    if seprei4 =="tidak":
                        if selimut5 =="tidak":
                            if bantal6 =="tidak":
                                if handuk7 =="tidak":
                                    print("Anda tidak dikenakan denda. Terima kasih telah mengikuti peraturan.")









