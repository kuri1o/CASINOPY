
import random
import time

penize = 1000
dohromady = 0
dohromadyd = 0
print("VITEJ B LACKJACKU\n")
sazka = input("Kolik chces vsadit?\n")
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
    print("mas moc, PROHRAL SI")
elif dohromadyd < 22 and dohromadyd < dohromady or dohromadyd > 21:
    print("VYHRAL SI")
else:
    print("PROHRAL SI")
