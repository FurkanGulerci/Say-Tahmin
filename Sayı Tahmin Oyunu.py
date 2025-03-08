import random

print("Sayı Tahmin Oyununa Hoşgeldiniz!" + "\n" + "Her Oyun 5 Hakkınız var! " + "\n" + "Haklar bittiğinde oyun biter..." + "\n" + "Bir Zorluk Seviyesi Seçiniz ? " + "\n" + "Kolay - 1 ile 50" + "\n" + "Orta - 1 ile 100" + "\n" + "Zor - 1 ile 200")

while True:
    Oyun_Türü = input("Oyun Türü:" + "\n " + "1-Oyuncu vs Bilgisayar" + "\n" + "2-Bilgisayar vs Oyuncu" + "\n" + "Oyun Türünü Seçiniz:")
    if Oyun_Türü == "1":
        print("Oyuncu Sayıyı Bulmaya Çalışacak, Zorluk Seviyenizi Seçiniz. !")
        while True:
            Seçiminiz = input("Seçiminiz: ")
            Hakkınız = 5

            if Seçiminiz.lower() == "kolay":
                print("Kolay Seviye Seçildi! 1 ile 50 Arası Sayılar Tahmin Edilecek!")
                Sayı = random.randint(1, 50)
            elif Seçiminiz.lower() == "orta":
                print("Orta Seviye Seçildi! 1 ile 100 Arası Sayılar Tahmin Edilecek!")
                Sayı = random.randint(1, 100)
            elif Seçiminiz.lower() == "zor":
                print("Zor Seviye Seçildi! 1 ile 200 Arası Sayılar Tahmin Edilecek!")
                Sayı = random.randint(1, 200)
            else:
                print("Geçersiz Seçim!")
                continue

            while Hakkınız > 0:
                Tahmin = int(input("Tahmininiz: "))
                if Tahmin < Sayı:
                    print("Daha Yüksek Bir Sayı Giriniz...")
                    Hakkınız -= 1
                    print("Kalan Hak: ", Hakkınız)
                elif Tahmin > Sayı:
                    print("Daha Düşük Bir Sayı Giriniz...")
                    Hakkınız -= 1
                    print("Kalan Hak: ", Hakkınız)
                else:
                    print("Tebrikler Doğru Tahmin Ettiniz!")
                    break

                if Hakkınız == 0:
                    print("Hakkınız Bitti! Doğru Sayı: ", Sayı)
                    break
            Tekrar = input("Tekrar Oynamak İster misiniz? (evet/hayır): ").lower()
            if Tekrar == "hayır":
                print("Oyun Sonlandırıldı.")
                break
    if Oyun_Türü == "2":
        print("Bilgisayar Sayıyı Bulmaya Çalışacak, Zorluk Seviyenizi Seçiniz. !")
        Seçiminiz = input("Zorlu Seviyesi Seçiniz: ")
        if Seçiminiz.lower() == "kolay":
            min_sayı = 1
            max_sayı = 50
        elif Seçiminiz.lower() == "orta":
            min_sayı = 1
            max_sayı = 100
        elif Seçiminiz.lower() == "zor":
            min_sayı = 1
            max_sayı = 200
        while True:

            Hakkınız = 5
            Hakkınız = print("Kalan Hak: ", Hakkınız)
            
            print("Kolay Seviye Seçildi! 1 ile 50 Arası Sayılar Tahmin Edilecek!")
            Bilgisayarın_Tahmini = random.randint(min_sayı, max_sayı)
            print("Bilgisayarın Tahmini: ", Bilgisayarın_Tahmini)
            response = input("1-Yukarı 2-Aşağı 3-Doğru: ")
               
            if response == "1":
                min_sayı = Bilgisayarın_Tahmini 
                max_sayı = 50
            elif response == "2":
                max_sayı = Bilgisayarın_Tahmini
                min_sayı = 1
            elif response == "3":
                print("Tebrikler!")
                break
            else:
                print("Geçersiz Seçim!")
                continue
        