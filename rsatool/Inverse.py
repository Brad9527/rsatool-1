import gmpy2

class Inverse():
    '''
    Multiplicative Inverse Attack
    d is the multiplicative inverse of e (modulo f(n)).
    '''
    def __init__(self, p, q, e):
        self.p = p
        self.q = q
        self.n = p * q # Modulo
        self.t = (p - 1) * (q - 1) # Carmichael's totient function
        self.e = e
        self.d = None
        

    def crack(self):
        try:
            self.d = int(gmpy2.invert(self.e, self.t))
            return True
        except:
            return False