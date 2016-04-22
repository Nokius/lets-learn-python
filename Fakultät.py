while True:
    zahl = input("Geben Sie ein Zahl ein: ")
    if zahl < 0:
        print "Negative Zahl sind nicht erlaubt"
        continue
    ergebnis = 1
    for i in range(2, zahl+1):
        ergebnis = ergebnis * i
    print "Ergebnis: ", ergebnis
