import math
from colorama import Back,Fore
def topla(sayi1,sayi2):
    global sonuc
    sonuc = sayi1+sayi2
    return sonuc
def cıkar(sayi1,sayi2):
    global sonuc
    sonuc = sayi1-sayi2
    return sonuc
def carp(sayi1,sayi2):
    global sonuc
    sonuc = sayi1*sayi2
    return sonuc
def bol(sayi1,sayi2):
    global sonuc
    sonuc = sayi1/sayi2
    return sonuc
def usal(sayi1,sayi2):
    global sonuc
    sonuc = sayi1**sayi2
    return sonuc
def karekok(sayi1):
    global sonuc
    sonuc = math.sqrt(sayi1)
    return sonuc
while True:
    print(Back.BLACK,Fore.RED)
    nmb1 = int(input("Birinci sayıyı giriniz: "))
    nmb2 = int(input("İkinci sayıyı giriniz: "))
    answer = input("""Hangi işlemi yapacaksınız?
    ======================================
    1-Toplama
    2-Çıkarma
    3-Çarpma
    4-Bölme
    5-Üs al (İlk Girdiğiniz Sayı Taban, İkincisi Üs Olacaktır)
    6-Karekök (İlk Girdiğiniz Sayı Üstte, İkinci Girdiğiniz Sayı Altta Olacaktır)
    ======================================
    """)
    print(Fore.BLUE)
    if answer == "1":
        topla(nmb1, nmb2)
        print(sonuc)
    elif answer == "2":
        cıkar(nmb1, nmb2)
        print(sonuc)
    elif answer == "3":
        carp(nmb1, nmb2)
        print(sonuc)
    elif answer == "4":
        bol(nmb1, nmb2)
        print(sonuc)
    elif answer == "5":
        usal(nmb1, nmb2)
        print(sonuc)
    elif answer == "6":
        karekok(nmb1)
        print(sonuc)
        karekok(nmb2)
        print(sonuc)
    else:
        print("Yanlış sayı girdiniz")