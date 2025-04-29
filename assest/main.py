def konversi_satuan():
    print("\n\n=====================")
    print("Konversi Satuan Meter")
    print("=====================")

    satuan_awal = input("(+)Satuan Awal (km, hm, dam, m, dm, cm, mm)> ")
    satuan_tujuan = input("(+)Satuan tujuan (km, hm, dam, m, dm, cm, mm)> ")

    if satuan_awal == satuan_tujuan:
        print("(!)Satuan awal tidak boleh sama dengan satuan tujuan")
        return konversi_satuan()

    nilai_awal = float(input(f"(+)  Nilai {satuan_awal}            > "))

    conversion_factors = {
        "km": {"hm": 10, "dam": 100, "m": 1000, "dm": 10000, "cm": 100000, "mm": 1000000},
        "hm": {"km": 1/10, "dam": 10, "m": 100, "dm": 1000, "cm": 10000, "mm": 100000},
        "dam": {"km": 1/100, "hm": 1/10, "m": 10, "dm": 100, "cm": 1000, "mm": 10000},
        "m": {"km": 1/1000, "hm": 1/100, "dam": 1/10, "dm": 10, "cm": 100, "mm": 1000},
        "dm": {"km": 1/10000, "hm": 1/1000, "dam": 1/100, "m": 1/10, "cm": 10, "mm": 100},
        "cm": {"km": 1/100000, "hm": 1/10000, "dam": 1/1000, "m": 1/100, "dm": 1/10, "mm": 10},
        "mm": {"km": 1/1000000, "hm": 1/100000, "dam": 1/10000, "m": 1/1000, "dm": 1/100, "cm": 1/10}
    }

    if satuan_awal in conversion_factors and satuan_tujuan in conversion_factors[satuan_awal]:
        hasil = nilai_awal * conversion_factors[satuan_awal][satuan_tujuan]
        print(f"Hasil dari {satuan_awal} ke {satuan_tujuan} = {hasil}")
    else:
        print("(!)Satuan tidak dikenal")

while True:
    konversi_satuan()