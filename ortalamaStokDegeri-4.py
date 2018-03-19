dbasiKoltukSayisi=int(input("Koltuk Sayısını giriniz: "))
dbasiYatakSayisi=int(input("Yatak Sayısını giriniz: "))
dbasiDolapSayisi=int(input("Dolap Sayısını giriniz: "))


def donemBasiStokH(dbasiKoltukSayisi,dbasiYatakSayisi,dbasiDolapSayisi):
    global donemBasiStok
    donemBasiStok=dbasiKoltukSayisi+dbasiYatakSayisi+dbasiDolapSayisi
    return donemBasiStok

dsonuKoltukSayisi=25
dsonuYatakSayisi=20
dsonuDolapSayisi=10

def donemSonuStokH(dsonuKoltukSayisi,dsonuYatakSayisi,dsonuDolapSayisi):
    global donemSonuStok
    donemSonuStok=dsonuKoltukSayisi+dsonuYatakSayisi+dsonuDolapSayisi
    return donemSonuStok

def ortalamaStokH(donemBasi,donemSonu):
    global ortalamaStok
    ortalamaStok=(donemBasi+donemSonu)/2
    print(ortalamaStok)

donemBasi =donemBasiStokH(dbasiKoltukSayisi,dbasiYatakSayisi, dbasiDolapSayisi)
donemSonu =donemSonuStokH(dsonuKoltukSayisi, dsonuYatakSayisi, dsonuDolapSayisi)
ortalamaStokH(donemBasi,donemSonu)

