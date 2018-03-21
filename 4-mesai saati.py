i = 1 #calisan Sayısı
butunPersonellereToplamAylikO  = 0

while (i < 51):
    j = 1  # hafta sayisi
    aylikToplamMesaiS = 0

    while (j<=4):
        soru = i,". çalışan ",j,". hafta kaç saat mesai yapmıştır?"
        haftalikMesaiS = int(input(soru))
        aylikToplamMesaiS += haftalikMesaiS

        j+=1

        if (aylikToplamMesaiS > 22):

            print("Bir personel aylık 22 saatten fazla mesai yapmamalı")
            aylikToplamMesaiS -= haftalikMesaiS


    personelAylikMaas = ((90*30) + (aylikToplamMesaiS * (90*10/100)))
    print("",i,". çalışan bu ay ",personelAylikMaas,"TL maaş alacaktır")

    butunPersonellereToplamAylikO += personelAylikMaas

    i += 1

print("İşletme bu ay personellerin toplam ",personelAylikMaas," TL ödeme yapacak.")

