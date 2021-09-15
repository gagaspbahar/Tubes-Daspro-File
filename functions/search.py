# F03 - Rarity search
def carirarity(gadget):
    # Realisasi fungsi cari rarity
    rarity = input("Masukkan rarity: ")
    print("\nHasil pencarian:\n")
    isFound = False
    for i in range(len(gadget)):
        if (gadget[i]['rarity'] == rarity):                                                 # Print apabila raritynya sama
            isFound = True
            print()
            print("Nama            : " + gadget[i]['nama'])
            print("Deskripsi       : " + gadget[i]['deskripsi'])
            print("Jumlah          : " + str(gadget[i]['jumlah']) + " buah")
            print("Rarity          : " + gadget[i]['rarity'])
            print("Tahun Ditemukan : " + str(gadget[i]['tahun_ditemukan']))

    if (isFound == False):                                                                  # Apabila tidak ada grup yang raritynya sama dengan input
        print("Tidak ada gadget yang ditemukan")
    else:    
        print("\n...")

# F04 - Year search
def caritahun(gadget):
    tahun = int(input("Masukkan tahun: "))                                                  # Input
    kategori = input("Masukkan kategori: ")
    isFound = False
    if (kategori == "<") or (kategori == "<="):                                             # Kategori < dan <=
        for i in range(len(gadget)):
                if (int(gadget[i]["tahun_ditemukan"]) < tahun):
                    isFound = True
                    print()
                    print("Nama            : " + gadget[i]["nama"])
                    print("Deskripsi       : " + gadget[i]["deskripsi"])
                    print("Jumlah          : " + str(gadget[i]["jumlah"]) + " buah")
                    print("Rarity          : " + gadget[i]["rarity"])
                    print("Tahun Ditemukan : " + gadget[i]["tahun_ditemukan"])

    if (kategori == "=") or (kategori == "<=") or (kategori == ">="):                       # Kategori =
        for i in range(len(gadget)):
                if (int(gadget[i]["tahun_ditemukan"]) == tahun):
                    isFound = True
                    print()
                    print("Nama            : " + gadget[i]["nama"])
                    print("Deskripsi       : " + gadget[i]["deskripsi"])
                    print("Jumlah          : " + str(gadget[i]["jumlah"]) + " buah")
                    print("Rarity          : " + gadget[i]["rarity"])
                    print("Tahun Ditemukan : " + gadget[i]["tahun_ditemukan"])

    if (kategori == ">") or (kategori == ">="):                                             # Kategori >
        for i in range(len(gadget)):
                if (int(gadget[i]["tahun_ditemukan"]) > tahun):
                    isFound = True
                    print()
                    print("Nama            : " + gadget[i]["nama"])
                    print("Deskripsi       : " + gadget[i]["deskripsi"])
                    print("Jumlah          : " + str(gadget[i]["jumlah"]) + " buah")
                    print("Rarity          : " + gadget[i]["rarity"])
                    print("Tahun Ditemukan : " + str(gadget[i]["tahun_ditemukan"]))

    if (isFound == False):                                                                  # Apabila tidak ada yang ditemukan
        print("Tidak ada gadget yang ditemukan")
    else:    
        print("\n...")