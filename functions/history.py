import datetime
from functions import fileio

# F11 - Lending History
def riwayatpinjam(gadget, gadget_borrow_history, user, role):
    # Realisasi fungsi riwayat pinjam
    if role == 'user':                                                                                                  # Validasi role
        print("Anda tidak memiliki kewenangan untuk melaksanakan aksi ini.")
    else:  
        gadget_borrow_history = sorted(gadget_borrow_history,key=lambda i: i['dt'], reverse=True)                       # Sort berdasarkan dt
        cnt = 0
        while True:
            try:
                for i in range(cnt,cnt+5):
                    for g in gadget:                                                                                    # Lookup value nama gadget
                        if gadget_borrow_history[i]['id_gadget'] == g['id']:
                            namaGadget = g['nama']
                    for u in user:
                        if u['id'] == gadget_borrow_history[i]['id_peminjam']:                                          # Lookup value nama peminjam
                            namaPeminjam = u['nama']
                    print(
                        '''
ID Peminjaman:      {}
Nama Pengambil:     {}
Nama Gadget:        {}
Tanggal Peminjaman: {}
Jumlah:             {}
                        '''.format(gadget_borrow_history[i]['id'], namaPeminjam, namaGadget, 
                        gadget_borrow_history[i]['tanggal_peminjaman'], gadget_borrow_history[i]['jumlah'])
                    )

            except(IndexError):
                print("Anda telah mencapai akhir entri.")                                                              # Apabila mencapai akhir entri
                break
            prompt = input("Tampilkan 5 entri lagi? (Y/N) ").lower()                                                   # Tampilkan 5 entri lagi atau tidak
            if prompt == 'y':
                cnt += 5
            else:
                break

# F12 - Returning History
def riwayatkembali(gadget, gadget_return_history, gadget_borrow_history, user, role):
    if role == 'user':                                                                                                  # Validasi role
        print("Anda tidak memiliki kewenangan untuk melaksanakan aksi ini.")
    else:  
        gadget_return_history = sorted(gadget_return_history,key=lambda i: i['dt'], reverse=True)                       # Sort berdasarkan dt
        cnt = 0
        while True:
            try:
                for i in range(cnt,cnt+5):
                    for gbh in gadget_borrow_history:
                        if gadget_return_history[i]['id_peminjaman'] == gbh['id']:
                            for g in gadget:
                                if g['id'] == gbh['id_gadget']:                                                         # Lookup value nama gadget
                                    namaGadget = g['nama']
                            for u in user:
                                if u['id'] == gbh['id_peminjam']:                                                       # Lookup value nama peminjam
                                    namaPeminjam = u['nama']
                    print(
                        '''ID Pengembalian:            {}
Nama Peminjam:              {}
Nama Gadget:                {}
Tanggal Pengembalian:       {}
Jumlah yang dikembalikan:   {}
                        '''.format(gadget_return_history[i]['id'], namaPeminjam, namaGadget,
                            gadget_return_history[i]['tanggal_pengembalian'], gadget_return_history[i]['jumlah_peminjaman'])
                        )
            except(IndexError):                                                                                         # Apabila indeks habis
                print("Anda telah mencapai akhir entri.")
                break
            prompt = input("Tampilkan 5 entri lagi? (Y/N) ").lower()                                                    # Apakah ingin melihat 5 entri lagi atau tidak
            if prompt == 'y':
                cnt += 5
            else:
                break     

# F13 - Ask History
def riwayatambil(consumable, consumable_history, user, role):
    if role == 'user':                                                                                                  # Validasi role
        print("Anda tidak memiliki kewenangan untuk melaksanakan aksi ini.")
    else:  
        consumable_history = sorted(consumable_history,key=lambda i: i['dt'], reverse=True)                             # Sort berdasarkan dt
        cnt = 0
        while True:
            try:
                for i in range(cnt,cnt+5):
                    for c in consumable:
                        if consumable_history[i]['id_consumable'] == c['id']:                                           # Lookup value nama consumable
                            namaCons = c['nama']
                    for u in user:
                        if consumable_history[i]['id_pengambil'] == u['id']:                                            # Lookup value nama pengambil
                            namaPengambil = u['nama']
                    print(
                        '''
ID Pengambilan:         {}
Nama Pengambil:         {}
Nama Consumable:        {}
Tanggal Pengambilan:    {}
Jumlah:                 {}
                        '''.format(consumable_history[i]['id'], namaPengambil, namaCons, 
                        consumable_history[i]['tanggal_pengambilan'], consumable_history[i]['jumlah'])
                    )

            except(IndexError):
                print("Anda telah mencapai akhir entri.")                                                               # Apabila telah mencapai akhir entri
                break
            prompt = input("Tampilkan 5 entri lagi? (Y/N) ").lower()                                                    # Ingin melihat 5 entri lagi atau tidak
            if prompt == 'y':
                cnt += 5
            else:
                break 