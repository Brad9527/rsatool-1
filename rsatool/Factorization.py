from libnum import *

class Factorization():
    def __init__(self, n, e):
        self.n = n
        self.e = e
        self.d = None
        self.p = None
        self.q = None

    def crack(self):
        p, q = factorize(self.n).keys()
        phi = (p - 1) * (q - 1)
        if has_invmod(self.e, phi):
            self.d = invmod(self.e, phi)
            self.p = p
            self.q = q
            return True
        else:
            return False