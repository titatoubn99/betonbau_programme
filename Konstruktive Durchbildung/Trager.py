#!/usr/bin/env python3

import math

class Trager:

    def __init__(self, id, breite, hohe, lange, fck, fyk) -> None:
        self.id = id
        self.breite = breite
        self.hohe = hohe
        self.lange = lange
        self.fck = fck
        self.fyk = fyk


    def querschnittsEigenschaften(self):
        querschnittsFlache = self.breite * self.hohe
        volumen = self.breite * self.hohe * self.lange
        tragheitsmoment = self.breite * math.pow(self.hohe, 3) / 12
        widerstandsmoment = self.breite * math.pow(self.hohe, 2) / 6
        return querschnittsFlache, volumen, tragheitsmoment, widerstandsmoment


class Balken(Trager):

    def __init__(self, id, breite, hohe, lange, fck, fyk) -> None:
        super().__init__(id, breite, hohe, lange, fck, fyk)



class Platten(Balken):
    pass

class Stutzen(Trager):
    pass

class Wande(Trager):
    pass


if __name__ == "__main__":
    # X1 = Balken()
    pass
    