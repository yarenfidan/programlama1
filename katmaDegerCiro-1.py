x=int(input("Toplam Satış Miktarını Giriniz:"))
y=int(input("Hammadde Maliyetini Giriniz:"))
z=int(input("Bakım Onarım Giderlerini Giriniz:"))
t=int(input("Sevkiyat Giderlerini Giriniz:"))
f=int(input("Satın Alınan Hizmet Giderlerini Giriniz:"))
def KatmaDegerCiroFonk():
    KatmaDegerCiro=x-(y+z+t+f)
    return KatmaDegerCiro
if KatmaDegerCiroFonk()>=1000:
    print("İşletme katma değer cirosu yüksek")
elif KatmaDegerCiroFonk()<500:
    print("işletme katma değer cirosu düşük")
else:
    print("işletme katma değer cirosu normal")

