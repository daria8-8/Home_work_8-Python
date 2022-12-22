import csv
import pandas as pd
import json
def export_data_csv():
   with open('phone_book.txt', 'r', encoding="cp437", errors='ignore') as infile, open('phone_book.csv', 'w', encoding="cp437", errors='ignore') as outfile:
        stripped = (line.strip() for line in infile)
        lines = (line.split(",") for line in stripped if line)
        writer = csv.writer(outfile)
        writer.writerow(['surname', 'name', 'birth_date', 'phone_number', 'salary']) 
        writer.writerows(lines)

def export_data_json():
    dict1 = {}
    fields =['surname', 'name', 'birth_date', 'phone_number', 'salary']
    with open('phone_book.txt') as fh:
      l = 1
      for line in fh:
          description = list( line.strip().split(',', 5))
          sno ='#'+str(l)
          i = 0
          dict2 = {}
          while i<len(fields):
                dict2[fields[i]]= description[i]
                i = i + 1
          dict1[sno]= dict2
          l = l + 1    
    out_file = open('phone_book.json', 'w')
    json.dump(dict1, out_file, indent = 5)

def create_xlsx():
   df = pd.read_csv('phone_book.csv')
   df.to_excel('phone_book.xlsx', 'Sheet1')

def import_data(data, sep=None):
    with open('phone_book.txt', 'a+', encoding="cp437", errors='ignore') as file:
        if sep == None:
            for i in data:
                file.write(f"{i}\n")
            file.write(f"\n")
        else:
            file.write(sep.join(data))
            file.write(f"\n")

def search_data(word, data):
    if len(data) > 0:
        for item in data:
            if word in item:
                return item
    else:
        return None

def cut_line():
    with open('phone_book.txt', 'r') as file:
        data = []
        for line in file:
            if ',' in line:
                temp = line.strip().split(',')
                data.append(temp)
    return data

def find_salary():
  with open('phone_book.txt', 'r') as file:
    lst = []
    min = int(input("Введите минимум: "))
    max = int(input("Введите максимум: "))
    for line in file:
        if ',' in line:
            temp = line.strip().split(',')
            lst.append(temp[4])
    salary = list(map(int, lst))
    lst = (list(filter(lambda x: min <= x <= max, salary)))
    return lst

def f_s(lst, data):
        lst_1 = list(map(str, lst))
        new_list = []
        print(lst_1)
        for item in data:
          for i in lst_1:
            if i in item:
                temp=item
                new_list.append(temp)
        return(new_list)
