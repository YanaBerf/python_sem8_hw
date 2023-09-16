import os
my_file = open("phones.txt", "w+")

def write_to_file(path1):
    tmp_line = input("Введите ФИО и телефон: ")
    with open('phones.txt', "a") as file1:
        file1.write(tmp_line + "\n")


def del_file(path1, to_delete):
    with open('phones.txt', 'r') as file1:
        del_list= file1.readlines()
        print(del_list)
        with open('phones.txt','w') as file1:
             for line in del_list:
                if to_delete not in line:
                    file1.write(line)
    with open('phones.txt', "r") as file1:
        return file1.read()


def change_file(path1, to_change, new_write):
    with open('phones.txt', "r") as file1:
        list1 = file1.readlines()
        print(list1)
        with open('phones.txt', "w") as file1:
            for line in list1:
                if to_change in line:
                    line = new_write + '\n'
                file1.write(line)
    with open('phones.txt', "r") as file1:
        return file1.readlines()
    

def search_file(path1, search_input):
    with open('phones.txt', "r") as file1:
        lst_1 = file1.readlines()
        flag1 = False
        result = "\n"
        for line in lst_1:
            if search_input in line:
                result = result + line
                flag1 = True
        if not flag1:
            result = "Извините, такой записи нет\n"
    return result



def show_all(path1):
    with open('phones.txt', "r") as file1:
        return file1.read()


def get_user_intention():
    txt_zapros = "Введите номер команды, которую хотите выполнить.\n" \
                 "1. Записать новые данные в файл?\n" \
                 "2. Найти конкретную запись в файле\n" \
                 "3. Вывести весь файл\n" \
                 "4. Какие данные нужно удалить?\n" \
                 "5. Какие данные нужно изменить?\n" \
                 "6. Выйти из программы.\n"
    
    a = None
    while a != '6':
        a = input(txt_zapros)
        if a == '1':
            write_to_file(os.getcwd())
        elif a == '2':
            to_search = input("Что ищем? ")
            result = search_file(os.getcwd(), to_search)
            print(result)
        elif a == '3':
            result = show_all(os.getcwd())
            print(result)
        elif a == '4':
            to_delete = input('Что удалить? ')
            #new_change = input('Введите изменения: ')
            result = del_file(os.getcwd(), to_delete)
            print(result)
        elif a == '5':
            to_change = input('что изменить? ')
            new_write = input('новая запись: ')
            result = change_file(os.getcwd(), to_change, new_write)
            print(result)

get_user_intention()