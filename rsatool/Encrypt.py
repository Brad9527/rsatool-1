from Crypto.PublicKey import RSA
import binascii

class Encrypt():
    def __init__(self, n, e, plaintext):
        key = RSA.construct((n, e))
        
        c = key.encrypt(plaintext, None)[0]
        c = '0x' + binascii.hexlify(c)
        c = long(c, 16)

        print('n = {}'.format(n))
        print('e = {}'.format(e))
        print('c = {}'.format(c))
