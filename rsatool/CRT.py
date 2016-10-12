from libnum import *

def CRT(ds, rs):
    '''
    Chinese Remainder Theorem
    ds: array of dividers
    rs: array of remainders
    Return the number s such that s mod ds[i] = rs[i]
    '''
    length = len(ds)
    if not length == len(rs):
        print "The lengths of the two must be the same"
        return None

    p = i = prod = 1
    s = 0
    for i in range(length):
        prod *= ds[i]
    for i in range(length):
        p = prod // ds[i]
        s += rs[i] * invmod(p, ds[i]) * p
    return s % prod