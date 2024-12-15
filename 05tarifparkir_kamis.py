def hitung_tarif_parkir():
    while True:
        try:
            jenis_kendaraan = input("Masukkan jenis kendaraan (motor/mobil): ").lower()
            if jenis_kendaraan not in ["motor", "mobil"]:
                print("Jenis kendaraan tidak valid. Harap pilih 'motor' atau 'mobil'.")
                continue
            jam = float(input("Berapa jam Anda parkir? "))
            if jam <= 0:
                print("Harap masukkan data dengan valid!")
            else:
                break
        except ValueError:
            print("Masukkan jumlah jam dalam angka!")

    # Tarif yang digunakan
    tarif_dua_jam_pertama_motor = 3000
    tarif_dua_jam_pertama_mobil = 3000
    tarif_melebihi_dua_jam_motor = 1000
    tarif_melebihi_dua_jam_mobil = 1500
    tarif_tambahan_melebihi_dua_puluh_empat_jam = 10000

    # Menghitung tarif berdasarkan jenis kendaraan dan waktu parkir
    if jenis_kendaraan == "motor":
        tarif_dua_jam_pertama = tarif_dua_jam_pertama_motor
        tarif_melebihi_dua_jam = tarif_melebihi_dua_jam_motor
    else:
        tarif_dua_jam_pertama = tarif_dua_jam_pertama_mobil
        tarif_melebihi_dua_jam = tarif_melebihi_dua_jam_mobil

    # Menghitung tarif berdasarkan waktu parkir
    if jam <= 2:
        biaya = tarif_dua_jam_pertama
    elif jam <= 24:
        biaya = tarif_dua_jam_pertama + (jam - 2) * tarif_melebihi_dua_jam
    else:
        biaya = tarif_dua_jam_pertama + (jam - 2) * tarif_melebihi_dua_jam + tarif_tambahan_melebihi_dua_puluh_empat_jam

    # Menampilkan total biaya
    print(f"Total tarif parkir: Rp{biaya}")

    ulang = input("Ingin menghitung ulang? (iya/tidak): ").lower()
    if ulang == "iya":
        hitung_tarif_parkir()

# Memanggil fungsi
hitung_tarif_parkir()