from libnum import *

class ChosenCipher(object):
    def __init__(self, n, e, c):
        self.n = n
        self.e = e
        self.c = c
        self.d = None
        self.p = None
        self.q = None

    def mulFactor(self, f):
        return (self.c * pow(f, self.e, self.n))%(self.n)

    def crack(self, f, plain):
        inv = invmod(f, self.n)
        self.plain = (plain * inv) % self.n
        return True

