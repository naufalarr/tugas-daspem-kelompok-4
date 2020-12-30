def nama ():
    print("==========================================================")
    print("|\t             PENJUALAN TIKET BIOSKOP            |")
    print("|\t                  FUTURE CINEMA                 |")
    print("|========================================================|")
    print("|________________________________________________________|")
    print("| No                Nama Film            Harga           |")
    print("|________________________________________________________|")
    print("| 1                 Ironman 2            40000           |")
    print("| 2                 Monster Inc          35000           |")
    print("| 3                 The Avengers         50000           |")
    print("| 4                 Star Wars 2          30000           |")
nama()

input("Nama Petugas     :")
input("Nama Customer    :")
daftar=int(input("Jumlah Pembelian  :"))
Nomor = []
banyak = []
nama_film =[]
harga = []
jumlah = []
i = 0
for i in range(daftar):
    print("Pembelian ke - ", i+1)
    nomor.append(input("No. Film [1/2/3/4] :"))
    banyak.append(int(input("Banyak Tiket :")))
    if nomor[i] == "1" :
        nama_film.append("Iron Man 2    ")
        harga.append("40000")
        jumlah.append(banyak[i]*int("40000"))