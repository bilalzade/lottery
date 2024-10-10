#Reqem texmini oyunu
#Tapsiriq beledir:
# Uduş məbləği 1 milyon manat
# Hər cəhdə görə 50 min manat azalsın
# Cəhd sayı 20 olacaq və hər cəhddən sonra say azalacaq
# Rastgələ rəqəmlər 1 ilə 1000 arasında olmalıdır
# İstifadəçidən giriş rəqəm istənilir. İstifadəçinin rəqəm əvəzinə səhvən simvol əlavə edilməsi də nəzərə alınır
# İstifadəçi doğru rəqəmdən aşağıdırsa rəqəmi yüksəldin əgər yuxarıdırsa rəqəmi azaldın istənilir
# Hər cəhdən sonra da qalanhaqq sayını çap edirsiniz.
# Sonda isə əgər istifadəçi 20 cəhddə doğru taparsa təbrik edirsiniz, təsadüfi doğru rəqəmləri tapana qədər təsadüfi verdiyi rəqəmləri ekrana çap edirsiniz
# Əgər doğru rəqəmi tapmayıbsa Üzgünəm cəhdləriniz bitdi mesajı verirsiniz və doğru rəqəm nə idisə onu çap edirsiniz



#Birinci növbədə təsadüfi rəqəmlər seçiləcəyi üçün random libraryni import edirik
import random

lottery = 0

number = random.randint(1, 1000)

cavablar = []

udus = 1000000

print("Oyunumuza xoş gəldiniz! 1 Milyon manat uduş üçün 1 ilə 1000 arasında təsadüfi seçilmiş rəqəmi tapın.") 
print("Diqqətli olun! 20 cəhdiniz mövcuddur və hər təxmində uduşunuz 50.000 AZN azalacaq!")

while lottery < 20:
    try:
        cavab = int(input("Şanslı olub olmadığınızı yoxlayın :) :"))
    except ValueError:
        print("Rəqəm daxil edin!")
        continue

    if number < cavab:
        print("Doğru rəqəm daha kiçikdir")
        cavablar.append(cavab)
        lottery += 1
        cehdsayisi = 20 - lottery
        udus -= 50000
        print("Qalan cəhdiniz:" , cehdsayisi)
        print("Qalan uduş fondu:", udus)

    elif number > cavab:
        print("Doğru rəqəm daha böyükdür")
        cavablar.append(cavab)
        lottery += 1
        cehdsayisi = 20 - lottery
        udus -= 50000
        print("Qalan cəhdiniz:", cehdsayisi)
        print("Qalan uduş məbləği:", udus)

    else:
        cavablar.append(cavab)
        print("Təbriklər! Qalib oldunuz!")
        print("Cəmi cəhdiniz:", len(cavablar))
        print("Təxminləriniz:", cavablar)
        print("Qazandığınız məbləğ:", udus)
        break

if lottery == 20:
    print("Cəhdləriniz bitdi. Doğru rəqəm: ", number)

