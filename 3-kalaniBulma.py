girilen=' '
toplam=0
while(girilen!=0):
    girilen=int(input("sayi gir:"))
    toplam+=(girilen%3)
print("kalanların tolamı",toplam)