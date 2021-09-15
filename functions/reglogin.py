import sys

# F02 : Login
def login(users):
    # Realisasi fungsi login
    currentuser = {}
    rightPassword = ''
    username = input("Masukkan username: ")                                                             # Input username dan password    
    password = input("Masukkan password: ")
    try:
        for user in users:                                                                              # Cek password pada database
            if user['username'] == username:
                rightPassword = user['password']
                currentuser = user
        if str(hashing(password)) == rightPassword and currentuser != {}:                               # Apabila password benar
            print("Berhasil login.")
            print("Halo {}! Selamat datang di Kantong Ajaib!".format(username))
        else:
            print("Username atau password salah. Silahkan coba lagi.")                                  # Apabila username/password salah
            sys.exit()
    except(NameError):
        print("Username atau password salah. Silahkan coba lagi.")
        sys.exit()
    return currentuser

# F01 : Register
def register(role, users):
    # Realisasi fungsi register
    isUsed = False
    if role == 'user':                                                                                                      # Validasi role
        print("Anda tidak memiliki kewenangan untuk melakukan aksi ini!")
    else:
        temp = {}                                                                                                           # Append user baru
        temp['ID'] = str(len(users) + 1)
        temp['nama'] = input("Masukkan nama: ").title()
        temp['username'] = input("Masukkan username: ")
        temp['alamat'] = input("Masukkan alamat: ")
        temp['password'] = str(hashing(input("Masukkan password: ")))
        temp['role'] = "user"
        for user in users:                                                                                                  # Validasi nama
            if temp['username'] == user['username']:
                isUsed = True
        if isUsed == True:                                                                                                  # Apabila namanya sama
            print("Username {} telah digunakan, harap register ulang dengan username berbeda.".format(temp['username']))
        else:
            users.append(temp)
            print("User {} telah berhasil diregister ke dalam Kantong Ajaib.".format(temp['nama']))
    return users


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
