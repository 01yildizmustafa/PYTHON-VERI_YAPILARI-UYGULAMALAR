y = []


def çıkış():
    print()
    print("Çıkılıyor...")


def hata():
    print()
    print("Hatalı tuşlama!")


def veri_okuma():
    print()
    print("Mevcut liste:")
    print()
    print("     ",y)


def veri_ekleme():
    print()
    sor = input("Eklenecek veriyi giriniz: ")
    veri = sor
    ekleme = y.append(veri)
    print()
    print("İşlem başarılı")
    print()
    print("--Yeni liste: ")
    print("     {}".format(y))
    print()


def veri_güncelleme():
    print()
    print("Mevcut listeniz: ")
    print()
    print(y)
    print()
    sor0 = int(input("Değiştirilecek verinin indisini giriniz: "))
    print()
    print("Şu veri değiştirilecek: {}".format(y[sor0]))
    sor = input("Girilecek veri tipi nedir?: aritmetik(a) / diğer(d)").lower()
    while True:
        if sor == "a":
            print()
            sor1 = int(input("Yeni aritmetik* veriyi giriniz: "))
            y[sor0] = sor1
            print()
            print("İşlem başarılı!")
            print()
            print("Girilen yeni veri: {}".format(sor1))
            print()
            print("--Yeni Liste:")
            print("     {}".format(y))
            break
        elif sor == "d":
            print()
            sor1 = input("Yeni veri giriniz: ")
            y[sor0] = sor1
            print()
            print("İşlem başarılı!")
            print()
            print("Yeni veri: {}".format(sor1))
            print()
            print("--Yeni Liste:")
            print("     {}".format(y))
            break
        else:
            hata()
            return
    

def veri_silme():
    print()
    sor = int(input("Silinecek veriyi giriniz: "))
    veri = sor
    silme = y.remove(veri)
    print()
    print("İşlem başarılı")
    print()
    print("--Yeni liste: ")
    print("     {}".format(y))
    print()


def diğer_işlem():
    while True:
        print()
        print("--Diğer İşlemler")
        print("""
        (0) Çıkış
        (1) Toplam Veri
        (2) Tekrar Bulma
        (3) n. İndise veri ekleme
        (4) Temizleme
        (5) n. İndisten n. İndise Kadar Veri Silme
        (6) Ters Çevir
        (7) Listenin Uzunluğu
        (8) Aritmetik Değerli Verileri Toplama
        (9) Küçükten Büyüğe Aritmetik Sıralama
        (10) Büyükten Küçüğe Aritmetik Sıralama
        (11) Küçükten Büyüğe Karakter Sıralama
        (12) Küçükten Büyüğe Karakter Sıralama
        (13) Aritmetik Verilerde Minimum Bulma
        (14) Aritmetik Verilerde Maksimum Bulma
        (15) Karakter Verilerinde Minimum Bulma
        (16) Karakter Verilerinde Maksimum Bulma
        """)
        sor = input("İşleminiz nedir?: ")
        if sor == "0":
            çıkış()
            break
        elif sor == "1":
            toplam_veri()
        elif sor == "2":
            tekrar_bulma()
        elif sor == "3":
            n_indise_veri_ekleme()
        elif sor == "4":
            temizleme()
        elif sor == "5":
            n_indisten_n_indise_kadar_veri_silme()
        elif sor == "6":
            ters_çevir()
        elif sor == "7":
            liste_uzunluğu()
        elif sor == "8":
            aritmetik_değerli_veri_toplama()
        elif sor == "9":
            küçükten_büyüğe_aritmetik_sıralama()
        elif sor == "10":
            büyükten_küçüğe_aritmetik_sıralama()
        elif sor == "11":
            küçükten_büyüğe_karakter_sıralama()
        elif sor == "12":
            büyükten_küçüğe_karakter_sıralama()
        elif sor == "13":
            aritmetik_verilerde_min_bulma()
        elif sor == "14":
            aritmetik_verilerde_min_bulma()
        elif sor == "15":
            karakter_verilerinde_min_bulma()
        elif sor == "16":
            karakter_verilerinde_max_bulma()
        else:
            hata()


def toplam_veri():
    toplam = 0
    for i in y:
        toplam += 1
    print()
    print("Listede bulunan toplam veri: {}".format(toplam))
 

def tekrar_bulma():
    print()
    print("Mevcut Liste:")
    print("     {}".format(y))
    print()
    print("Hangi verinin tekrar sayısını bulmak istiyorsunuz?")
    sor0 = input("*Veriyi giriniz: ")
    a = y.count(sor0)
    print()
    print("Tekrar sayısı bulunan veri: {}".format(sor0))
    print("Tekrar sayısı: {}".format(a))


def n_indise_veri_ekleme():
    sor0 = int(input("Verinin ekleneceği indisi giriniz: "))
    sor1 = input("Veriyi giriniz: ")
    while True:
        print()
        print("{}. indise veri eklenecek.".format(sor0))
        print()
        print("Eklenecek veri: {}".format(sor1))
        print()
        sor = input("Devam edilsin mi?: evet(e) / hayır(h)")
        if sor == "e":
            y.insert(sor0, sor1)
            print()
            print("İşlem başarılı!")
            print()
            print("--Yeni Liste:")
            print("     {}".format(y))
            break
        elif sor == "h":
            break
        else:
            return hata()


def temizleme():
    print()
    print("Liste içindeki tüm veriler silinecektir. Silinen veriler geri alınamaz!")
    print()
    print("Liste temizlensin mi?:   evet(e) / hayır(h)")
    sor = input().lower()
    if sor == "e":
        print()
        print("Emin misiniz?:   evet(e) / hayır(h)")
        sor = input().lower()
        if sor == "e":
            temizleme = y.clear()
            print()
            print("Tüm veriler temizlendi.")
            print()
            print("--Liste:")
            print()
            print("     {}".format(y))
        else:
            hata()
            print()
            print("Veriler korunuyor...")
    else:
        print()
        print("Veriler korunuyor...")


def n_indisten_n_indise_kadar_veri_silme():
    print()
    print("Mevcut Liste:")
    print("     {}".format(y))
    print()
    sor1 = int(input("Kaçıncı indisten silinmeye başlansın?: "))
    başlangıç = sor1
    sor2 = int(input("Kaçıncı indise kadar silinsin?: "))
    varış = sor2
    a = y[başlangıç:varış]
    print("""
    Silinecek veriler:
    """.format(a))
    del y[başlangıç:varış]
    print(y)
    print()
    print("İşlem başarılı!")
    print()
    print("--Yeni Liste:")
    print("     {}".format(y))


def ters_çevir():
    print()
    print("Sondan başa mevcut liste:")
    a = y.reverse()
    print()
    print("     ",y)


def liste_uzunluğu():
    sonuç = len(y)
    print()
    print("     ",sonuç)


def aritmetik_değerli_veri_toplama():
    print()
    print("   --Mevcut Liste:")
    print()
    print("     {}".format(y))
    u = len(y)
    if u == 0:
        print()
        print("Listede veri bulunmamaktadır.")
        print("İşlem yapılamaz.")
    else:
        print()
        print("Lüften listenizi kontrol ediniz!")
        print("Listede *yalnızca* aritmetik veri mi var?")
        print()
        print("Bu özellik, listede *yalnızca* aritmetik veri varsa kullanılabilir.")
        print("Aksi halde program ÇÖKECEKTİR!")
        print()
        print("İşlem yapmak istiyor musunuz?:    evet(e) / hayır(h)")
        sor = input().lower()
        if sor == "e":
            sonuç = sum(y)
            print()
            print("--Sonuç:")
            print()
            print("     {}".format(sonuç))
        elif sor == "h":
            return diğer_işlem()
        else:
            return hata()


def küçükten_büyüğe_aritmetik_sıralama():
    print()
    print("   --Mevcut Liste:")
    print()
    print("     {}".format(y))
    u = len(y)
    if u == 0:
        print()
        print("Listede veri bulunmamaktadır.")
        print("İşlem yapılamaz.")
    else:
        print()
        print("Lüften listenizi kontrol ediniz!")
        print("Listede *yalnızca* aritmetik veri mi var?")
        print()
        print("Bu özellik, listede *yalnızca* aritmetik veri varsa kullanılabilir.")
        print("Aksi halde program ÇÖKECEKTİR!")
        print()
        print("İşlem yapmak istiyor musunuz?:    evet(e) / hayır(h)")
        sor = input().lower()
        if sor == "e":
            sonuç = y.sort()
            print()
            print("--Küçükten Büyüğe Sonuç:")
            print()
            print("     {}".format(sonuç))
        elif sor == "h":
            return diğer_işlem()
        else:
            return hata()


def büyükten_küçüğe_aritmetik_sıralama():
    print()
    print("   --Mevcut Liste:")
    print()
    print("     {}".format(y))
    u = len(y)
    if u == 0:
        print()
        print("Listede veri bulunmamaktadır.")
        print("İşlem yapılamaz.")
    else:
        print()
        print("Lüften listenizi kontrol ediniz!")
        print("Listede *yalnızca* aritmetik veri mi var?")
        print()
        print("Bu özellik, listede *yalnızca* aritmetik veri varsa kullanılabilir.")
        print("Aksi halde program ÇÖKECEKTİR!")
        print()
        print("İşlem yapmak istiyor musunuz?:    evet(e) / hayır(h)")
        sor = input().lower()
        if sor == "e":
            sonuç = y.sort(reverse=True)
            print()
            print("--Büyükten Küçüğe Sonuç:")
            print()
            print("     {}".format(sonuç))
        elif sor == "h":
            return diğer_işlem()
        else:
            return hata()


def küçükten_büyüğe_karakter_sıralama():
    print()
    print("   --Mevcut Liste:")
    print()
    print("     {}".format(y))
    u = len(y)
    if u == 0:
        print()
        print("Listede veri bulunmamaktadır.")
        print("İşlem yapılamaz.")
    else:
        print()
        print("Lüften listenizi kontrol ediniz!")
        print("Listede *yalnızca* karakter verisi mi var?")
        print()
        print("Bu özellik, listede *yalnızca* karakter verisi varsa kullanılabilir.")
        print("Aksi halde program ÇÖKECEKTİR!")
        print()
        print("İşlem yapmak istiyor musunuz?:    evet(e) / hayır(h)")
        sor = input().lower()
        if sor == "e":
            sonuç = y.sort()
            print()
            print("--Küçükten Büyüğe Sonuç:")
            print()
            print("     {}".format(sonuç))
        elif sor == "h":
            return diğer_işlem()
        else:
            return hata()


def büyükten_küçüğe_karakter_sıralama():
    print()
    print("   --Mevcut Liste:")
    print()
    print("     {}".format(y))
    u = len(y)
    if u == 0:
        print()
        print("Listede veri bulunmamaktadır.")
        print("İşlem yapılamaz.")
    else:
        print()
        print("Lüften listenizi kontrol ediniz!")
        print("Listede *yalnızca* karakter verisi mi var?")
        print()
        print("Bu özellik, listede *yalnızca* karakter verisi varsa kullanılabilir.")
        print("Aksi halde program ÇÖKECEKTİR!")
        print()
        print("İşlem yapmak istiyor musunuz?:    evet(e) / hayır(h)")
        sor = input().lower()
        if sor == "e":
            sonuç = y.sort(reverse=True)
            print()
            print("--Küçükten Büyüğe Sonuç:")
            print()
            print("     {}".format(sonuç))
        elif sor == "h":
            return diğer_işlem()
        else:
            return hata()


def aritmetik_verilerde_min_bulma():
    print()
    print("   --Mevcut Liste:")
    print()
    print("     {}".format(y))
    u = len(y)
    if u == 0:
        print()
        print("Listede veri bulunmamaktadır.")
        print("İşlem yapılamaz.")
    else:
        print()
        print("Lüften listenizi kontrol ediniz!")
        print("Listede *yalnızca* aritmetik veri mi var?")
        print()
        print("Bu özellik, listede *yalnızca* aritmetik veri varsa kullanılabilir.")
        print("Aksi halde program ÇÖKECEKTİR!")
        print()
        print("İşlem yapmak istiyor musunuz?:    evet(e) / hayır(h)")
        sor = input().lower()
        if sor == "e":
            sonuç = min(y)
            print()
            print("--Sonuç:")
            print()
            print("     {}".format(sonuç))
        elif sor == "h":
            return diğer_işlem()
        else:
            return hata()


def aritmetik_verilerde_max_bulma():
    print()
    print("   --Mevcut Liste:")
    print()
    print("     {}".format(y))
    u = len(y)
    if u == 0:
        print()
        print("Listede veri bulunmamaktadır.")
        print("İşlem yapılamaz.")
    else:
        print()
        print("Lüften listenizi kontrol ediniz!")
        print("Listede *yalnızca* aritmetik veri mi var?")
        print()
        print("Bu özellik, listede *yalnızca* aritmetik veri varsa kullanılabilir.")
        print("Aksi halde program ÇÖKECEKTİR!")
        print()
        print("İşlem yapmak istiyor musunuz?:    evet(e) / hayır(h)")
        sor = input().lower()
        if sor == "e":
            sonuç = max(y)
            print()
            print("--Sonuç:")
            print()
            print("     {}".format(sonuç))
        elif sor == "h":
            return diğer_işlem()
        else:
            return hata()


def karakter_verilerinde_min_bulma():
    print()
    print("   --Mevcut Liste:")
    print()
    print("     {}".format(y))
    u = len(y)
    if u == 0:
        print()
        print("Listede veri bulunmamaktadır.")
        print("İşlem yapılamaz.")
    else:
        print()
        print("Lüften listenizi kontrol ediniz!")
        print("Listede *yalnızca* karakter verisi mi var?")
        print()
        print("Bu özellik, listede *yalnızca* karakter verisi varsa kullanılabilir.")
        print("Aksi halde program ÇÖKECEKTİR!")
        print()
        print("İşlem yapmak istiyor musunuz?:    evet(e) / hayır(h)")
        sor = input().lower()
        if sor == "e":
            sonuç = min(y)
            print()
            print("--Sonuç:")
            print()
            print("     {}".format(sonuç))
        elif sor == "h":
            return diğer_işlem()
        else:
            return hata()


def karakter_verilerinde_max_bulma():
    print()
    print("   --Mevcut Liste:")
    print()
    print("     {}".format(y))
    u = len(y)
    if u == 0:
        print()
        print("Listede veri bulunmamaktadır.")
        print("İşlem yapılamaz.")
    else:
        print()
        print("Lüften listenizi kontrol ediniz!")
        print("Listede *yalnızca* karakter verisi mi var?")
        print()
        print("Bu özellik, listede *yalnızca* karakter verisi varsa kullanılabilir.")
        print("Aksi halde program ÇÖKECEKTİR!")
        print()
        print("İşlem yapmak istiyor musunuz?:    evet(e) / hayır(h)")
        sor = input().lower()
        if sor == "e":
            sonuç = max(y)
            print()
            print("--Sonuç:")
            print()
            print("     {}".format(sonuç))
        elif sor == "h":
            return diğer_işlem()
        else:
            return hata()


def program():
    while True:
        print("""
        (0) Programı Kapat
        (1) Programı Çalıştır
        """)
        sor = input()
        if sor == "0":
            print()
            print("Program kapatılıyor...")
            print()
            break
        elif sor == "1":
            print()
            print("Program çalıştırılıyor...")
            print()
            while True:
                print("""
                (0) Çıkış
                (1) Veri Okuma
                (2) Veri Ekleme
                (3) Veri Güncelleme
                (4) Veri Silme
                (5) Diğer İşlemler
                """)
                sor = input("İşleminiz nedir?: ")
                if sor == "0":
                    çıkış()
                    break
                elif sor == "1":
                    veri_okuma()
                elif sor == "2":
                    veri_ekleme()
                elif sor == "3":
                    veri_güncelleme()
                elif sor == "4":
                    veri_silme()
                elif sor == "5":
                    diğer_işlem()
                else:
                    hata()
        else:
            pass


program()