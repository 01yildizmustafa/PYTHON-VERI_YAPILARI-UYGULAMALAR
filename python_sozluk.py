a = {
    100: "MUSTAFA",
    "bilgisayar": True,
    False: 3.14,
    }


def çıkış():
    print()
    print("Çıkılıyor...")


def hata():
    print()
    print("Hatalı tuşlama!")


def geçersiz():
    print()
    print("Geçersiz giriş!")


def veri_oku():
    print()
    print("  -----MEVCUT SÖZLÜK-----")
    print()
    print(a)
    print()


def veri_ekle():
    print()
    anahtar = input("Eklenecek anahtar verisini giriniz: ")
    değer = input("Eklenecek değer verisini giriniz: ")
    print()
    print("Eklenecek anahtar verisi: {}".format(anahtar))
    print("Eklenecek değer verisi: {}".format(değer))
    print()
    sor = input("Veriler eklensin mi?:   evet(e) / hayır(h) ").lower()
    if sor == "e":
        s = {anahtar: değer}
        a.update(s)
        print()
        print("Eklenen anahtar verisi: {}".format(anahtar))
        print("Eklenen değer verisi : {}".format(değer))
        print()
        print("  -----YENİ SÖZLÜK-----")
        print()
        print(a)
        print()
    elif sor == "h":
        çıkış()
        return
    else:
        geçersiz()
    

def veri_güncelle():
    print()
    print("  -----MEVCUT SÖZLÜK-----")
    print()
    print(a)
    print()
    anahtar = input("Değeri değiştirilecek olan anahtar verisini giriniz: ")
    değer = input("Yeni değer verisini giriniz: ")
    print()
    print("Şu anahtarın değeri değiştirilecek: {}".format(anahtar))
    print("Yeni değer şu olacak: {}".format(değer))
    print()
    sor = input("Veriler değiştirilsin mi?:   evet(e) / hayır(h) ").lower()
    if sor == "e":
        sonuç = {anahtar: değer}
        a.update(sonuç)
        print()
        print("Veriler değiştirildi.")
        print()
        print("Değeri değiştirilen anahtar: {}".format(anahtar))
        print("Yeni değer: {}".format(değer))
        print()
        print("  -----YENİ SÖZLÜK-----")
        print()
        print(a)
        print()
    elif sor == "h":
        return
    else:
        geçersiz()


def veri_sil():
    print()
    print("  -----MEVCUT SÖZLÜK-----")
    print()
    print(a)
    print()
    print("'anahtar: değer' çifti silinecek.")
    anahtar = input("Anahtar giriniz: ")
    if anahtar in a:
        print()
        print("Silinecek anahtar değer çifti: '{}: {}'".format(anahtar, a.get(anahtar)))
        sor = input("Veriler silinin mi?:   evet(e) / hayır(h) ").lower()
        if sor == "e":
            print()
            n = a.pop(anahtar)
            print("İşlem başarılı!")
        elif sor == "h":
            print()
            print("Veriler korunuyor...")
            return
        else:
            geçersiz()
            print()
            print("Veriler korunuyor...")
    else:
        geçersiz()


def tüm_anahtar():
    print()
    print("  -----TÜM ANAHTARLAR----- ")
    print()
    print(list(a.keys()))


def tüm_değer():
    print()
    print("  -----TÜM DEĞERLER-----")
    print()
    print(list(a.keys()))


def anahtar_değerini_bulma():
    print()
    sor = input("Değerini bulmak istediğiniz anahtarı giriniz: ")
    print()
    b = a.get(sor, "Geçersiz giriş!")
    print(b)


def kopyalama():
    print()
    print("Yeni bir kopya sözlük oluşacak.")
    sor = input("Kopya sözlüğün adını giriniz: ")
    kopya_isim = sor
    kopya_isim = a.copy()
    print()
    print("Sözlük kopyalandı.")
    print()
    print("  -----KOPYA SÖZLÜK-----")
    print()
    print(kopya_isim)
    print()
    print("Hafızada ikinci bir bağımsız sözlük oluşturuldu.")
    print("Oluşturulan bu sözlüğün verileri orijinal sözlüğün verileri ile aynı.")
    print("Orijinal sözlükte yapılan herhangi bir değişim, kopya sözlüğü etkilemez.")
    print("Bunun tersi de doğrudur.")


def temizleme():
    print()
    print("Sözlüğün içindeki bütün anahtarlar ve değerler silinecek!")
    print("Bu veriler geri alınamaz!")
    print()
    sor = input("Sözlük verileri silinsin mi?:   evet(e) / hayır(h) ").lower()
    if sor == "e":
        a.clear()
        print()
        print("Tüm veriler silindi.")
        print()
        print("  -----YENİ SÖZLÜK-----")
        print()
        print("     ",a)
        print()
    elif sor == "h":
        print()
        print("Veriler korunuyor...")
        return
    else:
        geçersiz()
        print()
        print("Veriler korunuyor...")


def varsayılan_ekle():
    print()
    print("Anahtar aranacak.")
    print("Eğer belirtilen anahtar sözlükte var ise değişiklik yapılmayacak.")
    print("Yok eğer belirtilen anahtar sözlükte yok ise sözlüğe eklenecek.")
    print()
    anahtar = input("Aramak istediğiniz anahtarı giriniz: ")
    değer = input("Değer verisi giriniz: ")
    a.setdefault(anahtar, değer)
    print()
    print("İşlem başarılı!")


def aritmetik_anahtar_ekle():
    print()
    try:
        anahtar = float(input("Veri giriniz: "))
        if anahtar == float(anahtar):
            print()
            print("Eklenecek anahtar verisi: {}".format(anahtar))
            print("""
            (1) Aritmetik Cebir
            (2) Mantık Cebri
            (3) Metin
            """)
            sor = input("Eklemek istediğiniz değer türünü giriniz: ")
            if sor == "1":
                print()
                try:
                    değer = float(input("Veri giriniz: "))
                    if değer == float(değer):
                        print()
                        print("Eklenecek anahtar verisi: {}".format(anahtar))
                        print("Eklenecek değer verisi: {}".format(değer))
                        print()
                        sor = input("Veriler eklensin mi?:   evet(e) / hayır(h) ")
                        if sor == "e":
                            print()
                            işlem = {anahtar: değer}
                            a.update(işlem)
                            print("İşlem başarılı!")
                        elif sor == "h":
                            çıkış()
                            return
                        else:
                            geçersiz()
                except:
                    geçersiz()
            elif sor == "2":
                print()
                sor = input("Eklenecek değer True mu, False mu?:   True(t) / False(f) ").lower()
                değer = sor
                if sor == "t":
                    print()
                    print("Eklenecek anahtar verisi: {}".format(anahtar))
                    print("Eklenecek değer verisi: {}".format(True))
                    print()
                    sor = input("Veriler eklensin mi?:   evet(e) / hayır(h) ")
                    if sor == "e":
                        print()
                        işlem = {anahtar: True}
                        a.update(işlem)
                        print("İşlem başarılı!")
                    elif sor == "h":
                        çıkış()
                        return
                elif sor == "f":
                    print()
                    print("Eklenecek anahtar verisi: {}".format(anahtar))
                    print("Eklenecek değer verisi: {}".format(False))
                    print()
                    sor = input("Veriler eklensin mi?:   evet(e) / hayır(h) ")
                    if sor == "e":
                        print()
                        işlem = {anahtar: False}
                        print("İşlem başarılı!")
                    elif sor == "h":
                        çıkış()
                        return
                else:
                    geçersiz()
            elif sor == "3":
                print()
                değer = input("Veriyi giriniz: ")
                print()
                print("Eklenecek anahtar verisi: {}".format(anahtar))
                print("Eklenecek değer verisi: {}".format(değer))
                print()
                sor = input("Veriler eklensin mi?:   evet(e) / hayır(h) ")
                if sor == "e":
                    print()
                    işlem = {anahtar: değer}
                    a.update(işlem)
                    print("İşlem başarılı!")
                elif sor == "h":
                    çıkış()
                    return
            else:
                hata()
    except:
        geçersiz()


def mantık_anahtar_ekle():
    while True:
        print()
        anahtar = input("Eklenecek anahtar verisi True mu, False mu?:   True(t) / False(f) ")
        if anahtar == "t":
            print("""
            (1) Aritmetik Cebir
            (2) Mantık Cebri
            (3) Metin
            """)
            sor = input("Eklemek istediğiniz değer türünü giriniz: ")
            if sor == "1":
                print()
                try:
                    değer = float(input("Veri giriniz: "))
                    if değer == float(değer):
                        print()
                        print("Eklenecek anahtar verisi: {}".format(True))
                        print("Eklenecek değer verisi: {}".format(değer))
                        print()
                        sor = input("Veriler eklensin mi?:   evet(e) / hayır(h) ")
                        if sor == "e":
                            print()
                            işlem = {True: değer}
                            a.update(işlem)
                            print("İşlem başarılı!")
                            break
                        elif sor == "h":
                            çıkış()
                            return
                        else:
                            geçersiz()
                except:
                    geçersiz()
            elif sor == "2":
                sor = input("Eklenecek değer verisi True mu, False mu?:   True(t) / False(f) ")
                if sor == "t":
                    print()
                    print("Eklenecek anahtar verisi: {}".format(True))
                    print("Eklenecek değer verisi: {}".format(True))
                    print()
                    sor = input("Veriler eklensin mi?:   evet(e) / hayır(h) ")
                    if sor == "e":
                        print()
                        işlem = {True: True}
                        a.update(işlem)
                        print("İşlem başarılı!")
                        break
                    elif sor == "h":
                        çıkış()
                        return
                    else:
                        geçersiz()
                elif sor == "f":
                    print()
                    print("Eklenecek anahtar verisi: {}".format(True))
                    print("Eklenecek değer verisi: {}".format(False))
                    print()
                    sor = input("Veriler eklensin mi?:   evet(e) / hayır(h) ")
                    if sor == "e":
                        print()
                        işlem = {True: False}
                        a.update(işlem)
                        print("İşlem başarılı!")
                        break
                    elif sor == "h":
                        çıkış()
                        return
                    else:
                        geçersiz()
                else:
                    geçersiz()
            elif sor == "3":
                print()
                değer = input("Veriyi giriniz: ")
                print()
                print("Eklenecek anahtar verisi: {}".format(True))
                print("Eklenecek değer verisi: {}".format(değer))
                print()
                sor = input("Veriler eklensin mi?:   evet(e) / hayır(h) ")
                if sor == "e":
                    print()
                    işlem = {True: değer}
                    a.update(işlem)
                    a.update(işlem)
                    print("İşlem başarılı!")
                    break
                elif sor == "h":
                    çıkış()
                    return
                else:
                    geçersiz()
            else:
                hata()
        elif anahtar == "f":
            print("""
            (1) Aritmetik Cebir
            (2) Mantık Cebri
            (3) Metin
            """)
            sor = input("Eklemek istediğiniz değer türünü giriniz: ")
            if sor == "1":
                print()
                try:
                    değer = float(input("Veri giriniz: "))
                    if değer == float(değer):
                        print()
                        print("Eklenecek anahtar verisi: {}".format(False))
                        print("Eklenecek değer verisi: {}".format(değer))
                        print()
                        sor = input("Veriler eklensin mi?:   evet(e) / hayır(h) ")
                        if sor == "e":
                            print()
                            işlem = {False: değer}
                            a.update(işlem)
                            print("İşlem başarılı!")
                            break
                        elif sor == "h":
                            çıkış()
                            return
                        else:
                            geçersiz()
                except:
                    geçersiz()
            elif sor == "2":
                sor = input("Eklenecek değer verisi True mu, False mu?:   True(t) / False(f) ")
                if sor == "t":
                    print()
                    print("Eklenecek anahtar verisi: {}".format(False))
                    print("Eklenecek değer verisi: {}".format(True))
                    print()
                    sor = input("Veriler eklensin mi?:   evet(e) / hayır(h) ")
                    if sor == "e":
                        print()
                        işlem = {False: True}
                        a.update(işlem)
                        print("İşlem başarılı!")
                        break
                    elif sor == "h":
                        çıkış()
                        return
                    else:
                        geçersiz()
                elif sor == "f":
                    print()
                    print("Eklenecek anahtar verisi: {}".format(False))
                    print("Eklenecek değer verisi: {}".format(False))
                    print()
                    sor = input("Veriler eklensin mi?:   evet(e) / hayır(h) ")
                    if sor == "e":
                        print()
                        işlem = {False: False}
                        a.update(işlem)
                        print("İşlem başarılı!")
                        break
                    elif sor == "h":
                        çıkış()
                        return
                    else:
                        geçersiz()
            elif sor == "3":
                print()
                değer = input("Veriyi giriniz: ")
                print()
                print("Eklenecek anahtar verisi: {}".format(False))
                print("Eklenecek değer verisi: {}".format(değer))
                print()
                sor = input("Veriler eklensin mi?:   evet(e) / hayır(h) ")
                if sor == "e":
                    print()
                    işlem = {False: değer}
                    a.update(işlem)
                    print("İşlem başarılı!")
                    break
                elif sor == "h":
                    çıkış()
                    return
                else:
                    geçersiz()
            else:
                hata()
        else:
            geçersiz()
            return
    

def diğer_işlem():
    while True:
        print("""
        (0) Çıkış
        (1) Tüm Anahtarlar
        (2) Tüm Değerler
        (3) Anahtar Değerini Bulma
        (4) Kopyalama
        (5) Temizleme
        (6) Varsayılan Ekle
        (7) Aritmetik Anahtar Ekleme
        (8) Mantık Anahtar Ekleme
        """)
        sor = input("İşleminiz nedir?: ")
        if sor == "0":
            çıkış()
            break
        elif sor == "1":
            tüm_anahtar()
        elif sor == "2":
            tüm_değer()
        elif sor == "3":
            anahtar_değerini_bulma()
        elif sor == "4":
            kopyalama()
        elif sor == "5":
            temizleme()
        elif sor == "6":
            varsayılan_ekle()
        elif sor == "7":
            aritmetik_anahtar_ekle()
        elif sor == "8":
            mantık_anahtar_ekle()
        else:
            hata()


def program():
    while True:
        print("""
        (0) Programı Kapat
        (1) Programı Çalıştır
        """)
        sor = input()
        if sor == "0":
            çıkış()
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
                    veri_oku()
                elif sor == "2":
                    veri_ekle()
                elif sor == "3":
                    veri_güncelle()
                elif sor == "4":
                    veri_sil()
                elif sor == "5":
                    diğer_işlem()
                else:
                    hata()
        else:
            pass


program()