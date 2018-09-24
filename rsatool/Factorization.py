from libnum import *
import requests
from lxml.html import fromstring


class Factorization():
    def __init__(self, n, e):
        self.n = n
        self.e = e
        self.d = None
        self.p = None
        self.q = None

    def crack(self):
        try:
            response = requests.get('https://factordb.com/index.php?query={}'.format(self.n))
            html = fromstring(response.text)
            factors = html.findall('.//font')
            self.p = long(factors[1].text)
            self.q = long(factors[2].text)
        except:
            self.p, self.q = factorize(self.n).keys()

        phi = (self.p - 1) * (self.q - 1)
        if has_invmod(self.e, phi):
            self.d = invmod(self.e, phi)
            return True
        else:
            return False