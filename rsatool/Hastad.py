import gmpy
from CRT import CRT

class Hastad(object):
    '''
    Hastad Broadcast Attack
    '''
    def __init__(self, ns, e, cs):
        '''
        ns: array of n
        e: public exponent
        cs: array of cipher text
        '''
        self.ns = ns
        self.n = None
        self.e = e
        self.d = None
        self.p = None
        self.q = None
        self.cs = cs

    def crack(self):
        s = CRT(self.ns, self.cs)
        plain, perfect = gmpy.root(s, self.e)
        if perfect:
            self.plain = ('%x' % plain).decode('hex')
            return True
        else:
            return False
