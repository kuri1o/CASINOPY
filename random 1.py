import random
import time
import os


def blackjack(penize):

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


    while True:
        print("\n" * 50)
        dohromady = 0
        dohromadyd = 0
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
            print("\n" * 50)
            print("Nedostatek penez")
            time.sleep(1)
            continue
        time.sleep(0.5)
        karta1 = random.choice(karty)
        karty.remove(karta1)
        karta2 = random.choice(karty)
        karty.remove(karta2)
        ruka = []
        ruka.append(karta1)
        ruka.append(karta2)
        dohromady = hodnota_ruky(ruka)
        print("\n" * 50)
        print("Padlo ti:",karta1,karta2,"\t dohromady mas:",dohromady)
        while True:
            if dohromady > 21 or dohromadyd > 16:
                break
            hrat = input("STAND | HIT").upper()
            time.sleep(0.5)
            match hrat:

                case "HIT":
                    karta = random.choice(karty)
                    karty.remove(karta)
                    ruka.append(karta)
                    dohromady = hodnota_ruky(ruka)
                    print("\n" * 50)
                    print("Padlo ti:", karta, "\tDohromady mas:", dohromady, "\n")
                    time.sleep(1)

                case "STAND":
                    rukad = []
                    karta1 = random.choice(karty)
                    karty.remove(karta1)
                    karta2 = random.choice(karty)
                    karty.remove(karta2)
                    rukad.append(karta1)
                    rukad.append(karta2)
                    dohromadyd = hodnota_ruky(rukad)
                    print("\n" * 50)
                    print("Dealerovi padlo:",karta1,karta2, "\tDohromady ma:", dohromadyd, "\n")
                    time.sleep(2)
                    if dohromadyd > 16:
                        break
                    while True:
                        karta = random.choice(karty)
                        karty.remove(karta)
                        rukad.append(karta)
                        dohromadyd = hodnota_ruky(rukad)
                        print("Dealerovi padlo:", karta, "\tDohromady ma:", dohromadyd, "\n")
                        time.sleep(2)
                        if dohromadyd > 16:
                            break

        print("\n" * 50)
        if dohromady > 21:
            print("mas moc, PROHRAL SI\n")
            penize -= sazka
        elif dohromadyd > 21:
            print("VYHRAL SI - dealer bust\n")
            penize += sazka
        elif dohromady > dohromadyd:
            print("VYHRAL SI\n")
            penize += sazka
        elif dohromady == dohromadyd:
            print("REMIZA\n")
        else:
            print("PROHRAL SI\n")
            penize -= sazka
        znova = input("1 pro znovu | 0 pro  exit")
        if znova == "0":
            break
    return penize


penize = 1000
print("\n" * 50)
while True:
    print(penize)
    print("VÍTEJ V CASINOPY")
    hra = input("Co si chces zahrat?\t1 - Blackjack\n\t\t\t\t\t9 - KONEC\n")
    match hra:
        case "1": penize = blackjack(penize)
        case "9": break
        case _:
            print("ahoj")


