from model import export_data_csv, export_data_json, create_xlsx, import_data, search_data, cut_line, find_salary, f_s
from view import input_data

def sep_is():
    sep = input("Введите разделитель: ")
    if sep == "":
        sep = None
    return sep

def do_it():
    print("Что хотите сделать?\n\
    1 - импорт\n\
    2 - экспорт в csv\n\
    3 - экспорт в json\n\
    4 - создать xslx\n\
    5 - удалить контакт\n\
    6 - выборка по зп\n\
    7 - поиск контакта")
    ch = input("Введите цифру: ")
    if ch == '1':
        sep = sep_is()
        import_data(input_data(), sep)
    if ch == '2':
        export_data_csv()
    if ch == '3':
        export_data_json()
    if ch == '4':
        create_xlsx() 
    if ch == '5':
        word = input("Введите данные для удаления: ")
        INFILE = 'phone_book.txt'
        OUTFILE = 'phone_book_1.txt'
        with open(INFILE, 'r', encoding="utf-8") as infile, open(OUTFILE, 'w', encoding="utf-8") as outfile:
           for line in infile:
              if word not in line:
                 outfile.write(line)
        import os
        os.remove(INFILE)
        os.rename(OUTFILE, INFILE)
    if ch == '6':
        lst = find_salary()
        data = cut_line()
        new_list = f_s(lst,data)
        print('\n'.join(map(str, new_list)))
    if ch == '7':
        word = input("Введите данные для поиска: ")
        data = cut_line()
        item = search_data(word, data)
        if item != None:
             print("-"*110)
             print("|","surname".center(20),"|", "name".center(20),"|", "birth_date".center(20), "|","phone_number".center(20), "|", "salary".center(15), "|")
             print("-"*110)
             print("|", item[0].center(20),"|", item[1].center(20),"|",item[2].center(20),"|", item[3].center(20), "|", item[4].center(15), "|")
             print("-"*110)
        else:
            print("Данные не обнаружены")