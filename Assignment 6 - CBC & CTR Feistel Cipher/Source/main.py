from encryption import PlainData
from decryption import EncryptedData
from subkeygen import Subkey_Gen

###################################################################################################################
############################# default configuration, for testing purpose ##########################################
###################################################################################################################


opt_mode = 0

file_type = 1

input_file = 'sample1.bmp'

output_file = 'encrypted.bmp'

key = 12

num_round = 8



###################################################################################################################
############################################# mian function #######################################################
###################################################################################################################

try:

	opt_mode = int(input('Please enter the operation mode (Choose the number of the mode):\n1.Encryption Mode\n2.Decryption Mode\n: '))

	file_type = int(input('Please enter the file type (Choose the number of the file type):\n1.Image FIle (Only supporting BMP format)\n2.Text File\n: '))

	input_file = input('Please enter the input file name/path: ')

	output_file = input('Please enter the output file name/path: ')

	
	while True:

		key = input('Please enter the encryption key to use(Can be Alphabet or Number. For best security, more than 3 character long): ')

		if len(key) >= 3:
			en_keys = Subkey_Gen(key,8)
			en_keys = en_keys.encryption_key()
			for k in en_keys:
				print('Generate Subkey:'+str(k))

			break

		else:
			print ('[Warning] For best security, the key needs to be more than 3 character long')
			continue



	cipher_mode = int(input('Please choose the block cipher encryption mode (Choose the number of the mode):\n1.ECB\n2.CBC\n3.CTR\n: '))



except:
	print('[Error:] Please enter the correct input')
	exit()




if opt_mode == 1:
		#print (opt_mode)

	try:

		if cipher_mode == 1:

			plaintext_data = PlainData(file_type,input_file,8,num_round,key,output_file)

			print ('-'*100+'\n Encrypting, please wait\n' + '-'*100)

			plaintext_data.ecb_encryption()


		elif cipher_mode == 2:

			plaintext_data = PlainData(file_type,input_file,8,num_round,key,output_file)

			print ('-'*100+'\n Encrypting, please wait\n' + '-'*100)

			plaintext_data.cbc_encryption()


		elif cipher_mode == 3:

			counter = int(input('Please enter the inital counter number (Any integer number):'))

			plaintext_data = PlainData(file_type,input_file,8,num_round,key,output_file,counter)


			print ('-'*100+'\n Encrypting, please wait\n' + '-'*100)

			plaintext_data.ctr_encryption()

		else:
			print('[Error:] Please enter the correct encryption mode')
			exit()

	except:
	
		print('[Error:] Please enter the correct input')
		exit()


	print('Finishsed encryption, please check the folder')

	exit()


if opt_mode == 2:
		#print(opt_mode)
	try:

		if cipher_mode == 1:

			Encrypted_data = EncryptedData(file_type,input_file,8,num_round,key,output_file)

			print ('-'*100+'\n Decrypting, please wait\n' + '-'*100)

			Encrypted_data.ecb_decryption()

		elif cipher_mode == 2:

			Encrypted_data = EncryptedData(file_type,input_file,8,num_round,key,output_file)

			print ('-'*100+'\n Decrypting, please wait\n' + '-'*100)

			Encrypted_data.cbc_decryption()


		elif cipher_mode == 3:

			counter = int(input('Please enter the inital counter number:'))

			Encrypted_data = EncryptedData(file_type,input_file,8,num_round,key,output_file,counter)

			print ('-'*100+'\n Decrypting, please wait\n' + '-'*100)

			Encrypted_data.ctr_decryption()

	except:
	
		print('[Error:] Please enter the correct input')
		exit()

	print('Finished decryption, please check the folder')

	exit()


else:
	print('[Error:] Please select the correct operation mode using the number')
	exit()


