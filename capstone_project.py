import pyinputplus as pyip

employee = [
            {
                'ID' : 12008, 
                'Nama' : 'Budi',
                'Gender' : 'Pria',
                'Umur' : 30,
                'Religion' : 'Islam',
                'Bagian' : 'IT Dev',
                'Department' : 'IT',
                'Married': 'Yes',
                'Child' : 2,
                'noTelp' : '+62-877-4001-3745'
                },
            {
                'ID' : 15001,
                'Nama' : 'Rian',
                'Gender' : 'Pria',
                'Umur' : 27,
                'Religion' : 'Islam',
                'Bagian' : 'IT Opr',
                'Department' : 'IT',
                'Married': 'Yes',
                'Child' : 2,
                'noTelp' : '+62-819-5977-4621'
                }
            ]

### Show List Function (list)employee
def Show(data):
    print('=====================================Tabel Karyawan=========================================')
    print('ID\t|Nama\t|Gender\t|Umur\t|Agama\t|Bagian\t|Departemen |Menikah |Anak |no. Telp\t      |')
    print('-----------------------------------------------------------------------------------------------')
    for i in range(len(data)):
        print('{}\t|{}\t|{}\t|{}\t|{}\t|{}\t|{}\t    |{}     |{}    |{} |'.format(data[i]['ID'],data[i]['Nama'],data[i]['Gender'],data[i]['Umur'],data[i]['Religion'],data[i]['Bagian'],data[i]['Department'],data[i]['Married'],data[i]['Child'],data[i]['noTelp'],))

### Search Function (int)ID
def search(id):
    searched = [data for data in employee if data['ID'] == id]
    return searched

### show data sebelum diupdate
def showS(idn,datan):
    print('=====================================Tabel Karyawan=========================================')
    print('ID\t|Nama\t|Gender\t|Umur\t|Agama\t|Bagian\t|Departemen |Menikah |Anak |no. Telp\t      |')
    print('-----------------------------------------------------------------------------------------------')
    for i in range(len(datan)):
        if idn == datan[i]['ID']:
            # return i, datan[i]
            print('{}\t|{}\t|{}\t|{}\t|{}\t|{}\t|{}\t    |{}     |{}    |{} |'.format(datan[i]['ID'],datan[i]['Nama'],datan[i]['Gender'],datan[i]['Umur'],datan[i]['Religion'],datan[i]['Bagian'],datan[i]['Department'],datan[i]['Married'],datan[i]['Child'],datan[i]['noTelp'],))

### Read Data Function
def ReadData():
    read = True
    while read != 'Kembali ke Menu Utama':
        print('\n##---------Lihat DataBase Karyawan---------##\n')
        submenu1 = ["Tampilkan Seluruh Data", "Cari Data with ID", "Kembali ke Menu Utama"]
        read = pyip.inputMenu(submenu1, numbered=True, prompt="Silahkan Pilih Sub Menu Read Data [1-3]:\n")
        print(f"Anda memilih ==> {read}")
        if read == 'Tampilkan Seluruh Data':
            if len(employee) != 0 :
                print('\nDatabase Karyawan :')
                Show(employee)
            else:
                print('\n---------Database Employee Kosong ---------')
            continue
        elif read == 'Cari Data with ID':
            if len(employee) != 0:
                addID = pyip.inputInt('===> input ID yang ingin dicari : ', min=10000, max=99999)
                search_result = search(addID)
                if len(search_result) > 0:
                    Show(search_result)
                else:
                    print(f'\nTidak ada data dengan ID: {addID}\n')
            else: 
                print('\n##-------Database Karyawan Kosong-------##')
            continue
        else:
            print('Kembali ke Menu Utama\n')
            MainMenu()

### add Data Function
def addData():
    print('##---------Tambah Data Karyawan---------##\n')
    submenu2 = ["Menambah Karyawan Baru", "Kembali ke Menu Utama"]
    inpadd = pyip.inputMenu(submenu2, numbered=True, prompt="Silahkan Pilih Sub Menu Tambah Data Karyawan:\n")
    print(f"Anda memilih ==> {inpadd}\n")
    if inpadd == 'Menambah Karyawan Baru':
        addID = pyip.inputInt('input ID Karyawan Baru (max 5 digit) : ', min=10000, max=99999)
        id_exists = False
        for i in range(len(employee)):
            if addID == employee[i]['ID']:
                id_exists = True
                print(f'\n{addID} ==> "Already exists"\n')
                break   
        if not id_exists:
            submenu_R = ["Islam", "Kristen", "Hindu", "Budha", "Katolik"]
            maxID= max(data['ID'] for data in employee)
            new_id = maxID + 1
            print(f'ID sudah otomatis ter-Generate\nID Karyawan menjadi : {new_id}\n')
            newNama = pyip.inputStr('Nama Karyawan Baru : ',allowRegexes=['[A-Z][a-z]'], blockRegexes=[r'\d+'])
            nGender = pyip.inputChoice(['Pria','Wanita'], prompt='Pilih jenis kelamin (pria/wanita): ')
            nUmur = pyip.inputInt('Umur Karyawan : ', min=18, max=70)
            nReligion = pyip.inputMenu(submenu_R, numbered=True, prompt="Agama :\n")
            nBagian = pyip.inputStr('Bagian/Jabatan : ',allowRegexes=['[A-Z][a-z]'], blockRegexes=[r'\d+'])
            nDepartment = pyip.inputStr('Departemen : ',allowRegexes=['[A-Z][a-z]'], blockRegexes=[r'\d+'])
            nMarried = pyip.inputChoice(['Ya','Belum'], prompt='\nsudah menikah (ya/belum)? \n: ')
            nChild = pyip.inputInt('\t\t\tAnak : ', min=0, max=10)
            print('(Jumlah anak yang dapat ditanggung bpjs max 5)\n')
            nTelp = pyip.inputStr('No Telp : ',allowRegexes=[r'[0-9]{12}\d*'], blockRegexes=[r'\d+'])
            newKaryawan = [{
                    'ID' : new_id,
                    'Nama' : newNama,
                    'Gender' : nGender,
                    'Umur' : nUmur,
                    'Religion' : nReligion,
                    'Bagian' : nBagian,
                    'Department' : nDepartment,
                    'Married': nMarried,
                    'Child' : nChild,
                    'noTelp' : nTelp
                }]
            Show(newKaryawan)
            save_ = pyip.inputChoice(['Ya','Tidak'], prompt='\nSimpan data? (Ya/Tidak)\n')
            if save_ == 'Ya':
                employee.extend(newKaryawan)
                print('Data successfully saved\n')
                Show(employee)
            else:
                print('Data not saved!\n')
    else:
        MainMenu()
    addData()

### Update Data Function
def updateData():
    print('##---------Update Data Karyawan---------##\n')
    submenu3 = ["Ubah Data Karyawan", "Kembali ke Menu Utama"]
    subM3 = pyip.inputMenu(submenu3, numbered=True, prompt="Silahkan Pilih Sub Menu Ubah Data Karyawan:\n")
    print(f"Anda memilih ==> {subM3}\n")
    if subM3 == 'Ubah Data Karyawan':
        Show(employee)
        print('Data mana yang ingin Anda ubah?')
        addID = pyip.inputInt('Masukan ID Karyawan yg ingin diubah : ', min=10000, max=99999)
        
        idFound = False
        for i in range(len(employee)):
            idFound = False
            if addID == employee[i]['ID']:
                idFound = True
                print(f'\n{addID} ==> "ID exists"')
                showS(addID,employee)
                update_ = pyip.inputChoice(['Ya','Tidak'], prompt='\nUpdate data ini (Ya/Tidak)? :')
                if update_ == 'Ya':
                    
                    submenu3a = ["Ubah Nama Karyawan", "Ubah Jabatan Karyawan", "Ubah status Menikah", "Update jumlah Anak", "Ubah no Telp", "Kembali ke Menu Utama"]
                    subM3a = pyip.inputMenu(submenu3a, numbered=True, prompt="\nPilih Data yang ingin di update:\n")
                    if subM3a == 'Ubah Nama Karyawan':
                        newNama1 = pyip.inputStr('Revisi/Ubah Nama : ',allowRegexes=['[A-Z][a-z]'], blockRegexes=[r'\d+'])
                        update_1 = pyip.inputChoice(['Ya','Tidak'], prompt='Anda yakin ubah data ini (Ya/Tidak)? :')
                        if update_1 == 'Ya':
                            employee[i]['Nama'] = newNama1
                            showS(addID,employee)
                            print('\n====> Nama berhasil diupdate\n')
                            
                        else:
                            print('update Data dicancel\n')
                    elif subM3a == 'Ubah Jabatan Karyawan':
                        passwor = 'admin'
                        pasw = input('masukan password : ')
                        if pasw == passwor:
                            nBagian1 = pyip.inputStr('Bagian/Jabatan Baru : ',allowRegexes=['[A-Z][a-z]'], blockRegexes=[r'\d+'])
                            update_1 = pyip.inputChoice(['Ya','Tidak'], prompt='Anda yakin ubah data ini (Ya/Tidak)? :')
                            if update_1 == 'Ya':
                                employee[i]['Bagian'] = nBagian1
                                showS(addID,employee)
                                print('\n====> Jabatan berhasil diupdate\n')
                            else:
                                print('update Data dicancel\n')
                        else:
                            print('\npassword salah\n')
                    elif subM3a == 'Ubah status Menikah':
                        nMarried = pyip.inputChoice(['Ya','Belum'], prompt='\nsudah menikah (ya/belum)? : ')
                        update_1 = pyip.inputChoice(['Ya','Tidak'], prompt='Anda yakin ubah data ini (Ya/Tidak)? :')
                        if update_1 == 'Ya':
                            employee[i]['Married'] = nMarried
                            showS(addID,employee)
                            print('\n======> Selamat! Anda sudah lepas dari masa Lajang\n')
                        else:
                            print('update Data dicancel\n')
                    elif subM3a == 'Update jumlah Anak':
                        nChild = pyip.inputInt('Jumlah Anak menjadi: ', min=0, max=10)
                        update_1 = pyip.inputChoice(['Ya','Tidak'], prompt='Anda yakin ubah data ini (Ya/Tidak)? :')
                        if update_1 == 'Ya':
                            employee[i]['Child'] = nChild
                            showS(addID,employee)
                            print('\n====> Selamat! Anak Anda telah Lahir\n')
                        else:
                            print('update Data dicancel\n')
                    elif subM3a == 'Ubah no Telp':
                        nTelp = pyip.inputStr('No Telp Baru : ',allowRegexes=[r'[0-9]{12}\d*'], blockRegexes=[r'\d+'])
                        update_1 = pyip.inputChoice(['Ya','Tidak'], prompt='Anda yakin ubah data ini (Ya/Tidak)? :')
                        if update_1 == 'Ya':
                            employee[i]['noTelp'] = nTelp
                            showS(addID,employee)
                            print('\n====> Data berhasil diupdate\n')
                        else:
                            print('update Data dicancel\n')
                    else:
                        print('===> Kembali ke Menu Utama\n')
                        MainMenu()
                else:
                    print('\nupdate Data dicancel\n')
                # jangan continue  
                break
            else:
                idFound = False
                print('\n===>')
        if not idFound:
            print('\n===> ID tidak ditemukan\n')        
    else:
        print('Kembali ke Menu Utama\n')
        MainMenu()
    updateData()

### delete data function
def deleteData():
    print('##---------Hapus Data Karyawan---------##\n')
    submenu4 = ["Menghapus Data Karyawan", "Kembali ke Menu Utama"]
    inpdel = pyip.inputMenu(submenu4, numbered=True, prompt="Silahkan Pilih Sub Menu Hapus Data Karyawan:\n")
    print(f"Anda memilih ==> {inpdel}\n")
    if inpdel == 'Menghapus Data Karyawan':
        Show(employee)
        addID = pyip.inputInt('Masukan ID Karyawan yg ingin dihapus : ', min=10000, max=99999)
        # search_result = search(addID)
        for i in range(len(employee)):
            if addID == employee[i]['ID']:
                print(f'\n{addID} ==> ada ID ini\n')
                showS(addID,employee)
                del_ = pyip.inputChoice(['Ya','Tidak'], prompt='\nAnda yakin Hapus data ini? (Ya/Tidak)')
                if del_ == 'Ya':
                    del employee[i]
                    Show(employee)
                    print('\n ===> Data berhasil dihapus\n')
                else:
                    print('\n ===> Data tidak jadi dihapus\n')
                break
        else:
            print(f'\nTidak ada data dengan ID: {addID}\n')
    else:
        MainMenu()
    deleteData()

### Main Menu Function
def MainMenu():
    menu = ["Lihat Data Karyawan", "Menambahkan Data Karyawan", "Ubah Data Karyawan", "Menghapus Data Karyawan", "exit"]
    while True:
        slcmenu = pyip.inputMenu(menu, numbered=True, prompt="Pilih menu (masukkan Angka):\n")
        print(f"Anda memilih ==> {slcmenu}\n")

        if(slcmenu == 'Lihat Data Karyawan'):
            ReadData()
        elif(slcmenu == 'Menambahkan Data Karyawan'):
            addData()
        elif(slcmenu == 'Ubah Data Karyawan'):
            updateData()
        elif(slcmenu == 'Menghapus Data Karyawan'):
            deleteData()
        elif(slcmenu == 'exit'):
            exit()
        else:
            MainMenu()

print('\n-------------Selamat Datang di--------------')
print('##-------Aplikasi Database Karyawan-------##\n')
MainMenu()