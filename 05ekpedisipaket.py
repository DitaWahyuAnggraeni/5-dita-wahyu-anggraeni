def hitung_biaya(berat, panjang, lebar, tinggi, wilayah):
    # Cek apakah wilayahnya adalah Kota atau Kabupaten Pasuruan
    if wilayah.lower() not in ['kota pasuruan', 'kabupaten pasuruan']:
        return "Wilayah tidak valid. Hanya menerima Kota dan Kabupaten Pasuruan."

    # Validasi berat minimal 1 kg
    if berat < 1:
        return "Berat minimal adalah 1 kg."

    # Harga dasar untuk 1 kg
    harga_per_kg = 8000

    # Cek dimensi paket
    if panjang > 50 or lebar > 50 or tinggi > 50:
        biaya_tambahan_dimensi = 50000
        harga_per_kg = 7000
    else:
        biaya_tambahan_dimensi = 0

    # Menghitung biaya total
    biaya_total = biaya_tambahan_dimensi + harga_per_kg * berat
    return f"Biaya pengiriman untuk paket dengan berat {berat} kg dan dimensi ({panjang}x{lebar}x{tinggi}) cm adalah: Rp {biaya_total}"

# Contoh penggunaan
wilayah = input("Masukkan wilayah (Kota atau Kabupaten Pasuruan): ")
berat = float(input("Masukkan berat paket (kg): "))
panjang = float(input("Masukkan panjang paket (cm): "))
lebar = float(input("Masukkan lebar paket (cm): "))
tinggi = float(input("Masukkan tinggi paket (cm): "))

biaya = hitung_biaya(berat, panjang, lebar, tinggi, wilayah)
print(biaya)