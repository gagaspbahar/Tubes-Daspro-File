from datetime import datetime
# F08 - Lend/Pinjam

def pinjam(gadget, gadget_borrow_history, currentuser):
    # Realisasi fungsi pinjam
    if currentuser['role'] == "admin":                                                  # Validasi role
        print("Menu tidak tersedia.")
        return []
    idlist = [gadgets['id'] for gadgets in gadget]                                      # Mengelist ID
    idpinjam = input("Masukkan ID item: ")
    tanggal = input("Tanggal peminjaman: ")
    jumlah = int(input("Jumlah peminjaman: "))
    if idpinjam in idlist:
        for gadgets in gadget:
            for history in gadget_borrow_history:
                if gadgets['id'] == history['id_gadget']:
                    if history['id_peminjam'] == currentuser['id']:
                        if history['is_returned'] == "0":
                            if gadgets['id'] == idpinjam:                               # Cek apabila barang sudah dipinjam oleh user
                                print("Anda sudah meminjam barang ini. Kembalikan dahulu sebelum meminjam lagi.")
                                return []
            if gadgets['id'] == idpinjam:                                               # Append kedalam gadget borrow history
                if int(gadgets['jumlah']) >= jumlah:
                    gadgets['jumlah'] = str(int(gadgets['jumlah']) - jumlah)
                    temp = {}
                    temp['id'] = str(len(gadget_borrow_history) + 1)
                    temp['id_peminjam'] = currentuser['id']
                    temp['id_gadget'] = idpinjam
                    temp['tanggal_peminjaman'] = tanggal
                    temp['dt'] = datetime.strptime(tanggal, "%d/%m/%Y")
                    temp['jumlah'] = str(jumlah)
                    temp['jumlah_kembali'] = str(0)
                    temp['is_returned'] = str(0)
                    gadget_borrow_history.append(temp)
                    print("Item {} (x{}) berhasil dipinjam!".format(gadgets['nama'], jumlah))
                    return (gadget, gadget_borrow_history)
                else:                                                                   # Apabila jumlah gadget tidak mencukupi
                    print("Jumlah gadget pada inventaris tidak mencukupi.")
                    return []   
    else:   
        print("ID gadget tidak tersedia.")
# F09 - Return
def kembalikan(gadget, gadget_borrow_history, gadget_return_history, currentuser):
    # Realisasi fungsi pinjam
    if currentuser['role'] == "admin":                                                  # Validasi role
        print("Menu tidak tersedia.")
        return []
    returnList = []
    allReturned = False
    for history in gadget_borrow_history:                                               # append gadget yang dapat dikembalikan
        if history['id_peminjam'] == currentuser['id']:
            returnList.append(history)
    if returnList == []:                                                                # Apabila tidak ada yang dapat dikembalikan
        print("Anda belum meminjam item apapun.")
        return []
    for i in range(len(returnList)):                                                    # Menampilkan yang dapat dikembalikan
        if returnList[i]['is_returned'] == "0":
            for gadgets in gadget:
                if returnList[i]['id_gadget'] == gadgets['id']:
                    currGadget = gadgets
            print("{}. {} (x{})".format(i+1, currGadget['nama'], str(int(returnList[i]['jumlah'])-int(returnList[i]['jumlah_kembali']))))
    idxKembali = int(input("Masukkan nomor peminjaman: "))
    try:
        tglKembali = input("Masukkan tanggal pengembalian (DD/MM/YYYY): ")              # Input tanggal kembali dan validasi
        dt_tglKembali = datetime.strptime(tglKembali, "%d/%m/%Y")
    except:
        print("Tanggal pengembalian tidak valid.")
        return []
    jmlKembali = int(input("Masukkan jumlah yang ingin dikembalikan: "))                # Input jumlah dikembalikan dan validasi
    if jmlKembali == int(returnList[idxKembali-1]['jumlah'])-int(returnList[idxKembali-1]['jumlah_kembali']):
        allReturned = True
    if jmlKembali < 1 or jmlKembali > int(returnList[idxKembali-1]['jumlah'])-int(returnList[idxKembali-1]['jumlah_kembali']):
        print("Jumlah pengembalian tidak valid.")
        return []
    else:
        for history in gadget_borrow_history:                                           # Pengubahan jumlahkembali
            if history['id'] == returnList[idxKembali-1]['id']:
                currHistory = history
                if allReturned:
                    history['is_returned'] = str(1)
                else:
                    history['jumlah_kembali'] = str(int(history['jumlah_kembali']) + jmlKembali)
        for gadgets in gadget:
            if gadgets['id'] == returnList[idxKembali-1]['id_gadget']:
                currGadget = gadgets
                gadgets['jumlah'] = str(int(gadgets['jumlah']) + jmlKembali)

    temp = {}                                                                           # Append ke return history
    temp['id'] = str(len(gadget_return_history) + 1)
    temp['id_peminjaman'] = str(currHistory['id'])
    temp['tanggal_pengembalian'] = tglKembali
    temp['dt'] = dt_tglKembali
    temp['jumlah_pengembalian'] = str(jmlKembali)
    gadget_return_history.append(temp)
    print("Berhasil mengembalikan {} sebanyak {} buah.".format(currGadget['nama'], jmlKembali))
    return (gadget, gadget_borrow_history, gadget_return_history)

# F10 - Ask item
def minta(consumable, consumable_history, currentuser):
    # Realisasi fungsi minta
    if currentuser['role'] == "admin":                                                  # validasi role
        print("Menu tidak tersedia.")
        return []
    idlist = [consumables['id'] for consumables in consumable]                          # list ID yang dapat diminta
    idambil = input("Masukkan ID item: ")
    tanggal = input("Tanggal permintaan: ")
    jumlah = int(input("Jumlah permintaan: "))
    if idambil in idlist:
        for consumables in consumable:
            if consumables['id'] == idambil:
                if int(consumables['jumlah']) >= jumlah:                                # append ke consumable_history
                    consumables['jumlah'] = str(int(consumables['jumlah']) - jumlah)
                    temp = {}
                    temp['id'] = str(len(consumable_history) + 1)
                    temp['id_pengambil'] = currentuser['id']
                    temp['id_consumable'] = idambil
                    temp['tanggal_pengambilan'] = tanggal
                    temp['dt'] = datetime.strptime(tanggal, "%d/%m/%Y")
                    temp['jumlah'] = str(jumlah)
                    consumable_history.append(temp)
                    print("Item {} (x{}) berhasil diminta!".format(consumables['nama'], jumlah))
                    return (consumable, consumable_history)
        else:
            print("Jumlah consumable pada inventaris tidak mencukupi.")                  # Apabila jumlah tidak cukup
            return []

    else:
        print("ID consumable tidak tersedia.")