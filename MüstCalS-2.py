CalisanSure2016=150
toplamMüsteriSayisi2016=50
CalisanSure2017=CalisanSure2016+50
toplamMüsteriSayisi2017=toplamMüsteriSayisi2016+20

def hesapla2016(CalisanSure2016,toplamMüsteriSayisi2016):
    global  ilkMüsteri
    ilkMüsteri=CalisanSure2016/toplamMüsteriSayisi2016
    return ilkMüsteri



def hesapla2017(CalisanSure2017,toplamMüsteriSayisi2017):
    global ikinciMüsteri
    ikinciMüsteri=CalisanSure2017/toplamMüsteriSayisi2017
    return ikinciMüsteri

def farkH(ilk,ikinci):
    global fark
    fark=ikinci-ilk
    print(fark)

ilk=hesapla2016(CalisanSure2016,toplamMüsteriSayisi2016)
ikinci=hesapla2017(CalisanSure2017,toplamMüsteriSayisi2017)
farkH(ilk,ikinci)



