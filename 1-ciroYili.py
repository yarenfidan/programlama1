satisM=500
birimSatisF=20
ciro=5000
i=0
while True:
    satisM=satisM+200
    birimSatisF=birimSatisF+10
    ciro=ciro+(satisM*birimSatisF)
    i=i+1
    if(ciro>500000):
        print(i/12," yıl sonra ciro 500.000 TL den fazla olacak")
        break