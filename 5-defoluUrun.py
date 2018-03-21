#soru5

i = 1 # gun sayaci
toplamDefoluUrunS = 0
while 1:

    gunlukDefoluUrunS = int(input("Bugün kaç defolu ürün çıktı ?"))

    toplamDefoluUrunS += gunlukDefoluUrunS

    # defolu urun (!!!) orani (!!!)  %20 den fazlaysa
    if (toplamDefoluUrunS > (200 * i)):

        print(
            "Toplam defolu ürün oranı toplam uretiminizin %20 sinden fazla daha fazla uretim yapmamalısınız!")
        break


    print(i , " gün boyunca toplamda " ,
          (i * 200) , " adet ürün elde ettiniz. Bunlardan " , toplamDefoluUrunS , " tanesi defolu!")


    # gunluk defolu urun sayisi gunluk uretilen urun sayisindan %20 fazla oldugunda
    if (gunlukDefoluUrunS > (200*20/100)):

        print("Dikkat bugünkü defolu ürün sayısı cok fazladır.")

    i+=1

