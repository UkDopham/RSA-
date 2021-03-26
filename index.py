class RSA:
	def generateKey(self, p, q):
		phi = self.getPhi(p,q)
		print("phi : " + str(phi))
		e = self.getE(phi)
		print("e : " + str(e))
		d = self.getD(phi,e)
		print("d : " + str(d))
		n = p*q
		return (n, d, e)

	def getGCD(self,a, b):
		if b == 0:
			return a
		else:
			return self.getGCD(b,a%b) 

	def getPhi(self,p,q):
		return (p-1)*(q-1)

	def getE(self,phi):
		for j in range(2, phi):
			if self.getGCD(j,phi) == 1: #nombre premier entre eux
				return j
		return 1

	def getD(self,phi, e):
		return self.getModInverse(e, phi)

	def getModInverse(self,a, m):
		for x in range(1, m):
			if (((a%m) * (x%m)) % m == 1):
				return x
		return -1

	def decyferKey(self, n, e , key):
		return pow(key, e)%n

	def cyferKey(self, n , d, key):
		return self.getModInverse(pow(key, d), n)
    	


n = 391
d = 235
rsa = RSA()
i = 331#304077315045304228040315356

#n, d, e = rsa.generateKey(391,235)

#print(f"n : {n} | d : {d} | e : {e}")
encodedStr = "331 304 077 315 045 304 228 040 315 356"

for val in encodedStr.split(' '):
    print(chr(rsa.decyferKey(n, d, int(val))), end='')

print()


