from filehandling import read_file
from filehandling import save_file
from subkeygen import Subkey_Gen

sample_bin_string = '1100111011100110'




class PlainData:

	def __init__(self,file_type,input_file,block_size,round,key,output_file,counter=None):
			self.file_type = file_type
			self.input_file = input_file
			self.block_size = block_size
			self.round = round
			self.key = key
			self.output_file = output_file
			self.counter = counter



	def split_blocks(self,plaintext_bin,block_size):
		plaintext_bin_blocks = []

		plaintext_bin_blocks = [plaintext_bin[i:i+block_size] for i in range (0,len(plaintext_bin),block_size)]


		#print(plaintext_bin_blocks)
		return (plaintext_bin_blocks)




	def encryption_singleblock(self,plaintext_bin_block,round,key,counter):
		feistal_blocks = self.split_blocks(plaintext_bin_block,int(len(plaintext_bin_block)/2))

		L = []
		R = []

		#print(feistal_blocks[1])
		


		# initial round
		L.append(feistal_blocks[0])
		R.append(feistal_blocks[1])

		#print(int(L[1-1],2))
		#print(int(R[1-1],2))


		en_keys = Subkey_Gen(key,round)
		en_keys = en_keys.encryption_key()
		

		# after inital round
		for n in range(1,round):

			k = en_keys[n-1]

			#print (type(R[n-1]))
			L.append(R[n-1])
			#R.append((format((int(L[n-1],2)^int(R[n-1],2)),'04b')))
			R.append((format((int(L[n-1],2)^int(self.scramblingfunction(R[n-1],n,k,counter),2)),'04b')))




		#L.append(''.join(feistal_blocks[0]))
		#R.append(''.join(feistal_blocks[1]))

		#L.append([plaintext_bin_blocks[i] for i in range (0,len(plaintext_bin_blocks,2))])
		#R.append([plaintext_bin_blocks[i] for i in range (1,len(plaintext_bin_blocks,2))])

		opt = L[round-1] + R[round-1]
		#print(opt)
		#encrypted_blocks[0] = 
		#for i in range(1,plaintext_blocks):
			#encrypted_blocks[i] =  
		return(opt)


	def ecb_encryption_img_blocks(self,plaintext_bin_blocks,round,key):
		#for block in plaintext_bin_blocks:

		encrypted_blocks = []

		# How many blocks to skip, to avoid modifying BMP header, 432 = 54 bytes
		n = int((432/len(plaintext_bin_blocks[0]))) + (432%len(plaintext_bin_blocks[0])>0)
		print('Skipping header: '+str(n)+'bytes long')

		for block in plaintext_bin_blocks[0:n]:
			#print(block)
			encrypted_blocks.append(block)

		#print(encrypted_blocks)


		for block in plaintext_bin_blocks[n:len(plaintext_bin_blocks)]:
			#print(block)
			encrypted_blocks.append(self.encryption_singleblock(block,round,key,0))


		#print (len(encrypted_blocks))
		encrypted_blocks = ''.join(encrypted_blocks)

		#print(len(encrypted_blocks))
		return (encrypted_blocks)


	def ecb_encryption_txt_blocks(self,plaintext_bin_blocks,round,key):
		#for block in plaintext_bin_blocks:

		encrypted_blocks = []


		for block in plaintext_bin_blocks:
			#print(block)
			encrypted_blocks.append(self.encryption_singleblock(block,round,key,0))


		encrypted_blocks = ''.join(encrypted_blocks)

		print(len(encrypted_blocks))
		return (encrypted_blocks)



	def cbc_encryption_img_blocks(self,plaintext_bin_blocks,round,key):
		#for block in plaintext_bin_blocks:

		encrypted_blocks = []

		# How many blocks to skip, to avoid modifying BMP header, 432 = 54 bytes
		n = int((432/len(plaintext_bin_blocks[0]))) + (432%len(plaintext_bin_blocks[0])>0)
		print('Skipping header: '+str(n)+'bytes long')

		for block in plaintext_bin_blocks[0:n]:
			#print(block)
			encrypted_blocks.append(block)

		#print(encrypted_blocks)

		# First encrytped block:
		encrypted_blocks.append(self.encryption_singleblock(plaintext_bin_blocks[n],round,key,0))
		n = n+1

		for i in range(n,len(plaintext_bin_blocks)):
			block = int(plaintext_bin_blocks[i],2)^int(encrypted_blocks[i-1],2)
			block = format(block,'08b')
			#print(block)
			encrypted_blocks.append(self.encryption_singleblock(block,round,key,0))


		#print (len(encrypted_blocks))
		#print(encrypted_blocks)
		encrypted_blocks = ''.join(encrypted_blocks)

		#print(len(encrypted_blocks))
		return (encrypted_blocks)


	def cbc_encryption_txt_blocks(self,plaintext_bin_blocks,round,key):
		#for block in plaintext_bin_blocks:

		encrypted_blocks = []

		# First encrypted block:
		encrypted_blocks.append(self.encryption_singleblock(plaintext_bin_blocks[0],round,key,0))	


		for i in range(1,len(plaintext_bin_blocks)):
			block = int(plaintext_bin_blocks[i],2)^int(encrypted_blocks[i-1],2)
			block = format(block,'08b')
			#print(block)
			encrypted_blocks.append(self.encryption_singleblock(block,round,key,0))


		encrypted_blocks = ''.join(encrypted_blocks)

		print(len(encrypted_blocks))
		return (encrypted_blocks)



	def ctr_encryption_img_blocks(self,plaintext_bin_blocks,round,key,counter):
		#for block in plaintext_bin_blocks:

		encrypted_blocks = []

		# How many blocks to skip, to avoid modifying BMP header, 432 = 54 bytes
		n = int((432/len(plaintext_bin_blocks[0]))) + (432%len(plaintext_bin_blocks[0])>0)
		print('Skipping header: '+str(n)+'bytes long')

		for block in plaintext_bin_blocks[0:n]:
			#print(block)
			encrypted_blocks.append(block)

		#print(encrypted_blocks)

		counter = counter
		for block in plaintext_bin_blocks[n:len(plaintext_bin_blocks)]:
			#print(block)
			encrypted_blocks.append(self.encryption_singleblock(block,round,key,counter))
			counter += 1


		#print (len(encrypted_blocks))
		encrypted_blocks = ''.join(encrypted_blocks)

		#print(len(encrypted_blocks))
		return (encrypted_blocks)


	def ctr_encryption_txt_blocks(self,plaintext_bin_blocks,round,key,counter):
		#for block in plaintext_bin_blocks:

		encrypted_blocks = []

		counter = counter

		for block in plaintext_bin_blocks:
			#print(block)
			encrypted_blocks.append(self.encryption_singleblock(block,round,key,counter))
			counter += 1


		encrypted_blocks = ''.join(encrypted_blocks)

		print(len(encrypted_blocks))
		return (encrypted_blocks)



	def scramblingfunction(self,plaintext,i,k,c):

		plaintext = str(plaintext)
		plainnum = int(plaintext,2)
		i = int(i)
		k = int(k)
		opt = (pow((2*i*k+c),plainnum)) % 15
		opt = format(opt,'04b')

		#print(opt)
		#opt = bin(opt)

		#print(opt)
		return (opt)


	def ecb_encryption(self):

		if self.file_type ==1:

			file_bin_string = read_file(self.input_file)

			plaintext_blocks = self.split_blocks(file_bin_string,self.block_size)

			encrypted_bin_string = self.ecb_encryption_img_blocks(plaintext_blocks,self.round,self.key)

			save_file(encrypted_bin_string,self.output_file)


		else:

			file_bin_string = read_file(self.input_file)

			plaintext_blocks = self.split_blocks(file_bin_string,self.block_size)

			encrypted_bin_string = self.ecb_encryption_txt_blocks(plaintext_blocks,self.round,self.key)

			save_file(encrypted_bin_string,self.output_file)


	def cbc_encryption(self):

		if self.file_type ==1:

			file_bin_string = read_file(self.input_file)

			plaintext_blocks = self.split_blocks(file_bin_string,self.block_size)

			encrypted_bin_string = self.cbc_encryption_img_blocks(plaintext_blocks,self.round,self.key)

			save_file(encrypted_bin_string,self.output_file)


		else:

			file_bin_string = read_file(self.input_file)

			plaintext_blocks = self.split_blocks(file_bin_string,self.block_size)

			encrypted_bin_string = self.cbc_encryption_txt_blocks(plaintext_blocks,self.round,self.key)

			save_file(encrypted_bin_string,self.output_file)


	def ctr_encryption(self):

		if self.file_type ==1:

			file_bin_string = read_file(self.input_file)

			plaintext_blocks = self.split_blocks(file_bin_string,self.block_size)

			encrypted_bin_string = self.ctr_encryption_img_blocks(plaintext_blocks,self.round,self.key,self.counter)

			save_file(encrypted_bin_string,self.output_file)


		else:

			file_bin_string = read_file(self.input_file)

			plaintext_blocks = self.split_blocks(file_bin_string,self.block_size)

			encrypted_bin_string = self.ctr_encryption_txt_blocks(plaintext_blocks,self.round,self.key,self.counter)

			save_file(encrypted_bin_string,self.output_file)


if __name__ == '__main__':

	####################################################################################################################
	#Image Encryption
	####################################################################################################################


	#print(plaintext_blocks)
	#encryption_singleblock (plaintext_blocks[0],16,7)
	#scramblingfunction('1000',1,7)
	#print(encrypted_bin_string)




	#file_bin_string = read_file('sample2.bmp')

	#plaintext_blocks = split_blocks(file_bin_string,8)

	#encrypted_bin_string = encryption_img_blocks(plaintext_blocks,16,7)

	#save_file(encrypted_bin_string,'output.bmp')


	####################################################################################################################
	#Text Encryption
	####################################################################################################################

	#file_bin_string = read_file('sample1.bmp')

	#plaintext_blocks = split_blocks(file_bin_string,8)
	#print(plaintext_blocks)
	#encryption_singleblock (plaintext_blocks[0],16,7)
	#scramblingfunction('1000',1,7)

	#encrypted_bin_string = encryption_img_blocks(plaintext_blocks,16,25)

	#print(encrypted_bin_string)

	#save_file(encrypted_bin_string,'output.bmp')



	file_type = 1

	input_file = 'sample1.bmp'

	output_file = 'encrypted.bmp'

	key = 12

	plaintext_data = PlainData(file_type,input_file,8,16,key,output_file,5)

	plaintext_data.ctr_encryption()