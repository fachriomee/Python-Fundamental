
listPasienRS = [
    {
        'NAMA': 'KARTINI',
        'UMUR': 20,
        'BIAYABEROBAT': 25000
    },
    {
        'NAMA': 'KARTINO',
        'UMUR': 15,
        'BIAYABEROBAT': 15000
    },
    {
        'NAMA': 'KARTONI',
        'UMUR': 25,
        'BIAYABEROBAT': 20000
    }
]

cart = []

#menampilkan seluruh data(Menu Read Data)
def MenampilkanDaftarPasien() :
    print('DAFTAR PASIEN')
    print('INDEX\t| NAMA  \t| UMUR\t| BIAYABEROBAT')
    for i in range(len(listPasienRS)) :
        print(f'{i}'.ljust(8),f'|{listPasienRS[i]["NAMA"]}'.ljust(16),f'| {listPasienRS[i]["UMUR"]}'.ljust(8),f'| {listPasienRS[i]["BIAYABEROBAT"]}')

#menu create data
def MenambahkanPasien() :
    namaPasien = input('Masukkan Nama Pasien : ')
    UmurPasien = int(input('Masukkan Umur Pasien : '))
    BiayaBerobat = int(input('Masukkan Biaya Berobat : '))
    listPasienRS.append({
        'NAMA': namaPasien.upper(),
        'UMUR': UmurPasien,
        'BIAYABEROBAT': BiayaBerobat
    })
    MenampilkanDaftarPasien()
#menu delete data
def MenghapusListPasien() :
    MenampilkanDaftarPasien()
    indexPasien = int(input('Masukkan index pasien yang ingin dihapus : '))
    del listPasienRS[indexPasien]
    MenampilkanDaftarPasien()

#menu update data
def MembayarBiayaPengobatan() :
    MenampilkanDaftarPasien()
    while True :
        indexPasien = int(input('Masukkan index pasien yang ingin di bayar: '))
        UMUR = int(input('Masukkan umur pasien: '))
        if(UMUR != listPasienRS[indexPasien]['UMUR']) :
            print('umur salah')
        else :
            cart.append({
                'NAMA': listPasienRS[indexPasien]['NAMA'],  
                'BIAYABEROBAT': listPasienRS[indexPasien]['BIAYABEROBAT'], 
                'indexPasien': indexPasien
            })
            print('Isi Cart :')
            print('Nama\t| UMUR\t| BIAYABEROBAT')
            print(listPasienRS[indexPasien])
        checker = input('Mau membayar yang lain? (ya/tidak) = ')
        if(checker == 'tidak') :
            break

    print('Daftar Biaya Berobat:')
    print('Nama\t| UMUR\t| BIAYABEROBAT\t|') 
    BIAYABEROBAT = listPasienRS[indexPasien]['BIAYABEROBAT']  
    while True :
        print('Total Yang Harus Dibayar = {}'.format(BIAYABEROBAT))
        jmlUang = int(input('Masukkan jumlah uang : '))
        nama = input('Masukkan nama anda : ')
        if(jmlUang > BIAYABEROBAT) :
            kembali = jmlUang - BIAYABEROBAT
            print('Terima kasih {} \n\nUang kembali anda : {}'.format(nama, kembali))
            break
        elif(jmlUang == BIAYABEROBAT) :
            print('Terima kasih {}'.format(nama))
            break
        else :
            kekurangan = BIAYABEROBAT - jmlUang
            print('Maaf {}, Uang anda kurang sebesar {}'.format(nama, kekurangan))

#menu utama
while True :
    pilihanMenu = input('''
        Selamat Datang di Rumah Sakit Sentosa

        List Menu :
        1. Melihat Daftar Pasien Rawat Inap
        2. Menambahkan Pasien ke Dalam Daftar
        3. Menghapus Daftar Pasien Rawat Inap
        4. Melakukan Transaksi Pengobatan
        5. Exit Program

        Masukkan angka Menu yang ingin dijalankan : ''')
    if pilihanMenu == '1' :
        MenampilkanDaftarPasien()
    elif pilihanMenu == '2' :
        MenambahkanPasien()
    elif pilihanMenu == '3' :
        MenghapusListPasien()
    elif pilihanMenu == '4' :
        MembayarBiayaPengobatan()
    elif pilihanMenu == '5' :
        print('program berhenti untuk dijalankan')
        break
    