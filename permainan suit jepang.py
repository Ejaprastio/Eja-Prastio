import random


def pilihan_pemain():
    """Fungsi untuk meminta input pemain."""
    print("Pilih: 1 - Batu, 2 - Gunting, 3 - Kertas")
    return int(input("Masukkan pilihan Anda: "))


def pilihan_komputer():
    """Fungsi untuk menghasilkan pilihan acak komputer."""
    return random.randint(1, 3)


def menentukan_pemenang(pemain, komputer):
    """Fungsi untuk menentukan pemenang setiap putaran."""
    if pemain == komputer:
        return "Seri!"
    elif (pemain == 1 and komputer == 2) or (pemain == 2 and komputer == 3) or (pemain == 3 and komputer == 1):
        return "Anda Menang!"
    else:
        return "Anda Kalah!"


def main():
    skor_pemain = 0
    skor_komputer = 0
    putaran = 1

    while putaran <= 3:  # Ubah sesuai keinginan
        print(f"\nPutaran ke-{putaran}")

        pemain = pilihan_pemain()
        komputer = pilihan_komputer()

        print(f"Anda memilih: {pemain}")
        print(f"Komputer memilih: {komputer}")

        hasil_putaran = menentukan_pemenang(pemain, komputer)
        print(hasil_putaran)

        if "Menang" in hasil_putaran:
            skor_pemain += 1
        elif "Kalah" in hasil_putaran:
            skor_komputer += 1

        putaran += 1

    print("\n=== Hasil Akhir ===")
    print(f"Skor Anda: {skor_pemain}")
    print(f"Skor Komputer: {skor_komputer}")


if 'name' == "_main_":
    main()
