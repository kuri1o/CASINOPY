import random
import time


def blackjack(penize):
    while True:
        dohromady = 0
        dohromadyd = 0
        print(penize)
        print("VITEJ V LACKJACKU\n")
        sazka = float(input("Kolik chces vsadit?\n"))
        while True:
            karta = random.randint(1, 10)
            dohromady += karta
            print("Padlo ti:", karta, "\tDohromady mas:", dohromady, "\n")
            if dohromady > 21:
                break
            else:
                dalsi = input("1 pro kartu | 0 pro konec\n")
                if dalsi == "0":
                    break
        if dohromady < 22:
            while True:
                kartad = random.randint(1, 10)
                dohromadyd += kartad
                print("Dealerovi padlo:", kartad, "\tDohromady ma:", dohromadyd, "\n")
                time.sleep(1)
                if dohromadyd > 18:
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
        znova = input("1 pro znovu | 0 pro exit")
        if znova == "0":
            break
    return penize


penize = 1000
konecm = 66
while True:
    print(penize)
    print("VÍTEJ V CASINOPY")
    hra = input("Co si chces zahrat?\t1 - Blackjack\n\t\t\t\t\t2 - KONEC\n")
    match hra:
        case "1": penize = blackjack(penize)
        case "2": break
        case _:
            print("ahoj")


