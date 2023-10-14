import os

def print_title(text:str, title_length=30):
    print('-' * title_length)
    print(text.center(title_length))
    print('-' * title_length)

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


def show_menu():
    os.system('cls')
    print_title('CaloryTracker')
    choice = show_and_select_options(['Profil', 'Makan', 'Olahraga'])

    if choice == -1:
        return show_menu()
    
    if choice == 1:
        profil()
    elif choice == 2:
        makan()
    elif choice == 3:
        olahraga()

def profil():
    os.system('cls')
    print_title('Profil')
    # TODO: Implement this functions

def makan():
    os.system('cls') 
    print_title('Makan')
    # TODO: Implement this functions

def olahraga():
    os.system('cls')
    print_title('Olahraga')
    # TODO: Implement this functions
    # buat olahraga kebanyakan rumusnya sama
    # MET x Berat Badan (kg) x Waktu (jam)
    # kecuali olahraga yang bobotnya itu dari diri sendiri (push up, pull up, sit up)
    # (Waktu Latihan (jam) x MET x Berat Badan (kg)) / 200

show_menu()