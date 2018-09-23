import unittest
from rsatool.Factorization import *


class Test(unittest.TestCase):
	def test_crack(self):
		n = 783340156742833416191
		e = 653
		c = 309117097659990665453

		attack = Factorization(n, e)
		self.assertTrue(attack.crack())

		m = pow(c, attack.d, n)
		self.assertEquals(m, 6297558865603227502)


if __name__ == '__main__':
	unittest.main()