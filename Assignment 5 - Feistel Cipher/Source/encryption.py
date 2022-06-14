from filehandling import read_file
from filehandling import save_file

sample_bin_string = '1100111011100110'




class PlainData:

	def __init__(self,file_type,input_file,block_size,round,key,output_file):
			self.file_type = file_type
			self.input_file = input_file
			self.block_size = block_size
			self.round = round
			self.key = key
			self.output_file = output_file




	def split_blocks(self,plaintext_bin,block_size):
		plaintext_bin_blocks = []

		plaintext_bin_blocks = [plaintext_bin[i:i+block_size] for i in range (0,len(plaintext_bin),block_size)]


		#print(plaintext_bin_blocks)
		return (plaintext_bin_blocks)




	def encryption_singleblock(self,plaintext_bin_block,round,key):
		feistal_blocks = self.split_blocks(plaintext_bin_block,int(len(plaintext_bin_block)/2))

		L = []
		R = []

		#print(feistal_blocks[1])
		


		# initial round
		L.append(feistal_blocks[0])
		R.append(feistal_blocks[1])

		#print(int(L[1-1],2))
		#print(int(R[1-1],2))
		
		# after inital round
		for n in range(1,round):
			#print (type(R[n-1]))
			L.append(R[n-1])
			#R.append((format((int(L[n-1],2)^int(R[n-1],2)),'04b')))
			R.append((format((int(L[n-1],2)^int(self.scramblingfunction(R[n-1],n,key),2)),'04b')))




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


	def encryption_img_blocks(self,plaintext_bin_blocks,round,key):
		#for block in plaintext_bin_blocks:

		encrypted_blocks = []

		# How many blocks to skip, to avoid modifying BMP header, 432 = 54 bytes
		n = int((432/len(plaintext_bin_blocks[0]))) + (432%len(plaintext_bin_blocks[0])>0)
		print(n)

		for block in plaintext_bin_blocks[0:n]:
			#print(block)
			encrypted_blocks.append(block)

		#print(encrypted_blocks)


		for block in plaintext_bin_blocks[n:len(plaintext_bin_blocks)]:
			#print(block)
			encrypted_blocks.append(self.encryption_singleblock(block,round,key))


		encrypted_blocks = ''.join(encrypted_blocks)

		#print(len(encrypted_blocks))
		return (encrypted_blocks)


	def encryption_txt_blocks(self,plaintext_bin_blocks,round,key):
		#for block in plaintext_bin_blocks:

		encrypted_blocks = []


		for block in plaintext_bin_blocks:
			#print(block)
			encrypted_blocks.append(self.encryption_singleblock(block,round,key))


		encrypted_blocks = ''.join(encrypted_blocks)

		#print(len(encrypted_blocks))
		return (encrypted_blocks)




	def scramblingfunction(self,plaintext,i,k):
		plaintext = str(plaintext)
		plainnum = int(plaintext,2)
		i = int(i)
		k = int(k)
		opt = (pow((2*i*k),plainnum)) % 15
		opt = format(opt,'04b')

		#print(opt)
		#opt = bin(opt)

		#print(opt)
		return (opt)


	def encryption(self):

		if self.file_type ==1:

			file_bin_string = read_file(self.input_file)

			plaintext_blocks = self.split_blocks(file_bin_string,self.block_size)

			encrypted_bin_string = self.encryption_img_blocks(plaintext_blocks,self.round,self.key)

			save_file(encrypted_bin_string,self.output_file)


		else:

			file_bin_string = read_file(self.input_file)

			plaintext_blocks = self.split_blocks(file_bin_string,self.block_size)

			encrypted_bin_string = self.encryption_txt_blocks(plaintext_blocks,self.round,self.key)

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

	plaintext_data = PlainData(file_type,input_file,8,16,key,output_file)

	plaintext_data.encryption()