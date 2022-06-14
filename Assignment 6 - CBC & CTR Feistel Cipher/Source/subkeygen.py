''''
Design:
	1.Take 24 bits integer
	2.PC1 to select 16 bits
	3.Divided to 2 parts, 8 bits each (C and D)
	4.Left shift 1 bit each for C section and right shit 1 bit each for D section
	And  repeat 8 rounds

Produce the key:
	Reconnect 2 sections (C and D)
	PC2 to select 8 bits
'''

# pc1 - selecting 16 bits from 24 bits
pc1 = [22,0,8,2,5,16,18,7,3,1,12,15,6,20,15,11]

# pc2 - slecting 8 bits from 16 bits
pc2 = [7,8,12,3,6,5,8,11]



#key_bin = ''.join(format(sample_key,'024b'))


class Subkey_Gen:

	def __init__(self,sample_key,num_round):
		self.sample_key = sample_key
		self.round = num_round



	#devide into 2 parts
	def initialize(self):

		key_ord = ''

		for char in self.sample_key:
			key_ord += str(ord(char))

		key_ord = int(key_ord)
		key_bin = ''.join(format(key_ord,'024b'))
		
		# filter with pc 1
		pc1_bin =''
		for i in pc1:
			pc1_bin += key_bin[23-i]

		#print(key_bin)
		#print (pc1_bin)

		c = ''
		d = ''
		for i in range (0,8):
			c += pc1_bin[i]

		for i in range(8,16):
			d += pc1_bin[i]

		return c,d


	# shifts
	def bit_left_shit(self,bi):
		#bi = (int(bi,2))
		#bi = bi<<1
		#bi_otp  = ''.join(format(bi,'08b'))


		bi_otp = ''
		for i in range(1,8):
			bi_otp += bi[i]

		bi_otp += bi[0]

		return bi_otp

	def bit_right_shit(self,bi):
		bi_otp = ''
		bi_otp += bi[7]
		for i in range(0,7):
			bi_otp += bi[i]



		return bi_otp


	def pc2_gen(self,c,d):
		key_bi = c+d

		pc2_bin =''
		for i in pc2:
			pc2_bin += key_bi[15-i]

		#print(pc2_bin)
		return int(pc2_bin,2)

	def encryption_key(self):

		keys = []

		key_bi = self.initialize()
		c = key_bi[0]
		d = key_bi[1]

		for n in range(0,self.round):
			c = self.bit_left_shit(c)
			d = self.bit_right_shit(d)
			#print(c,d)
			pc2_opt = self.pc2_gen(c,d)
			keys.append(pc2_opt)

		return keys



if __name__ == '__main__':

	sample_key = input('Please enter the key: ')

	en_keys = Subkey_Gen(sample_key,8)
	en_keys = en_keys.encryption_key()
	print(en_keys)





