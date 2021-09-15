import os
import sys
from datetime import datetime

def countsemicolon(s):
    # Fungsi penghitung jumlah semicolon pada string
    out = 0
    for i in s:
        out += 1 if i == ';' else 0
    return out

# Comma Splitter to a Data Array
def parseData(lines):
    # Fungsi parse data dari CSV, mirip dengan split() dengan beberapa tambahan
    lines = [line.replace("\n","") for line in lines]
    ar = [["" for i in range(countsemicolon(lines[0])+1)] for j in range(len(lines))]
    for i in range(len(lines)):
        j = 0
        while j < (countsemicolon(lines[0])):
            for k in range(len(lines[i])):
                if lines[i][k] != ';':
                    ar[i][j] += lines[i][k]
                else:
                    j += 1
    ar = [[data.strip() for data in ar[i]] for i in range(len(ar))]
    return ar

# F14 - Load Data
def load(folder, thing):
    # Fungsi load data
    things = []
    path = os.path.join('{}/{}.csv').format(folder,thing)
    with open(path,"r") as obj:                                                                 # Read lines dari CSV
        arthing = obj.readlines()
    if arthing == "":                                                                           # Apabila csv kosong
        return []
    arthing = parseData(arthing)
    if thing == 'user':                                                                         # Load user
        for line in arthing:
            temp = {}
            temp['id'] = line[0]
            temp['username'] = line[1]
            temp['nama'] = line[2]
            temp['alamat'] = line[3]
            temp['password'] = line[4]
            temp['role'] = line[5]
            things.append(temp)
    elif thing == 'gadget':                                                                     # Load gadget
        for line in arthing:
            temp = {}
            temp['id'] = line[0]
            temp['nama'] = line[1]
            temp['deskripsi'] = line[2]
            temp['jumlah'] = line[3]
            temp['rarity'] = line[4]
            temp['tahun_ditemukan'] = line[5]
            things.append(temp)
    elif thing == 'consumable':                                                                 # Load consumable
        for line in arthing:
            temp = {}
            temp['id'] = line[0]
            temp['nama'] = line[1]
            temp['deskripsi'] = line[2]
            temp['jumlah'] = line[3]
            temp['rarity'] = line[4]
            things.append(temp)
    elif thing == 'consumable_history':                                                         # Load consumable_history
        for line in arthing:
            temp = {}
            temp['id'] = line[0]
            temp['id_pengambil'] = line[1]
            temp['id_consumable'] = line[2]
            temp['tanggal_pengambilan'] = line[3]
            temp['dt'] = datetime.strptime(line[3], "%d/%m/%Y")
            temp['jumlah'] = line[4]
            things.append(temp)
    elif thing == 'gadget_borrow_history':                                                      # Load gadget_borrow_history
        for line in arthing:
            temp = {}
            temp['id'] = line[0]
            temp['id_peminjam'] = line[1]
            temp['id_gadget'] = line[2]
            temp['dt'] = datetime.strptime(line[3], "%d/%m/%Y")
            temp['tanggal_peminjaman'] = line[3]
            temp['jumlah'] = line[4]
            temp['jumlah_kembali'] = line[5]
            temp['is_returned'] = line[6]
            things.append(temp)
    elif thing == 'gadget_return_history':                                                      # Load gadget_return_history
        for line in arthing:
            temp = {}
            temp['id'] = line[0]
            temp['id_peminjaman'] = line[1]
            temp['tanggal_pengembalian'] = line[2]
            temp['dt'] = datetime.strptime(line[2], "%d/%m/%Y")
            temp['jumlah_peminjaman'] = line[3]
            things.append(temp)
    return things

# F15 - Save Data
def save(files):
    # Realisasi fungsi save
    filenames = ["user.csv", "gadget.csv", "consumable.csv", "consumable_history.csv", "gadget_return_history.csv", "gadget_borrow_history.csv"]
    folder = input("Masukkan nama folder penyimpanan: ")
    parent = os.getcwd()                                                                        # Current working dir
    listdir = os.listdir(parent)                                                                # Listdir
    fpath = parent + "\\{}".format(folder)
    if folder not in listdir:                                                                   # Apabila folder tidak ada
        os.mkdir(fpath)
    listdir = os.listdir(fpath)
    for filename in filenames:                                                                  # Remove file bernama sama terlebih dahulu
        if filename in listdir:
            os.remove("{}\\{}".format(fpath,filename))
    for i in range(6):
        with open("{}\\{}".format(fpath, filenames[i]),"w") as obj:                             # Write kedalam csv
            obj.write(dataToString(files[i]))
    print("Data telah berhasil disave.")

def dataToString(array):
    # Fungsi data To String untuk save
    stringData = ""
    for i in array:
        if i.get("dt") != None:
            i = i.pop("dt")
    for dic in array:
        dic = list(dic.values())
        dic = ";".join(dic)
        for i in dic:
            allString = [str(one) for one in i]
            stringData += ";".join(allString)
        stringData += "\n"
    return stringData

# F16 - Help
def help(role):
    # Fungsi help, berdasarkan role
    if role == 'user':                                                                                                              # Apabila role = user
        print(
            '''
==== HELP ====
carirarity = Cari gadget berdasarkan rarity.
caritahun = Cari gadget berdasarkan tahun ditemukannya, dengan parameter >, >=, <, <=, =.
pinjam = Pinjam gadget yang tersedia pada inventaris.
kembalikan = Kembalikan gadget yang telah anda pinjam.
minta = Minta consumable yang tersedia pada inventaris.
save = Simpan data yang telah diubah pada sistem.
help = Munculkan list command yang tersedia.
exit = Keluar dari sistem.
            '''
        )
    elif role == 'admin':                                                                                                           # Apabila role = admin
        print(
            '''
==== HELP ====
register = Daftarkan user baru.
carirarity = Cari gadget berdasarkan rarity.
caritahun = Cari gadget berdasarkan tahun ditemukannya, dengan parameter >, >=, <, <=, =.
tambahitem = Tambahkan item (gadget atau consumable) ke dalam inventaris.
hapusitem = Hapus item (gadget atau consumable) ke dalam inventaris.
ubahjumlah = Ubah jumlah item (gadget atau consumable) yang ada pada inventaris.
riwayatpinjam = Lihat riwayat peminjaman gadget.
riwayatkembali = Lihat riwayat pengembalian gadget.
riwayatambil = Lihat riwayat pengambilan consumable.
save = Simpan data yang telah diubah pada sistem.
help = Munculkan list command yang tersedia.
exit = Keluar dari sistem.
            '''
        )
    else:                                                                                                                           # Apabila belum login
        print("login = untuk masuk kedalam akun")