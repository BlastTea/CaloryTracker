from functions import *

def print_title(text:str, title_length=30):
    print('-' * title_length)
    print(text.center(title_length))
    print('-' * title_length)

def show_and_select_options(options: list[str]):
    for i, x in enumerate(options):
        print(f'{i + 1}. {x}')
    print('0. Exit')
    
    input('Pilihan Anda : ')


def show_menu():
    print_title('CaloryTracker')
    show_and_select_options(['Makan', 'Olahraga'])

show_menu()