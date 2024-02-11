masuk = [100, 200]
keluar = [50, 25]


def money_tracker():
    while True:
        selected_menu = input("Pilih menu (masuk/keluar/sum masuk/sum keluar/sum all/exit): ").lower()
        if selected_menu == "exit":
            print("exiting program..")
            break
        pilih_menu(selected_menu)


def sum_masuk(masuk):
    total = 0
    for n in masuk:
        total += n

    return total


def sum_keluar(keluar):
    total = 0
    for n in keluar:
        total += n

    return total


def pilih_menu(selected_menu: str):
    if selected_menu == "sum masuk":
        print(sum_masuk(masuk))
        money_tracker()
    elif selected_menu == "sum keluar":
        print(sum_keluar(keluar))
        money_tracker()
    elif selected_menu == "masuk":
        try:
            uang_masuk = int(input("masukkan nominal uang masuk: "))
            masuk.append(uang_masuk)
            print("list uang masuk: ", masuk)
            money_tracker()
        except ValueError:
            uang_masuk = int(input("masukkan nominal uang masuk yang benar e.g. 1000, 2000: "))
            masuk.append(uang_masuk)
            print("list uang masuk: ", masuk)
            money_tracker()

    elif selected_menu == "keluar":
        try:
            uang_keluar = int(input("masukkan nominal uang keluar: "))
            keluar.append(uang_keluar)
            print("list uang keluar: ", keluar)
            money_tracker()
        except ValueError:
            uang_keluar = int(input("masukkan nominal uang keluar yang benar e.g. 200, 500: "))
            keluar.append(uang_keluar)
            print("list uang keluar: ", keluar)
            money_tracker()
    elif selected_menu == "sum all":
        print(sum_masuk(masuk) - sum_keluar(keluar))
    elif selected_menu == "exit":
        return
    else:
        money_tracker()


if __name__ == "__main__":
    money_tracker()
