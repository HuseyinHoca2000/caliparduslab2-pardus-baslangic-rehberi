#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Pardus Başlangıç Rehberi
ÇalıPardusLab2 / Pardus Hata Yakalama ve Öneri Yarışması 2026
"""

def baslik_yaz():
    print("=" * 60)
    print("PARDUS BAŞLANGIÇ REHBERİ")
    print("=" * 60)
    print("Pardus'a yeni başlayan kullanıcılar için temel rehber\n")


def menu_goster():
    print("Lütfen bir konu seçin:")
    print("1 - Pardus nedir?")
    print("2 - Uygulamalar nasıl açılır?")
    print("3 - Yazılım Merkezi nedir?")
    print("4 - Ayarlar menüsü ne işe yarar?")
    print("5 - Dosyalarımı nerede bulurum?")
    print("6 - Güvenli kapatma")
    print("7 - Çıkış")
    print()


def konu_anlat(secim):
    if secim == "1":
        return (
            "Pardus, açık kaynak kodlu ve yerli bir Linux işletim sistemidir. "
            "Eğitim kurumları ve kamu kullanımı için uygun, güvenli ve geliştirilebilir bir yapıya sahiptir."
        )

    if secim == "2":
        return (
            "Uygulamaları açmak için ekranın alt veya üst kısmındaki uygulama menüsünü kullanabilirsiniz. "
            "Arama kutusuna uygulama adını yazarak hızlıca ulaşabilirsiniz."
        )

    if secim == "3":
        return (
            "Yazılım Merkezi, Pardus üzerinde uygulama bulma, yükleme ve kaldırma işlemleri için kullanılır. "
            "Yeni kullanıcılar için uygulama yönetimini kolaylaştırır."
        )

    if secim == "4":
        return (
            "Ayarlar menüsü; ekran, ses, ağ, kullanıcı hesabı ve benzeri sistem ayarlarını düzenlemek için kullanılır."
        )

    if secim == "5":
        return (
            "Kişisel dosyalarınızı Dosyalar uygulaması içinde Ev klasöründe bulabilirsiniz. "
            "Belgeler, İndirilenler ve Masaüstü klasörleri sık kullanılan alanlardır."
        )

    if secim == "6":
        return (
            "Bilgisayarı kapatmadan önce açık dosyalarınızı kaydedin. "
            "Ardından sistem menüsünden Kapat seçeneğini kullanarak güvenli şekilde çıkış yapabilirsiniz."
        )

    return "Geçersiz seçim."


def main():
    baslik_yaz()

    while True:
        menu_goster()
        secim = input("Seçiminiz: ").strip()

        if secim == "7":
            print("\nPardus Başlangıç Rehberi kapatıldı.")
            break

        print("\n[Rehber Bilgisi]")
        print(konu_anlat(secim))
        print()


if __name__ == "__main__":
    main()
