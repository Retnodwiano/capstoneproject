
# NRM adalah nomer rekam medis 

daftar_pasien = [{'NRM': 'PWD001','Nama' : 'Adinda Utami','Umur': 30,'Gender': 'Wanita','Diagnosa':'Hipertensi'},
    {'NRM': 'PWD002','Nama' : 'Audi Saputra','Umur': 40,'Gender': 'Pria','Diagnosa':'Diabetes'},
    {'NRM': 'PWD003','Nama' : 'Nira Warna','Umur': 20,'Gender': 'Wanita','Diagnosa':'Tipes'},
    {'NRM': 'PWD004','Nama' : 'Wawan Ramadhan','Umur': 50,'Gender': 'Pria','Diagnosa':'Hipertensi'},
    {'NRM': 'PWD005','Nama' : 'Tyna Jayanti ','Umur': 60,'Gender': 'Wanita' ,'Diagnosa':'Hipertensi'}]

def tampil():
     while True :
        menuTampil = int(input('''
                ========== Daftar Data Pasien ==========

                Pilihan Menu :
                1. Menampilkan Data seluruh Pasien
                2. Menampilkan Data Pasien Tertentu
                3. Kembali ke Menu Utama

                Masukan Sub Menu Tampilan? [1-3]:'''))
        if (menuTampil == 1):
            print('Daftar seluruh Pasien Rumah Sakit Purwadhika')
            for i in range(len(daftar_pasien)):
                print('NRM:',daftar_pasien[i]['NRM'],', Nama:',daftar_pasien[i]['Nama'],', Umur:',daftar_pasien[i]['Umur'],', Gender:',daftar_pasien[i]['Gender'],',Diagnosa:',daftar_pasien[i]['Diagnosa'])
        
        elif (menuTampil == 2 ):
            print('Data Pasien Tertentu Rumah Sakit Purwadhika')
            inputData = input('Masukan NRM:').upper()
            for j,i in enumerate(daftar_pasien) :
                if (i['NRM'] == inputData):
                    print('\nBerikut Data Pasien dari NRM', inputData,':')
                    print('NRM:',i['NRM'], ', Nama:' , i['Nama'],',Umur:', i['Umur'] ,',Gender:', i['Gender'] ,', Diagnosa:' , i['Diagnosa'] ,'\n')
                    break
                    
                elif i['NRM'] == daftar_pasien[-1]['NRM']: 
                    print('Tidak Ada Data Pasien dengan NRM :',inputData,'\n')
                    break
                
        elif (menuTampil == 3):
            break

        else: print('Pilihan yang anda Masukan salah!!!')

def create():
    while True:
        menuCreate = int(input('''
                ========== Menambahkan Data Pasien ==========

                Pilihan Menu :
                1. Tambah Data Pasien
                2. Kembali ke Menu Utama

                Masukan Sub Menu Create [1-2]: '''))
        
        if (menuCreate == 1):
            print('Masukan Data Pasien yang ingin ditambah')
            tambah_NRM = input('Masukan NRM :').upper()

            for i in daftar_pasien:
                if (i['NRM']== tambah_NRM):
                    print('Nomor Rekam Medis',tambah_NRM,'sudah Ada')
                    break

                elif i['NRM'] == daftar_pasien[-1]['NRM']:
                    tambahNama = input('Masukan Nama:').capitalize()
                    tambahUmur = int(input ('Masukan Umur:'))
                    tambahGender = input('Masukan Gender:').capitalize()
                    tambahDiagnosa = input('Masukan Diagnosa:').capitalize()
                    daftar_pasien.append({
                        'NRM': tambah_NRM,
                        'Nama': tambahNama,
                        'Umur': tambahUmur,
                        'Gender': tambahGender,
                        'Diagnosa' : tambahDiagnosa})
                    print('Data Pasien Tersimpan')
                    print('Daftar Pasien :')
                    for i in range(len(daftar_pasien)):
                         print('NRM:',daftar_pasien[i]['NRM'],', Nama:',daftar_pasien[i]['Nama'],', Umur:',daftar_pasien[i]['Umur'],', Gender:',daftar_pasien[i]['Gender'],',Diagnosa:',daftar_pasien[i]['Diagnosa'])
                    break

        elif (menuCreate == 2):
            break

        else: print('Pilihan yang anda masukan salah!!!')


def update():
    while True:
        menu_Update= int(input('''
                ========== Mengubah Data Pasien ==========

                Pilihan Menu :
                1. Mengubah Data Pasien
                2. Kembali ke Menu Utama

                Masukan PIlihan Sub Update [1-2]: '''))

        if (menu_Update == 1):
            ubah_NRM = input('Masukan NRM:').upper()
            for j,i in enumerate(daftar_pasien):
                if (i['NRM'] == ubah_NRM) :
                    print('NRM:',i['NRM'],', Nama:',i['Nama'],', Umur:',i['Umur'],', Gender:',i['Gender'],',Diagnosa:',i['Diagnosa'])
                    while True :
                        ubahData = input('Apakah anda ingin mengubah Data?[y/n]:').upper()
                        if (ubahData == 'Y'):
                            inputKolom = input('Masukan Kolom yg ingin diubah:').capitalize()
                            inputValue = input('Masukan Data '+ inputKolom + 'Baru:').capitalize()

                            if inputKolom == 'NRM':
                                inputKolom = inputKolom.upper()

                            daftar_pasien[j][inputKolom] = inputValue
                            print('NRM:',daftar_pasien[j]['NRM'],', Nama:',daftar_pasien[j]['Nama'],', Umur:',daftar_pasien[j]['Umur'],', Gender:',daftar_pasien[j]['Gender'],',Diagnosa:',daftar_pasien[j]['Diagnosa'])
                            print('Data Terupdate')
                            break
                        
                        elif (ubahData == 'N'):
                            print('Data tidak dirubah')
                            break 
                    break

                elif i['NRM'] == daftar_pasien[-1]['NRM']:
                    print('\nData Nomor Rekam Medis', ubah_NRM ,'Tidak Ada\n')

        elif (menu_Update == 2):
            break

        else :
            print('Pilihan yang anda masukan salah!!!')


def delete():
    while True :
        menuDelete= int(input('''
                ========== Menghapus Data Pasien ==========

                Pilihan Menu :
                1. Hapus Data Pasien
                2. Kembali ke Menu Utama

                Masukan PIlihan Sub Delete [1-2]: '''))
        
        if (menuDelete == 1):
            print('Hapus Data Pasien')
            hapus_NRM = input('Masukan NRM:').upper()

            for j,i in enumerate(daftar_pasien):
                if(i['NRM'] == hapus_NRM):
                    print('NRM:',daftar_pasien[j]['NRM'],', Nama:',daftar_pasien[j]['Nama'],', Umur:',daftar_pasien[j]['Umur'],', Gender:',daftar_pasien[j]['Gender'],',Diagnosa:',daftar_pasien[j]['Diagnosa'])
                    while True:
                        hapusData = input('Apakah Anda yakin Ingin Hapus Data?[y/n]:').upper()
                        if (hapusData == 'Y'):
                            del daftar_pasien[j]
                            print('\nData Pasien', hapus_NRM, 'Terhapus')
                            break

                        elif (hapusData =='N'):
                            print('\nData Pasien', hapus_NRM, ' Tidak Terhapus')
                            break 
                    break

                elif i['NRM'] == daftar_pasien[-1]['NRM']:
                    print('\nData Nomor Rekam Medis', hapus_NRM ,'Tidak Ada\n')        

        elif (menuDelete ==2):
            break 

        else: print('Pilihan yang anda masukan salah!!!')


def menu_utama():
    while True :
        try:
            input_User = int(input('''
                Selamat Datang di Rumah Sakit Purwadhika:

                Pilihan Menu :
                1. Menampilkan Daftar Pasien
                2. Menambah Daftar Pasien
                3. Update Data Pasien 
                4. Delete Data Pasien 
                5. Exit Program

                Silahkan pilih Angka Menu yang ingin dijalankan : '''))
            if (input_User == 1):
                tampil()

            elif (input_User == 2):
                create()

            elif (input_User == 3):
                update()

            elif (input_User == 4):
                delete()

            elif (input_User == 5):
                print('SELESAI AND GOODBYE!!!')
                break

            else :
                print('Pilihan yang anda masukan salah!!!')
        except:
            print('Pilihan yang anda masukan salah!!!')
        

menu_utama()

