from random import randint

n1 = randint(1,8)
n2 = randint(1,8)
n3 = randint(1,8)
n4 = randint(1,8)
n5 = randint(1,8)
tölur = list()
tölur.append(n1)
tölur.append(n2)
tölur.append(n3)
tölur.append(n4)
tölur.append(n5)
print(tölur)
teljari = 1
while True:
    print (n1,n2,n3,n4,n5)
    gisk1 = input("Giskaðu fyrstu töluna")
    gisk2 = input("Giskaðu aðra töluna")
    gisk3 = input("Giskaðu þriðju töluna")
    gisk4 = input("Giskaðu fjórðu töluna")
    gisk5 = input("Giskaðu fimmtu töluna")
    gisk1 = int(gisk1)
    gisk2 = int(gisk2)
    gisk3 = int(gisk3)
    gisk4 = int(gisk4)
    gisk5 = int(gisk5)
    vitlaust = 0
    rettar = 0

    if gisk1 != n1:
        vitlaust += 1
    if gisk2 != n2:
        vitlaust += 1
    if gisk3 != n3:
        vitlaust += 1
    if gisk5 != n5:
        vitlaust += 1
    for tala in tölur:
        if gisk1 == tala:
            rettar += 1
        if gisk2 == tala:
            rettar += 1
        if gisk3 == tala:
            rettar += 1
        if gisk4 == tala:
            rettar += 1
        if gisk5 == tala:
            rettar += 1



    if vitlaust == 0:
        print('Vel Gert')
        print('Það tók þig ' + str(teljari) + ' skipti að finna réttu töluna')
        break

    else:
        print(str(rettar)+ " tölur réttar. "+str(4-vitlaust)+ " tölur á réttum stað." )

    if teljari == 20:
        print('Þú ert búin að reyna 20 sinnum, þú tapaðir')
        break
    teljari += 1
