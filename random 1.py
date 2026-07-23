import random
import time


def blackjack(penize):

    def hodnota(karta):
        if karta == "A":
            return 11
        elif karta in ["J", "Q", "K"]:
            return 10
        else:
            return karta

    while True:
        dohromady = 0
        dohromadyd = 0
        karty = ["A","A","A","A",2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,"J","J","J","J","Q","Q","Q","Q","K","K","K","K"]

        print(penize)
        print("VITEJ V BLACKJACKU\n")
        time.sleep(0.5)
        sazka = float(input("Kolik chces vsadit?\n"))
        time.sleep(0.5)
        karta1 = random.choice(karty)
        karty.remove(karta1)
        dohromady += hodnota(karta1)
        karta2 = random.choice(karty)
        karty.remove(karta2)
        dohromady += hodnota(karta2)
        print("Padlo ti:",karta1,karta2,"\t dohromady mas:",dohromady)
        while True:
            if dohromady > 21 or dohromadyd > 16:
                break
            hrat = input("STAND | HIT")
            time.sleep(0.5)
            match hrat:
                case "HIT":
                    karta = random.choice(karty)
                    karty.remove(karta)
                    dohromady += hodnota(karta)
                    print("Padlo ti:", karta, "\tDohromady mas:", dohromady, "\n")
                    time.sleep(0.5)

                case "STAND":
                    karta1 = random.choice(karty)
                    karty.remove(karta1)
                    dohromadyd += hodnota(karta1)
                    karta2 = random.choice(karty)
                    karty.remove(karta2)
                    dohromadyd += hodnota(karta2)
                    print("Dealerovi padlo:",karta1,karta2, "\tDohromady ma:", dohromadyd, "\n")
                    time.sleep(0.5)
                    if dohromadyd > 16:
                        break
                    while True:
                        karta = random.choice(karty)
                        karty.remove(karta)
                        dohromadyd += hodnota(karta)
                        print("Dealerovi padlo:", karta, "\tDohromady ma:", dohromadyd, "\n")
                        time.sleep(0.5)
                        if dohromadyd > 16:
                            break

        if dohromady > 21:
            print("mas moc, PROHRAL SI\n")
            penize-=sazka
            print(penize)
        elif dohromadyd < 22 and dohromadyd < dohromady or dohromadyd > 21:
            print("VYHRAL SI\n")
            penize += sazka
            print(penize)
        elif dohromadyd == dohromady:
            print("REMIZA\n")
            print(penize)
        else:
            print("PROHRAL SI\n")
            penize -= sazka
            print(penize)
        znova = input("1 pro znovu | 0 pro  exit")
        if znova == "0":
            break
    return penize


penize = 1000
while True:
    print(penize)
    print("VÍTEJ V CASINOPY")
    hra = input("Co si chces zahrat?\t1 - Blackjack\n\t\t\t\t\t9 - KONEC\n")
    match hra:
        case "1": penize = blackjack(penize)
        case "9": break
        case _:
            print("ahoj")


