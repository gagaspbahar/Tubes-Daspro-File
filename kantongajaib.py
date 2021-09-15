import argparse, os, time, sys, math, time, datetime
from functions import fileio, reglogin, adminfn, userfn, history, search, bonus

# Argument Parsing
parser = argparse.ArgumentParser()
parser.add_argument("nama_folder", help="load a specific folder")
args = parser.parse_args()
folder = args.nama_folder
if (not os.path.isdir(folder)):
    # bila nama folder tidak tersedia
    print("Tidak ada nama folder yang diberikan!")
    print("Usage: python kantongajaib.py <nama_folder>")
    sys.exit()


# Load semua csv (6 files) (F14)
user = fileio.load(folder, "user")
gadget = fileio.load(folder, "gadget")
consumable = fileio.load(folder, "consumable")
consumable_history = fileio.load(folder, "consumable_history")
gadget_borrow_history = fileio.load(folder, "gadget_borrow_history")
gadget_return_history = fileio.load(folder, "gadget_return_history")

print("Halo, selamat datang di Kantong Ajaib.")


# Menu
current = []
loggedIn = False
# Apabila belum login
while not loggedIn:
    prompt = input()
    if prompt == 'login':
        # Implementasi fungsi login di main
        current.append(reglogin.login(user))
        currentuser = current[0]
        role = currentuser['role']
        loggedIn = True
        continue
    elif prompt == 'help':
        # Implementasi fungsi help sebelum ada role
        if loggedIn:
            fileio.help(role)
        else:
            fileio.help("")
    elif prompt == 'exit':
        # Implementasi fungsi exit sebelum ada role
        print("Sampai jumpa di lain waktu!")
        sys.exit()
    else:
        print("Command tidak valid atau anda tidak memiliki kewenangan. Login lalu coba kembali.")
while loggedIn:
    prompt = input()    
    if prompt == 'register':
        # Implementasi fungsi register
        user = reglogin.register(role, user)
        continue
    elif prompt == "carirarity":
        # Implementasi fungsi carirarity
        search.carirarity(gadget)
    elif prompt == "caritahun":
        # Implementasi fungsi caritahun
        search.caritahun(gadget)
    elif prompt == "tambahitem":
        # Implementasi fungsi tambahitem
        temp = adminfn.tambahitem(gadget, consumable, role)
        if temp != 0:
            if temp[0]['id'][0] == 'G':
                gadget = temp
            elif temp[0]['id'][0] == 'C':
                consumable = temp
    elif prompt == "hapusitem":
        # Implementasi fungsi hapusitem
        temp = adminfn.hapusitem(gadget, gadget_borrow_history, consumable, role)
        if temp != 0:
            if temp[0]['id'][0] == 'G':
                gadget = temp
            elif temp[0]['id'][0] == 'C':
                consumable = temp
    elif prompt == "ubahjumlah":
        # Implementasi fungsi ubahjumlah
        temp = adminfn.ubahjumlah(gadget, consumable, role)
        if temp != 0:
            if temp[0]['id'][0] == 'G':
                gadget = temp
            elif temp[0]['id'][0] == 'C':
                consumable = temp
    elif prompt == "pinjam":
        # Implementasi fungsi pinjam
        temp = userfn.pinjam(gadget, gadget_borrow_history, currentuser)
        if temp != []:
            gadget = temp[0]
            gadget_borrow_history = temp[1]
    elif prompt == "kembalikan":
        # Implementasi fungsi kembalikan
        temp = userfn.kembalikan(gadget, gadget_borrow_history, gadget_return_history, currentuser)
        if temp != []:
            gadget = temp[0]
            gadget_borrow_history = temp[1]
            gadget_return_history = temp[2]
    elif prompt == "minta":
        # Implementasi fungsi minta
        temp = userfn.minta(consumable, consumable_history, currentuser)
        if temp != []:
            consumable = temp[0]
            consumable_history = temp[1]
    elif prompt == "riwayatpinjam":
        # Implementasi fungsi riwayatpinjam
        history.riwayatpinjam(gadget, gadget_borrow_history, user, role)
        continue
    elif prompt == "riwayatkembali":
        # Implementasi fungsi riwayatkembali
        history.riwayatkembali(gadget, gadget_return_history, gadget_borrow_history, user, role)
        continue
    elif prompt == "riwayatambil":
        # Implementasi fungsi riwayatambil
        history.riwayatambil(consumable, consumable_history, user, role)
        continue
    elif prompt == "save":
        # Implementasi fungsi save
        files = [user, gadget, consumable, consumable_history, gadget_return_history, gadget_borrow_history]
        fileio.save(files)
        continue
    elif prompt == "help":
        # Implementasi fungsi help
        fileio.help(role)
    elif prompt == "gacha":
        # Implementasi fungsi gacha
        bonus.gacha(consumable)
    elif prompt == 'exit':
        # Implementasi fungsi exit
        flag = input("Apakah anda ingin melakukan penyimpanan file yang telah diubah? (Y/N) ").lower()
        if flag == 'y':
            files = [user, gadget, consumable, consumable_history, gadget_return_history, gadget_borrow_history]
            fileio.save(files)
        print("Sampai jumpa di lain waktu!")
        sys.exit()