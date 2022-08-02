#!/usr/bin/env python3

import math


class Trager:

    """ festigkeitsKennwerte = {
        "C12/15": { "fck": 12, "fctm": 1.6 },
        "C16/20": { "fck": 16, "fctm": 1.9 },
        "C20/25": { "fck": 20, "fctm": 2.2 },
        "C25/30": { "fck": 25, "fctm": 2.6 },
        "C30/37": { "fck": 30, "fctm": 2.9 },
        "C35/45": { "fck": 35, "fctm": 3.2 },
        "C40/50": { "fck": 40, "fctm": 3.5 },
        "C45/55": { "fck": 45, "fctm": 3.8 },
        "C50/60": { "fck": 50, "fctm": 4.1 },
        "C55/67": { "fck": 55, "fctm": 4.2 },
        "C60/75": { "fck": 60, "fctm": 4.4 },
        "C70/85": { "fck": 70, "fctm": 4.6 },
        "C80/95": { "fck": 80, "fctm": 4.8 },
        "C90/105": { "fck": 90, "fctm": 5.0 }
    } """

    def __init__(self, id, breite, hohe, lange, betongute, fyk) -> None:
        self.festigkeitsKennwerte = {
            "C12/15": { "fck": 12, "fctm": 1.6 },
            "C16/20": { "fck": 16, "fctm": 1.9 },
            "C20/25": { "fck": 20, "fctm": 2.2 },
            "C25/30": { "fck": 25, "fctm": 2.6 },
            "C30/37": { "fck": 30, "fctm": 2.9 },
            "C35/45": { "fck": 35, "fctm": 3.2 },
            "C40/50": { "fck": 40, "fctm": 3.5 },
            "C45/55": { "fck": 45, "fctm": 3.8 },
            "C50/60": { "fck": 50, "fctm": 4.1 },
            "C55/67": { "fck": 55, "fctm": 4.2 },
            "C60/75": { "fck": 60, "fctm": 4.4 },
            "C70/85": { "fck": 70, "fctm": 4.6 },
            "C80/95": { "fck": 80, "fctm": 4.8 },
            "C90/105": { "fck": 90, "fctm": 5.0 }
        }
        self.id = id
        self.breite = breite
        self.hohe = hohe
        self.lange = lange
        self.betongute = betongute
        self.fck = self.festigkeitsKennwerte[self.betongute]["fck"]
        self.fctm = self.festigkeitsKennwerte[self.betongute]["fctm"]
        self.fyk = fyk


    def querschnittsEigenschaften(self):
        querschnittsFlache = self.breite * self.hohe
        volumen = self.breite * self.hohe * self.lange
        tragheitsmoment = self.breite * math.pow(self.hohe, 3) / 12
        widerstandsmoment = self.breite * math.pow(self.hohe, 2) / 6
        return querschnittsFlache, volumen, tragheitsmoment, widerstandsmoment


class Balken(Trager):

    def __init__(self, id, breite, hohe, lange, betongute, fyk) -> None:
        super().__init__(id, breite, hohe, lange, betongute, fyk)



class Platten(Balken):
    pass

class Stutzen(Trager):
    pass

class Wande(Trager):
    pass


if __name__ == "__main__":
    # Beispielbalken mit 1
    X1 = Balken(1, 1, 1, 1, "C40/50", 550)
    print(type(X1.betongute))
    print(X1.fctm)
    pass
    