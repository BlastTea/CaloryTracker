import csv
import os
import datetime
import functools

def divider(length=30):
    print('-' * length)

def print_title(text:str, title_length=30):
    divider(title_length)
    print(text.center(title_length))
    divider(title_length)

def show_and_select_options(options: list[str]):
    for i, x in enumerate(options):
        print(f'{i + 1}. {x}')
    print('0. Exit')

    user_choice = None
    
    try:
        user_choice = int(input('Pilihan Anda : '))
    except ValueError:
        input('Pilihan tidak ditemukan')
        os.system('cls')
        return -1
    
    if user_choice == 0 or any(user_choice == i + 1 for i, v in enumerate(options)):
        return user_choice
    
    input('Pilihan tidak ditemukan')
    os.system('cls')
    return -1

def show_sign_in():
    global current_profil

    os.system('cls')
    print_title('CaloryTracker')
    nama = input('Nama : ')

    with open('profil.csv') as file:
        if len(list(filter(lambda e: e['nama'] == nama and e['password'] == input('Password : '), list(csv.DictReader(file))))) > 0:
            current_profil = nama
            show_menu()
            return
    
    input('Nama atau Password salah')
    show_sign_in()


def show_menu():
    os.system('cls')
    print_title('CaloryTracker')

    jumlah_kalori_value = jumlah_kalori()
    jumlah_kalori_terbakar_value = jumlah_kalori_terbakar()

    print(f'Jumlah kalori : {jumlah_kalori_value}')
    print(f'Jumlah kalori terbakar : {jumlah_kalori_terbakar_value}')
    print(f'Hari ini Anda kelebihan kalori, silahkan olahraga' if jumlah_kalori_value >= jumlah_kalori_terbakar_value else f'Hari ini Anda kekurangan kalori, silahkan makan')
    divider()
    choice = show_and_select_options(['Profil', 'Makan', 'Olahraga'])

    if choice == -1:
        return show_menu()
    
    if choice == 1:
        profil()
    elif choice == 2:
        makan()
    elif choice == 3:
        olahraga()

def jumlah_kalori():
    global current_profil

    try:
        return functools.reduce(lambda a, b: a + b, map(lambda m: float(m['kalori']), filter(lambda e: e['tanggal'] == datetime.date.today().isoformat() and e['nama'] == current_profil, list(csv.DictReader(open('makan.csv'))))))
    except:
        return 0

def jumlah_kalori_terbakar():
    global current_profil
    
    try:
        return functools.reduce(lambda a, b: a + b, map(lambda m: float(m['kalori_terbakar']), filter(lambda e: e['tanggal'] == datetime.date.today().isoformat() and e['nama'] == current_profil, list(csv.DictReader(open('olahraga.csv'))))))
    except:
        return 0

def profil():
    os.system('cls')
    print_title('Profil')

    while True:
        print('1. Profil Baru')
        print('2. Profil yang sudah ada')
        print('0. Kembali')

        user_choice = input('Pilihan Anda: ')

        if user_choice == '1':
            create_new_profile()
            break
        elif user_choice == '2':
            load_existing_profile()
            break
        elif user_choice == '0':
            show_menu()
            break
        else:
            print('Pilihan tidak valid. Silakan pilih nomor yang valid.')
    return


def create_new_profile():
    os.system('cls')
    print_title('Profil Baru')

    nama = input('Masukkan nama Anda: ')
    password = input('Masukkan password Anda: ')
    umur = input('Masukkan umur Anda: ')

    print('Pilih jenis kelamin:')
    print('1. Laki-laki')
    print('2. Perempuan')

    while True:
        try:
            pilihan_jenis_kelamin = int(input('Pilihan Anda (1/2): '))
            if pilihan_jenis_kelamin == 1:
                jenis_kelamin = 'Laki-Laki'
                break
            elif pilihan_jenis_kelamin == 2:
                jenis_kelamin = 'Perempuan'
                break
            else:
                print('Pilihan tidak valid. Silakan pilih 1 untuk Laki-laki atau 2 untuk Perempuan.')
        except ValueError:
            print('Masukkan nomor yang valid.')

    with open('profil.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([nama, password, umur, jenis_kelamin])

    os.system('cls')
    print('Profil baru telah dibuat.')
    input('Tekan Enter untuk kembali ke menu.')
    show_menu()

def load_existing_profile():
    global nama, umur, jenis_kelamin, current_profil

    with open('profil.csv', 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        data = list(reader)

        nama_list = [row[0] for row in data]
        print("Profil yang tersedia:")
        for i, nama_user in enumerate(nama_list):
            print(f"{i + 1}. {nama_user}")

        while True:
            try:
                pilihan = int(input('Pilih profil (nomor): '))
                if 1 <= pilihan <= len(nama_list):
                    selected_user = data[pilihan - 1]
                    nama, umur, jenis_kelamin = selected_user
                    current_profil = nama
                    os.system('cls')
                    print('Profil telah dimuat.')
                    print(f'Nama: {nama}')
                    print(f'Umur: {umur}')
                    print(f'Jenis Kelamin: {jenis_kelamin}')
                    input('Tekan Enter untuk kembali ke menu.')
                    show_menu()
                    return
                else:
                    print('Pilihan tidak valid. Silakan pilih nomor yang valid.')
            except ValueError:
                print('Masukkan nomor yang valid.')

def makan():
    os.system('cls') 
    print_title('Makan')
    makanan = input('Masukkan nama makanan : ')
    kalori = float(input('Masukkan jumlah kalori : '))

    with open('makan.csv', 'a', newline='') as file:
        csv.writer(file).writerow([current_profil, makanan, kalori, datetime.date.today()])

    show_menu()

def olahraga():
    global current_profil

    os.system('cls')  
    print_title('Olahraga')

    hitung_olahraga = lambda bobot, waktu, met: bobot * waktu * met
    hitung_olahraga_diri_sendiri = lambda waktu, met, bobot: (waktu * met * bobot) / 200

    met_olahraga = 7.0 
    berat_badan = float(input("Masukkan berat badan (kg): "))
    waktu = float(input("Masukkan waktu latihan (jam): "))

    print("Pilih jenis olahraga:")
    print("1. Olahraga umum (MET x Berat Badan x Waktu)")
    print("2. Olahraga diri sendiri (MET x Waktu x Berat Badan / 200)")
    pilihan = int(input("Pilihan: "))

    if pilihan == 1:
        hasil = hitung_olahraga(berat_badan, waktu, met_olahraga)
    elif pilihan == 2:
        hasil = hitung_olahraga_diri_sendiri(waktu, met_olahraga, berat_badan)
    else:
        print("Pilihan tidak valid")
        return
    input(f'Kalori terbakar: {hasil}')

    with open('olahraga.csv', 'a', newline='') as file:
        csv.writer(file).writerow([current_profil, berat_badan, waktu, hasil, datetime.date.today()])

    show_menu()

show_sign_in()
