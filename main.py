# _*_ coding: utf-8 _*_

secret = 1345
guess = 0
i = 0

while guess != secret:
    guess = input ("Bitte eine Zahl ")
    if guess == 0:
        print "Das Spiel wird beendet"
        break
else:
    print"Sie haben es geschaft!"
