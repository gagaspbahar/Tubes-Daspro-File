import time, math

#FB01 - Hashing
def hashing(s):
# String Folding
    sum = 0
    mul = 1
    i = 0
    while i < len(s)-1:
        if i % 4 == 0:
            mul * 256
        now = int(str(ord(s[i])) + str(ord(s[i+1]))) * mul
        sum += now
        i += 1
    return sum

#FB03 - Gacha
def gacha(consumable):
    consumable = sorted(consumable,key=lambda i: i['rarity'], reverse=True)                                                     # Sort by rarity
    consS = []
    consA = []
    consB = []
    consC = []
    print("Inventory List: ")                                                                                                   # Pilah by rarity
    for i in range(len(consumable)):
        if consumable[i]['rarity'] == 'S':
            consS.append(consumable[i])
        elif consumable[i]['rarity'] == 'A':
            consA.append(consumable[i])
        elif consumable[i]['rarity'] == 'B':
            consB.append(consumable[i])
        elif consumable[i]['rarity'] == 'C':
            consC.append(consumable[i])                                                                                         # Tampilkan yang tersedia
        print("{}. {} (Rarity {}) (x{})".format(i+1, consumable[i]['nama'], consumable[i]['rarity'], consumable[i]['jumlah']))
    
    # Inisiasi list item yang akan digacha
    itemList = []
    prompt = True
    while prompt:
        temp = {}
        # Input
        select = int(input("Pilih consumable yang ingin digunakan: "))
        jumlahGacha = int(input("Jumlah yang ingin digunakan: "))
        if jumlahGacha < 1 or jumlahGacha > int(consumable[select-1]['jumlah']):                                                # Validasi jumlah
            print("Jumlah tidak valid.")
            return []
        # Append
        temp['id'] = consumable[select-1]['id']
        temp['jumlah'] = consumable[select-1]['jumlah']
        temp['rarity'] = consumable[select-1]['rarity']
        temp['jumlahGacha'] = jumlahGacha
        itemList.append(temp)
        prompt = input("Tambahkan item lagi? (y/n)?: ").lower()
        if prompt == 'n':
            prompt = False
    
    # Penentuan chance berdasarkan jumlah item
    totalGacha = 0
    chance = [0,0,0,0]
    for item in itemList:
        if item['rarity'] == 'S':
            chance[3] += int(temp['jumlah'])*4
        elif item['rarity'] == 'A':
            chance[3] += int(temp['jumlah'])*3
            chance[2] += int(temp['jumlah'])*4
        elif item['rarity'] == 'B':
            chance[3] += int(temp['jumlah'])*2
            chance[2] += int(temp['jumlah'])*3
            chance[1] += int(temp['jumlah'])*4
        elif item['rarity'] == 'C':
            chance[3] += int(temp['jumlah'])*1
            chance[2] += int(temp['jumlah'])*2
            chance[1] += int(temp['jumlah'])*3
            chance[0] += int(temp['jumlah'])*4
        for entry in consumable:
            if entry['id'] == item['id']:
                entry['jumlah'] = str(int(entry['jumlah'])-int(item['jumlahGacha']))

    # Penentuan rarity hasil
    for i in chance:
        totalGacha += i
    number = seed() % totalGacha
    result = ""
    if number <= chance[0]:
        result = "c"
    elif chance[0] < number <= chance[1]:
        result = "b"
    elif chance[1] < number <= chance[2]:
        result = "a"
    else:
        result = "s"
    
    # Penentuan item hasil (dengan rarity tertentu)
    itemDidapat = []
    if result == "s":
        number = seed() % len(consS)
        itemDidapat = consS[number]
    elif result == "a":
        number = seed() % len(consA)
        itemDidapat = consA[number]
    elif result == "b":
        number = seed() % len(consB)
        itemDidapat = consB[number]
    else:
        number = seed() % len(consC)
        itemDidapat = consC[number]
    
    for entry in consumable:
        if itemDidapat['id'] == entry['id']:
            entry['jumlah'] = str(int(entry['jumlah'])+1)
            namaItem = entry['nama']
    
    print("Selamat! Item baru telah ditambahkan ke dalam sistem: {} (Rarity {})".format(namaItem, result.upper()))
    return consumable

def seed():
    #Seed dari waktu saat ini (dihitung sejak UNIX Epoch)
    return round(time.time())