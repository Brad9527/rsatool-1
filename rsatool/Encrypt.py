from Crypto.PublicKey import RSA

class Encrypt():
    def __init__(self, e, plaintext, keylength=1024):
        # Generate a public/private key pair 
        #   1024 bits key length (128 bytes)
        #   2048 bits key length (256 bytes)
        #   4096 bits key length (512 bytes)
        keypair = RSA.generate(keylength, e=e)
        c = int(keypair.encrypt(plaintext, keypair.publickey)[0].encode('hex'), 16)

        print('p = {}'.format(keypair.p))
        print('q = {}'.format(keypair.q))
        print('n = {}'.format(keypair.n))
        print('e = {}'.format(keypair.e))
        print('d = {}'.format(keypair.d))
        print('c = {}'.format(c))
