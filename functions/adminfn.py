# F05 - Add item
def tambahitem(gadget, consumable, role):
    if role == 'user':                                                                                  # Validasi role
        print("Anda tidak memiliki kewenangan untuk melaksanakan aksi ini.")
    else:
        item_id = input("Masukkan ID: ")
        isUsed = False
        if (item_id[0] != 'C') and (item_id[0] != 'G'):                                                 # Validasi ID
            print("Gagal menambahkan item karena ID tidak valid.")
        else:
            for i in range(len(gadget)):                                                                # Validasi ID sudah ada atau belum
                if(gadget[i]['id'] == item_id):
                    isUsed = True
            for i in range(len(consumable)):
                if (consumable[i]['id'] == item_id):
                    isUsed = True
            if (isUsed == True):
                print("Gagal menambahkan item karena ID sudah ada.")
            else:  
                nama = input("Masukkan Nama: ")                                                         # Input, validasi input
                deskripsi = input("Masukkan Deskripsi: ")
                jumlah = input("Masukkan Jumlah: ")
                isNumber = False
                if (jumlah.isnumeric):
                    if int(jumlah) > 0: 
                        isNumber = True
                if (isNumber == False):
                    print("Input jumlah tidak valid")
                else:
                    rarity = input("Masukkan Rarity: ")
                    if (rarity != 'S') and (rarity != 'A') and (rarity != 'B') and (rarity != 'C'):
                        print("Input rarity tidak valid")
                    elif (item_id[0] == 'C'):
                        temp = {'id': item_id, 'nama': nama, 'deskripsi': deskripsi, 'jumlah': jumlah, 'rarity': rarity}
                        consumable.append(temp)
                        print("Item telah berhasil ditambahkan ke database.")
                    else:
                        tahun_ditemukan = input("Masukkan tahun ditemukan: ")
                        if (tahun_ditemukan.isnumeric):
                            isNumber = True
                        if (isNumber == False):
                            print("Input tahun tidak valid")
                        else:
                            temp = {'id': item_id, 'nama': nama, 'deskripsi': deskripsi, 'jumlah': jumlah, 'rarity': rarity, 'tahun_ditemukan': tahun_ditemukan}
                            gadget.append(temp)
                            print("Item telah berhasil ditambahkan ke database.")
                            return gadget
    return consumable

# F06 - Delete
def hapusitem(gadget, gadget_borrow_history, consumable, role):
    if role == 'user':                                                                                                      # Validasi role
        print("Anda tidak memiliki kewenangan untuk melaksanakan aksi ini.")
    else:
        delID = input("Masukkan ID item: ")                                                                                 
        idlist = [gadgets['id'] for gadgets in gadget]                                                                      # Mengelist ID yang ada pada sistem
        idlist += [consumables['id'] for consumables in consumable]
        if delID in idlist:
            if delID[0] == 'G':
                sedangDipinjam = False
                for history in gadget_borrow_history:                                                                       # Validasi sedang dipinjam
                    if delID == history['id_gadget']:
                        if history['is_returned'] == "0":
                            sedangDipinjam = True
                if sedangDipinjam:                                                                                          # Error sedang dipinjam
                    print("Gadget tidak bisa dihapus dari database karena gadget sedang dipinjam oleh user.")
                    return 0
                gadget = [i for i in gadget if not(i['id'] == delID)]                                                       # Penghapusan gadget
                print("Gadget telah berhasil dihapus dari database.")
                return gadget
            else:
                consumable = [i for i in consumable if not(i['id'] == delID)]                                               # Penghapusan consumable
                print("Consumable telah berhasil dihapus dari database.")
                return consumable
        else:                                                                                                               # Catch akhir apabila tidak ada item dgn ID tsb
            print("Tidak ada item dengan ID tersebut.")
            return 0

# F07 - Edit jumlah
def ubahjumlah(gadget, consumable, role):
    if role == 'user':                                                                                                      # Validasi role
        print("Anda tidak memiliki kewenangan untuk melaksanakan aksi ini.")
    else:
        ubahID = input("Masukkan ID item: ")
        idlist = [gadgets['id'] for gadgets in gadget]                                                                      # Mengelist ID yang ada pada sistem
        idlist += [consumables['id'] for consumables in consumable]
        change = int(input("Masukkan jumlah: "))
        if ubahID not in idlist:                                                                                            # Validasi ID
            print("Tidak ada item dengan ID tersebut!")
            return 0
        else:
            if ubahID[0] == 'G':
                for g in gadget:
                    if g['id'] == ubahID:                                                                                   # Pengurangan/penambahan jumlah gadget
                        g['jumlah'] = str(int(g['jumlah']) + change)
                        if int(g['jumlah']) < 0:
                            g['jumlah'] = str(int(g['jumlah']) - change)                                                    
                            print("{} {} gagal dibuang karena stok kurang. Stok sekarang: {}.".format(-1*change, g['nama'], g['jumlah']))
                        elif change > 0:
                            print("{} {} berhasil ditambahkan. Stok sekarang: {}.".format(change, g['nama'], g['jumlah']))
                        else:
                            print("{} {} berhasil dibuang. Stok sekarang: {}.".format(-1*change, g['nama'], g['jumlah']))
                return gadget
            else:
                for c in consumable:
                    if c['id'] == ubahID:                                                                                   # Pengurangan/penambahan jumlah consumable
                        c['jumlah'] = str(int(c['jumlah']) + change)
                        if int(c['jumlah']) < 0:
                            c['jumlah'] = str(int(c['jumlah']) - change)
                            print("{} {} gagal dibuang karena stok kurang. Stok sekarang: {}".format(-1*change, c['nama'], c['jumlah']))
                        elif change > 0:
                            print("{} {} berhasil ditambahkan. Stok sekarang: {}.".format(change, c['nama'], c['jumlah']))
                        else:
                            print("{} {} berhasil dibuang. Stok sekarang: {}.".format(-1*change, c['nama'], c['jumlah']))
                return consumable