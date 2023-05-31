from . import Operasi

DB_NAME = "data.txt"
TEMPLATE = {
    "pk":"XXXXXX",
    "date_add":"yyyy-mm-dd",
    "nama":255*" ",
    "kategori":255*" ",
    "alamat":255*" ",
    "email":255*" ",
    "telepon":100*" "
}


def init_console():
    try:
        with open(DB_NAME,"r") as file:
            print("database tersedia, init done!")
    except:
        print("database tidak ditemukan, silahkan membuat database baru")
        Operasi.create_first_data()
        # with open(DB_NAME,"w", encoding="utf-8") as file:
        #     nama = input("nama: ")
        #     telepon = input("telepon: ") 
        #     alamat = input("alamat: ")
        #     email = input("email: ")
        #     data_str = f"{nama},{telepon},{alamat},{email}"
        #     file.write(data_str)
