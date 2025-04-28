def Menu():
    print("\n\n=====================")
    print("Konversi Satuan Meter")
    print("=====================")
    
    
    satuanAwal = input("(+)Satuan Awal (km, hm, dam, m, dm, cm, mm)> ")
    satuanTujuan = input("(+)Satuan tujuan (km, hm, dam, m, dm, cm, mm)> ")
    
    if satuanAwal == satuanTujuan:
        print("(!)Satuan awal tidak boleh sama dengan satuan tujuan")
        Menu()
    
    nilaiAwal = float(input(f"(+)  Nilai {satuanAwal}              > "))
    
    def Km():
            if(satuanAwal == "km" and satuanTujuan == "hm"):
                hasil = nilaiAwal * 10
                print(f"Hasil dari {satuanAwal} ke {satuanTujuan} = {hasil}")
            elif(satuanAwal == "km" and satuanTujuan == "dam"):
                hasil = nilaiAwal * 100
                print(f"Hasil dari {satuanAwal} ke {satuanTujuan} = {hasil}")
            elif(satuanTujuan == "km" and satuanTujuan == "m"):
                hasil = nilaiAwal * 1000
                print(f"Hasil dari {satuanAwal} ke {satuanTujuan} = {hasil}")
            elif(satuanAwal == "km" and satuanTujuan == "dm"):
                hasil = nilaiAwal * 10000
                print(f"Hasil dari {satuanAwal} ke {satuanTujuan} = {hasil}")
            elif(satuanAwal == "km" and satuanTujuan == "cm"):
                hasil = nilaiAwal * 100000
                print(f"Hasil dari {satuanAwal} ke {satuanTujuan} = {hasil}")
            elif(satuanAwal == "km" and satuanTujuan == "mm"):
                hasil = nilaiAwal * 1000000
                print(f"Hasil dari {satuanAwal} ke {satuanTujuan} = {hasil}")
    Km()


    def Hm():
            if(satuanAwal == "hm" and satuanTujuan == "km"):
                hasil = nilaiAwal / 10
                print(f"Hasil dari {satuanAwal} ke {satuanTujuan} = {hasil}")
            elif(satuanAwal == "hm" and satuanTujuan == "dam"):
                hasil = nilaiAwal * 10
                print(f"Hasil dari {satuanAwal} ke {satuanTujuan} = {hasil}")
            elif(satuanTujuan == "hm" and satuanTujuan == "m"):
                hasil = nilaiAwal * 100
                print(f"Hasil dari {satuanAwal} ke {satuanTujuan} = {hasil}")
            elif(satuanAwal == "hm" and satuanTujuan == "dm"):
                hasil = nilaiAwal * 1000
                print(f"Hasil dari {satuanAwal} ke {satuanTujuan} = {hasil}")
            elif(satuanAwal == "hm" and satuanTujuan == "cm"):
                hasil = nilaiAwal * 10000
                print(f"Hasil dari {satuanAwal} ke {satuanTujuan} = {hasil}")
            elif(satuanAwal == "hm" and satuanTujuan == "mm"):
                hasil = nilaiAwal * 100000
                print(f"Hasil dari {satuanAwal} ke {satuanTujuan} = {hasil}")
    Hm()


    def Dam():
            if(satuanAwal == "dam" and satuanTujuan == "km"):
                hasil = nilaiAwal / 100
                print(f"Hasil dari {satuanAwal} ke {satuanTujuan} = {hasil}")
            elif(satuanAwal == "dam" and satuanTujuan == "hm"):
                hasil = nilaiAwal / 10
                print(f"Hasil dari {satuanAwal} ke {satuanTujuan} = {hasil}")
            elif(satuanTujuan == "dam" and satuanTujuan == "m"):
                hasil = nilaiAwal * 10
                print(f"Hasil dari {satuanAwal} ke {satuanTujuan} = {hasil}")
            elif(satuanAwal == "dam" and satuanTujuan == "dm"):
                hasil = nilaiAwal * 100
                print(f"Hasil dari {satuanAwal} ke {satuanTujuan} = {hasil}")
            elif(satuanAwal == "dam" and satuanTujuan == "cm"):
                hasil = nilaiAwal * 1000
                print(f"Hasil dari {satuanAwal} ke {satuanTujuan} = {hasil}")
            elif(satuanAwal == "dam" and satuanTujuan == "mm"):
                hasil = nilaiAwal * 10000
                print(f"Hasil dari {satuanAwal} ke {satuanTujuan} = {hasil}")
    Dam()


    def M():
            if(satuanAwal == "m" and satuanTujuan == "km"):
                hasil = nilaiAwal / 1000
                print(f"Hasil dari {satuanAwal} ke {satuanTujuan} = {hasil}")
            elif(satuanAwal == "m" and satuanTujuan == "hm"):
                hasil = nilaiAwal / 100
                print(f"Hasil dari {satuanAwal} ke {satuanTujuan} = {hasil}")
            elif(satuanTujuan == "m" and satuanTujuan == "dam"):
                hasil = nilaiAwal / 10
                print(f"Hasil dari {satuanAwal} ke {satuanTujuan} = {hasil}")
            elif(satuanAwal == "m" and satuanTujuan == "dm"):
                hasil = nilaiAwal * 10
                print(f"Hasil dari {satuanAwal} ke {satuanTujuan} = {hasil}")
            elif(satuanAwal == "m" and satuanTujuan == "cm"):
                hasil = nilaiAwal * 100
                print(f"Hasil dari {satuanAwal} ke {satuanTujuan} = {hasil}")
            elif(satuanAwal == "m" and satuanTujuan == "mm"):
                hasil = nilaiAwal * 1000
                print(f"Hasil dari {satuanAwal} ke {satuanTujuan} = {hasil}")
    M()


    def Dm():
            if(satuanAwal == "dm" and satuanTujuan == "km"):
                hasil = nilaiAwal / 10000
                print(f"Hasil dari {satuanAwal} ke {satuanTujuan} = {hasil}")
            elif(satuanAwal == "dm" and satuanTujuan == "hm"):
                hasil = nilaiAwal / 1000
                print(f"Hasil dari {satuanAwal} ke {satuanTujuan} = {hasil}")
            elif(satuanTujuan == "dm" and satuanTujuan == "dam"):
                hasil = nilaiAwal / 100
                print(f"Hasil dari {satuanAwal} ke {satuanTujuan} = {hasil}")
            elif(satuanAwal == "dm" and satuanTujuan == "m"):
                hasil = nilaiAwal * 10
                print(f"Hasil dari {satuanAwal} ke {satuanTujuan} = {hasil}")
            elif(satuanAwal == "dm" and satuanTujuan == "cm"):
                hasil = nilaiAwal * 10
                print(f"Hasil dari {satuanAwal} ke {satuanTujuan} = {hasil}")
            elif(satuanAwal == "dm" and satuanTujuan == "mm"):
                hasil = nilaiAwal * 100
                print(f"Hasil dari {satuanAwal} ke {satuanTujuan} = {hasil}")
    Dm()

    def Cm():
            if(satuanAwal == "cm" and satuanTujuan == "km"):
                hasil = nilaiAwal / 100000
                print(f"Hasil dari {satuanAwal} ke {satuanTujuan} = {hasil}")
            elif(satuanAwal == "cm" and satuanTujuan == "hm"):
                hasil = nilaiAwal / 10000
                print(f"Hasil dari {satuanAwal} ke {satuanTujuan} = {hasil}")
            elif(satuanTujuan == "cm" and satuanTujuan == "dam"):
                hasil = nilaiAwal / 1000
                print(f"Hasil dari {satuanAwal} ke {satuanTujuan} = {hasil}")
            elif(satuanAwal == "cm" and satuanTujuan == "m"):
                hasil = nilaiAwal / 100
                print(f"Hasil dari {satuanAwal} ke {satuanTujuan} = {hasil}")
            elif(satuanAwal == "cm" and satuanTujuan == "dm"):
                hasil = nilaiAwal / 10
                print(f"Hasil dari {satuanAwal} ke {satuanTujuan} = {hasil}")
            elif(satuanAwal == "cm" and satuanTujuan == "mm"):
                hasil = nilaiAwal * 10
                print(f"Hasil dari {satuanAwal} ke {satuanTujuan} = {hasil}")
    Cm()

    def Mm():
            if(satuanAwal == "mm" and satuanTujuan == "km"):
                hasil = nilaiAwal / 1000000
                print(f"Hasil dari {satuanAwal} ke {satuanTujuan} = {hasil}")
            elif(satuanAwal == "mm" and satuanTujuan == "hm"):
                hasil = nilaiAwal / 100000
                print(f"Hasil dari {satuanAwal} ke {satuanTujuan} = {hasil}")
            elif(satuanTujuan == "mm" and satuanTujuan == "dam"):
                hasil = nilaiAwal / 10000
                print(f"Hasil dari {satuanAwal} ke {satuanTujuan} = {hasil}")
            elif(satuanAwal == "mm" and satuanTujuan == "m"):
                hasil = nilaiAwal / 1000
                print(f"Hasil dari {satuanAwal} ke {satuanTujuan} = {hasil}")
            elif(satuanAwal == "mm" and satuanTujuan == "dm"):
                hasil = nilaiAwal / 100
                print(f"Hasil dari {satuanAwal} ke {satuanTujuan} = {hasil}")
            elif(satuanAwal == "mm" and satuanTujuan == "cm"):
                hasil = nilaiAwal * 10
                print(f"Hasil dari {satuanAwal} ke {satuanTujuan} = {hasil}")
    Mm()


while True:
    Menu()