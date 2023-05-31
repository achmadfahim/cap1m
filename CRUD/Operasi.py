from . import Database
from .Util import random_string
import time
import os

def delete(no_index):
    try:
        with open(Database.DB_NAME,'r') as file:
            counter = 0
            while(True):
                content = file.readline()
                if len(content) == 0:
                    break
                elif counter == no_index - 1:
                    pass
                else:
                    with open("data_temp.txt",'a',encoding="utf-8") as temp_file:
                        temp_file.write(content)
                counter += 1 
    except:
        print("database error") 

    os.replace("data_temp.txt",Database.DB_NAME)
    


def update(no_index,pk,date_add,telepon,nama,kategori,alamat,email):
    data = Database.TEMPLATE.copy()
    
    data["pk"] = pk
    data["date_add"] = date_add
    data["nama"] = nama + Database.TEMPLATE["nama"][len(nama):]
    data["kategori"] = kategori + Database.TEMPLATE["kategori"][len(kategori):]
    data["alamat"] = alamat + Database.TEMPLATE["alamat"][len(alamat):]
    data["email"] = email + Database.TEMPLATE["email"][len(email):]
    data["telepon"] = telepon + Database.TEMPLATE["telepon"][len(telepon):]

    data_str = f'{data["pk"]},{data["date_add"]},{data["nama"]},{data["kategori"]},{data["alamat"]},{data["email"]},{data["telepon"]}\n'

    panjang_data = len(data_str)

    try:
        with(open(Database.DB_NAME,'r+',encoding="utf-8")) as file:
            file.seek(panjang_data*(no_index-1))
            file.write(data_str)

    except:
        print("error saat update data")

# def update(no_index,pk,date_add,telepon,kategori,nama,alamat,email):
#     data = Database.TEMPLATE.copy()

#     data["pk"] = pk
#     data["date_add"] = date_add
#     data["nama"] = nama + Database.TEMPLATE["nama"][len(nama):]
#     data["kategori"] = kategori + Database.TEMPLATE["kategori"][len(kategori):]
#     data["alamat"] = alamat + Database.TEMPLATE["alamat"][len(alamat):]
#     data["email"] = email + Database.TEMPLATE["email"][len(email):]
#     data["telepon"] = telepon + Database.TEMPLATE["telepon"][len(telepon):]

#     data_str = f'{data["pk"]},{data["date_add"]},{data["nama"]},{data["kategori"]},{data["alamat"]},{data["email"]},{data["telepon"]}\n'
    
#     panjang_data = len(data_str)

#     try:
#         with open(Database.DB_NAME,'r+',encoding="utf-8") as file:
#             file.seek(panjang_data*(no_index-1))
#             file.write(data_str)
#     except:
#         print("error dalam update data")


def create(nama,kategori,alamat,email,telepon):
    
    data = Database.TEMPLATE.copy()
    
    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
    data["nama"] = nama + Database.TEMPLATE["nama"][len(nama):]
    data["kategori"] = kategori + Database.TEMPLATE["kategori"][len(kategori):]
    data["alamat"] = alamat + Database.TEMPLATE["alamat"][len(alamat):]
    data["email"] = email + Database.TEMPLATE["email"][len(email):]
    data["telepon"] = telepon + Database.TEMPLATE["telepon"][len(telepon):]

    data_str = f'{data["pk"]},{data["date_add"]},{data["nama"]},{data["kategori"]},{data["alamat"]},{data["email"]},{data["telepon"]}\n'
    # print(data_str)
    try:
        with open(Database.DB_NAME,'a',encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("data gagal ditambahkan")

    print(data)


def create_first_data():

    nama = input("nama\t\t: ")
    kategori = input("kategori\t: ") 
    alamat = input("alamat\t\: ")
    email = input("email\t: ")
    while(True):    
        try:
            telepon = input("telepon\t: ")
            if len(str(telepon)) <= 12:
                break     
            else:
                print("telepon harus angka (xxxxxxxxxxxx)")
        except:
            print("telepon harus angka (xxxxxxxxxxxx)")

    data = Database.TEMPLATE.copy()
    
    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
    data["nama"] = nama + Database.TEMPLATE["nama"][len(nama):]
    data["kategori"] = kategori + Database.TEMPLATE["kategori"][len(kategori):]
    data["alamat"] = alamat + Database.TEMPLATE["alamat"][len(alamat):]
    data["email"] = email + Database.TEMPLATE["email"][len(email):]
    data["telepon"] = telepon + Database.TEMPLATE["telepon"][len(telepon):]

    data_str = f'{data["pk"]},{data["date_add"]},{data["nama"]},{data["kategori"]},{data["alamat"]},{data["email"]},{data["telepon"]}\n'
    print(data_str)
    try:
        with open(Database.DB_NAME,'w',encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("gagal untuk input")

# def read(**kwargs):
#     try:
#         with open(Database.DB_NAME,'r') as file:
#             content = file.readlines()
#             jumlah_index = len(content)
#             # print(jumlah_index)
#             if "index" in kwargs:
#                 index_ = kwargs["index"]-1
#                 if index_ < 0 or index_ >jumlah_index:
#                     return False
#                 else: 
#                     return content[index_]
#             else:
#                 # print(content[kwargs["index"]-1])
#                 return content
#     except:
#         print("membaca database error")
#         return False

       
def read(**kwargs):
    try:
        with open(Database.DB_NAME, 'r') as file:
            content = file.readlines()
            jumlah_index = len(content)
            if "index" in kwargs:
                index_ = kwargs["index"]-1
                if index_ < 0 or index_ > jumlah_index:
                    return False
                else:    
                    return content[index_]
            else:
                return content
    except:
        print("Membaca database error")
        return False
    
