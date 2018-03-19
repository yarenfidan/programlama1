yazilimGeliri = int(input("İlk 6 Aydaki Yazılım Gelirini giriniz: "))
finansmanGeliri=int(input("İlk 6 Aydaki Finansman Gelirini giriniz: "))
urunSatisGeliri=int(input("İlk 6 Aydaki Ürün Satış Gelirini giriniz: "))
calisanMaaslari=int(input("İlk 6 Aydaki Çalışan Maaşlarını giriniz: "))
kiraGideri=int(input("İlk 6 Aydaki Kira Giderini giriniz: "))
donanimMaliyeti=int(input("İlk 6 Aydaki Donanım Maliyetini giriniz: "))


def ilk6AyGelir(yazilimGeliri,finansmanGeliri,urunSatisGeliri):
    global ilkToplamGelir
    ilkToplamGelir=yazilimGeliri+finansmanGeliri+urunSatisGeliri
    return ilkToplamGelir

def ilk6AyGider(calisanMaaslari,kiraGideri,donanimMaliyeti):
    global ilkToplamGider
    ilkToplamGider=calisanMaaslari+kiraGideri+donanimMaliyeti
    return ilkToplamGider

def ilk6AyKarH(ilkGelir,ilkGider):
    ilk6AyKar=ilkGelir-ilkGider
    return ilk6AyKar

ilkGelir=ilk6AyGelir(yazilimGeliri,finansmanGeliri,urunSatisGeliri)
ilkGider=ilk6AyGider(calisanMaaslari,kiraGideri,donanimMaliyeti)
ilk6AyKarH(ilkGelir,ilkGider)


ikinciYazilimGeliri = int(input("Son 6 Aydaki Yazılım Gelirini giriniz: "))
sponsorlukGeliri=int(input("Son 6 Aydaki Sponsorluk Gelirini giriniz: "))
eTicaretGeliri=int(input("Son 6 Aydaki E-Ticaret Gelirini giriniz: "))
ikinciUrunSatisGeliri=int(input("Son 6 Aydaki Ürün Satış Gelirini giriniz: "))
ikinciCalisanMaaslari=int(input("Son 6 Aydaki Çalışan Maaşlarını giriniz: "))
ikinciKiraGideri=int(input("Son 6 Aydaki Kira Giderini giriniz: "))
bakimMaliyeti=int(input("Son 6 Aydaki Bakım Maliyetini giriniz: "))

def son6AyGelir(ikinciyazilimGeliri,sponsorlukGeliri,eTicaretGeliri,ikinciUrunSatisiGeliri):
    global sonToplamGelir
    sonToplamGelir=ikinciYazilimGeliri+sponsorlukGeliri+eTicaretGeliri+ikinciUrunSatisGeliri
    return  sonToplamGelir

def son6AyGider(calisanMaaslari,ikinciKiraGideri,bakimMaliyeti):
    global sonToplamGider
    sonToplamGider=calisanMaaslari+ikinciKiraGideri+bakimMaliyeti
    return sonToplamGider

def son6AyKarH(sonGelir,sonGider):
    son6AyKar=sonGelir-sonGider
    return  son6AyKar


sonGelir=son6AyGelir(ikinciYazilimGeliri,sponsorlukGeliri,eTicaretGeliri,ikinciUrunSatisGeliri)
sonGider=son6AyGider(calisanMaaslari,ikinciKiraGideri,bakimMaliyeti)

def karFarkiH(ilkKar,sonKar,):
    global karFarki
    karFarki=sonKar-ilkKar
    print(karFarki)

    if karFarki>=5000:
        print("işletme çok karlı")
    elif (1000<=karFarki<=5000):
        print("İşletme karı normal")
    else:
        print("İşletme yeterince karda değil")

ilkKar=ilk6AyKarH(ilkGelir,ilkGider)
sonKar=son6AyKarH(sonGelir,sonGider)
karFarkiH(ilkKar, sonKar)


