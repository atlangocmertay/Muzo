a = 1
while a == 1:
        soru = input("""
        (1) topla
        (2) çıkar
        (3) çarp
        (4) böl
        (5) karesini hesapla
        (6) karekök hesapla
        çıkmak için (q) 'yu tuşlayınız.
        """)
        if soru == 'q':
            print('çıkış yapılıyor...')
            a = 0
        elif soru == '1':
            top1 = int(input('İlk sayıyı giriniz: '))
            top2 = int(input('İkinci sayıyı giriniz:'))
            print(top1, '+', top2, '=', top1 + top2)
        elif soru == '2':
            cikar1 = int(input('İlk sayıyı giriniz: '))
            cikar2 = int(input('İkinci sayıyı giriniz:'))
            print(cikar1, '-', cikar2, '=', cikar1 - cikar2)
        elif soru == '3':
            carp1 = int(input('İlk sayıyı giriniz: '))
            carp2 = int(input('İkinci sayıyı giriniz:'))
            print(carp1, '*', carp2, '=', carp1 - carp2)
        elif soru == '4':
            bol1 = int(input('İlk sayıyı giriniz: '))
            bol2 = int(input('İkinci sayıyı giriniz:'))
            print(bol1, '/', bol2, '=', bol1 / bol2)
        elif soru == '5':
            kare1 = int(input('Karesini hesaplamak istediğiniz sayıyı giriniz: '))
            print(kare1, 'sayısının karesi = ', kare1 ** 2)
        else:
            print('doğru gir sayıları piç')
            print('lütfen tekrar deneyiniz')
            print(soru)
