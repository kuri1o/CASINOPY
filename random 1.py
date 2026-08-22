import random
import time
import os


def blackjack(penize):

    def tahni_kartu(karty):
        karta = random.choice(karty)
        karty.remove(karta)
        return karta

    def hrac(ruka,karty):
        karta = tahni_kartu(karty)
        ruka.append(karta)
        dohromady = hodnota_ruky(ruka)
        os.system("cls")
        print("Padlo ti:", karta, "\tDohromady mas:", dohromady, "\n")
        time.sleep(1)
        return dohromady

    def hodnota_ruky(ruka):
        soucet = 0
        esa = 0
        for karta in ruka:
            if karta == "A":
                esa += 1
                soucet += 11
            elif karta in ["J", "Q", "K"]:
                soucet += 10
            else:
                soucet += karta
        while soucet > 21 and esa > 0:
            soucet -= 10  # změň eso z 11 na 1
            esa -= 1
        return soucet

    def dealer(rukad,karty):
        soucet = hodnota_ruky(rukad)
        print("Dealerovi padlo:",*rukad, "\tDohromady ma:", soucet, "\n")
        time.sleep(2)
        while True:
            soucet = hodnota_ruky(rukad)

            if soucet >= 17:
                return soucet

            karta = tahni_kartu(karty)
            rukad.append(karta)
            soucet = hodnota_ruky(rukad)

            os.system("cls")
            print("Dealerovi padlo:", karta,"\tDohromady ma:", soucet, "\n")
            time.sleep(2)


    while True:
        os.system("cls")
        dohromady = 0
        dohromadyd = 0
        kolo = 0
        koloznova = 0
        karty = ["A","A","A","A",2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,"J","J","J","J","Q","Q","Q","Q","K","K","K","K"]
        if penize<1:
            print("jsi broke")
            time.sleep(0.8)
            break
        print(penize)
        print("VITEJ V BLACKJACKU\n")
        time.sleep(0.5)
        sazka = float(input("Kolik chces vsadit?\n"))
        if sazka > penize:
            os.system("cls")
            print("Nedostatek penez")
            time.sleep(1)
            continue

        time.sleep(0.5)
        ruka = []
        karta = tahni_kartu(karty)
        ruka.append(karta)
        karta = tahni_kartu(karty)
        ruka.append(karta)
        dohromady = hodnota_ruky(ruka)

        rukad = []
        karta1 = tahni_kartu(karty)
        rukad.append(karta1)
        karta = tahni_kartu(karty)
        rukad.append(karta)


        os.system("cls")
        print("Padlo ti:",*ruka,"\t dohromady mas:",dohromady," | Dealerovi padlo:",karta1," ???")
        time.sleep(1)
        while True:
            if dohromady > 21:
                break
            if kolo == 0:
                hrat = input("STAND | HIT | DOUBLE").upper()
            else:
                hrat = input("STAND | HIT").upper()
            time.sleep(0.5)
            kolo += 1
            match hrat:

                case "HIT":
                    dohromady = hrac(ruka,karty)

                case "STAND":
                    os.system("cls")
                    dohromadyd = dealer(rukad, karty)
                    break

                case "DOUBLE":
                    if penize >= 2 * sazka:
                        sazka *= 2
                        os.system("cls")
                        dohromady = hrac(ruka, karty)

                        if dohromady <= 21:
                            dohromadyd = dealer(rukad, karty)
                        break
                    else:
                        print("NEMAS DOSTATEK PENEZ NA DOUBLE")

                case _:
                    kolo -= 1

        os.system("cls")
        if dohromady > 21:
            print("mas moc, PROHRAL SI\n")
            penize -= sazka
            print(penize)
        elif dohromadyd > 21:
            print("VYHRAL SI - dealer bust\n")
            penize += sazka
            print(penize)
        elif dohromady > dohromadyd:
            print("VYHRAL SI\n")
            penize += sazka
            print(penize)
        elif dohromady == dohromadyd:
            print("REMIZA\n")
            print(penize)
        else:
            print("PROHRAL SI\n")
            penize -= sazka
            print(penize)
        while koloznova == 0:
            znova = input("1 pro znovu | 0 pro  exit")
            match znova:
                case "0":
                    koloznova += 2
                case "1":
                    koloznova += 1
                case _:
                    koloznova = 0
        os.system("cls")
        if koloznova == 2:
            break
    return penize


penize = 1000
os.system("cls")
while True:
    print(penize)
    print("VÍTEJ V CASINOPY")
    hra = input("Co si chces zahrat?\t1 - Blackjack\n\t\t\t9 - KONEC\n")
    match hra:
        case "1": penize = blackjack(penize)
        case "9": break
        case _:
            print("ahoj")


