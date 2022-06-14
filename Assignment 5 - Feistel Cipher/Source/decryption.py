from filehandling import read_file
from filehandling import save_file

sample_bin_string = '00111111'


class EncryptedData:

	def __init__(self,file_type,input_file,block_size,round,key,output_file):
		self.file_type = file_type
		self.input_file = input_file
		self.block_size = block_size
		self.round = round
		self.key = key
		self.output_file = output_file



	def split_blocks(self,text_bin,block_size):
		text_bin_blocks = []

		text_bin_blocks = [text_bin[i:i+block_size] for i in range (0,len(text_bin),block_size)]


		#print(plaintext_bin_blocks)
		return (text_bin_blocks)




	def decryption_singleblock(self,plaintext_bin_block,round,key):
		feistal_blocks = self.split_blocks(plaintext_bin_block,int(len(plaintext_bin_block)/2))

		L = []
		R = []

		#print(feistal_blocks[1])
		


		# initial round
		L.append(feistal_blocks[0])
		R.append(feistal_blocks[1])

		# after inital round
		for n in range(1,round):
			#print (type(R[n-1]))
			R.append(L[n-1])
			L.append((format((int(R[n-1],2)^int(self.scramblingfunction(L[n-1],round-n,key),2)),'04b')))




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


	def decryption_img_blocks(self,plaintext_bin_blocks,round,key):
		#for block in plaintext_bin_blocks:

		encrypted_blocks = []

		# How many block to skip, to avoid modifying BMP header, 432 = 54 bytes
		n = int((432/len(plaintext_bin_blocks[0]))) + (432%len(plaintext_bin_blocks[0])>0)
		print(n)

		for block in plaintext_bin_blocks[0:n]:
			#print(block)
			encrypted_blocks.append(block)

		#print(encrypted_blocks)


		for block in plaintext_bin_blocks[n:len(plaintext_bin_blocks)]:
			#print(block)
			encrypted_blocks.append(self.decryption_singleblock(block,round,key))


		encrypted_blocks = ''.join(encrypted_blocks)

		#print(len(encrypted_blocks))
		return (encrypted_blocks)


	def decryption_txt_blocks(self,plaintext_bin_blocks,round,key):
		#for block in plaintext_bin_blocks:

		encrypted_blocks = []


		for block in plaintext_bin_blocks:
			#print(block)
			encrypted_blocks.append(self.decryption_singleblock(block,round,key))


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

	def decryption(self):

		if self.file_type ==1:

			file_bin_string = read_file(self.input_file)

			text_blocks = self.split_blocks(file_bin_string,self.block_size)

			decrypted_bin_string = self.decryption_img_blocks(text_blocks,self.round,self.key)

			save_file(decrypted_bin_string,self.output_file)


		else:

			file_bin_string = read_file(self.input_file)

			text_blocks = self.split_blocks(file_bin_string,self.block_size)

			decrypted_bin_string = self.decryption_txt_blocks(text_blocks,self.round,self.key)

			save_file(decrypted_bin_string,self.output_file)






if __name__ == '__main__':

	####################################################################################################################
	#Decryption
	####################################################################################################################

	file_type = 1

	input_file = 'encrypted.bmp'

	output_file = 'decrypted.bmp'

	key =12

	Encrypted_data = EncryptedData(file_type,input_file,8,16,key,output_file)

	Encrypted_data.decryption()
