from . import Operasi

def delete_console():
    read_console()
    while(True):
        print("Silakan pilih nomor buku yang akan didelete")
        no_index = int(input("Nomor index: "))
        data_index = Operasi.read(index=no_index)

        if data_index:
            data_break = data_index.split(',')
            pk = data_break[0]
            date_add = data_break[1]
            nama = data_break[2]
            kategori = data_break[3]
            alamat = data_break[4]
            email = data_break[5]
            telepon = data_break[6][:-1]

            # data yang ingin didelete
            print("\n"+"="*100)
            print("Data yang akan dihapus")
            print(f"1. nama\t\t: {nama:.20}")
            print(f"2. kategori\t: {kategori:.20}")
            print(f"3. alamat\t: {alamat:.20}")
            print(f"4. email\t: {email:.20}")
            print(f"5. telepon\t: {telepon:20}")    

            is_done = input("Apakah anda yakin ingin menghapus data tersebut (Y/N)? ")
            if is_done == "y" or is_done == "Y" :
                Operasi.delete(no_index)
                break
        else:
            print("nomor tidak valid, silahkan masukan lagi")

    print("data berhasil dihapus")





def update_console():
    read_console()
    while(True):
        print("pilih data yellow pages yang akan diupdate ")
        no_index = int(input("nomor index: "))
        data_index = Operasi.read(index=no_index)

        if data_index:
            break
        else:
            print("nomor tidak valid, silahkan input kembali")
        
    data_break = data_index.split(',')
    pk = data_break[0]
    date_add = data_break[1]
    nama = data_break[2]
    kategori = data_break[3]
    alamat = data_break[4]
    email = data_break[5]
    telepon = data_break[6][:-1]

    while(True):
        # data yang ingin diupdate
        print("\n"+"="*100)
        print("silahkan pilih data yang ingin anda rubah")
        print(f"1. nama\t\t: {nama:.40}")
        print(f"2. kategori\t: {kategori:.40}")
        print(f"3. alamat\t: {alamat:.40}")
        print(f"4. email\t: {email:.40}")
        print(f"5. telepon\t: {telepon:40}")

        # memilih mode untuk update
        user_option = input("pilih data [1,2,3,4,5]: ")

        print("\n"+"="*100)
        match user_option:
            case "1": nama = input("nama\t\t: ")
            case "2": kategori = input("kategori\t: ")
            case "3": alamat = input("alamat\t: ")
            case "4": email = input("email\t\t: ")
            case "5":     
                while(True):    
                    try:
                        telepon = input("telepon\t: ")
                        if len(str(telepon)) <= 12:
                            break     
                        else:
                            print("telepon harus angka (xxxxxxxxxxxx)")
                    except:
                        print ("telepon harus angka (xxxxxxxxxxxx)")
            case _: print("index yang dipilih tidak ada")    

        print("Data baru anda")
        print(f"1. nama\t: {nama:.40}")
        print(f"2. kategori\t: {kategori:.40}")
        print(f"3. alamat\t: {alamat:.40}")
        print(f"4. email\t: {email:.40}")
        print(f"5. telepon\t: {telepon:.40}")

        is_done = input("Apakah Update sudah sesuai (Y/N)? ")
        if is_done == "y" or is_done == "Y" :
            break

    Operasi.update(no_index,pk,date_add,telepon,nama,kategori,alamat,email)


# def update_console():
#     read_console()
#     while(True):
#         print("Silahkan pilih nomor buku yang akan di update")
#         no_index = int(input("Nomor index: "))
#         data_index = Operasi.read(index=no_index)
#         if data_index:
#             break
#         else:
#             print("nomor tidak valid, silahkan masukan lagi")
    
#     data_break = data_index.split(',')
#     pk = data_break[0]
#     date_add = data_break[1]
#     nama = data_break[2]
#     kategori = data_break[3]
#     alamat = data_break[4]
#     email = data_break[5]
#     telepon = data_break[6][:-1]
#     print(pk)
#     print(date_add)
#     print(nama)
#     print(kategori)
#     print(alamat)
#     print(email)
#     print(telepon)

    
#     while(True):
#         # data yang ingin diupdate
#         print("\n"+"="*100)
#         print("Silahkan pilih data apa yang ingin anda ubah")
#         print(f"1. Kategori\t: {kategori:.40}")
#         print(f"2. Nama\t\t: {nama:.40}")
#         print(f"3. alamat\t: {alamat:40}")
#         print(f"4. email\t: {email:40}")
#         print(f"5. telepon\t: {telepon:40}")

#         # memilih mode untuk update
#         user_option = input("Pilih data [1,2,3,4,5]: ")
#         print("\n"+"="*100)
#         match user_option:
#             case "1": kategori = input("kategori\t: ")
#             case "2": nama = input("nama\t: ")
#             case "3": alamat = input("alamat\t: ")
#             case "4": email = input("email\t: ")
#             case "5": telepon = input("telepon\t: ")

#         print("Data baru anda")
#         print(f"1. kategori\t: {kategori:.40}")
#         print(f"2. nama\t: {nama:.40}")
#         print(f"1. alamat\t: {alamat:.40}")
#         print(f"2. email\t: {email:.40}")
#         print(f"2. telepon\t: {telepon:.40}")
        
#         is_done = input("Apakah data sudah sesuai(y/n)? ")
#         if is_done == "y" or is_done == "Y":
#             break
    
#     Operasi.update(no_index,pk,date_add,alamat,kategori,nama,email,telepon)
            


def create_console():
    print("\n\n"+"="*100)
    print("Silahkan tambah data kontak yellow pages")
    nama = input("nama\t\t: ")
    kategori = input("kategori\t: ")
    alamat = input("alamat\t\t: ")
    email = input("email\t\t: ")
    while(True):    
        try:
            telepon = input("telepon\t\t: ")
            if len(str(telepon)) <= 12:
                break     
            else:
                print("telepon harus angka (xxxxxxxxxxxx)")
        except:
            print("telepon harus angka (xxxxxxxxxxxx)")
    


    Operasi.create(nama,kategori,alamat,email,telepon)
    print("\nberikut data baru anda")
    read_console()

def read_console(): 
    data_file = Operasi.read()
    # print(data_file)
    index = "No"
    nama = "Nama"
    kategori = "kategori"
    alamat = "alamat"
    email = "email"
    telepon = "telepon"

    # Header
    print("\n"+"="*122)
    print(f"{index:4} | {nama:20} | {kategori:20} | {alamat:30} | {email:20} | {telepon:10}")
    print("-"*122)
    # print("data")

    for index, data in enumerate(data_file):
        data_break = data.split(",")
        # print(data_break)
        pk = data_break[0]
        if len(data_break) >= 2:
            date_add = data_break[1]
        else:
            continue
        nama = data_break[2]
        kategori = data_break[3]
        alamat = data_break[4]
        email = data_break[5]
        telepon = data_break[6]
        print(f"{index+1:4} | {nama:.20} | {kategori:.20} | {alamat:.30} | {email:.20} | {telepon:9}",end="")
    # Footer
    print("="*122+"\n")
