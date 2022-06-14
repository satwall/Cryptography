from encryption import PlainData
from decryption import EncryptedData


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

	opt_mode = int(input('Please enter the operation mode (Choose the number of the mode):\n1.Encryption Mode\n2.Decryption Mode\n:'))

	file_type = int(input('Please enter the file type (Choose the number of the file type):\n1.Image FIle (Only supporting BMP format)\n2.Text File\n:'))

	input_file = input('Please enter the input file name/path: ')

	output_file = input('Please enter the output file name/path: ')

	key = int(input('Please enter the encryption key (Any integer number) to use: '))

except:
	print('[Error:] Please enter the correct inputs')
	exit()




if opt_mode == 1:
		#print (opt_mode)

	try:

		plaintext_data = PlainData(file_type,input_file,8,num_round,key,output_file)

		print ('-'*100+'\n Encrypting, please wait\n' + '-'*100)

		plaintext_data.encryption()

	except:
	
		print('[Error:] Please enter the correct input')
		exit()


	print('Encryption has finished, please check the folder')

	exit()


if opt_mode == 2:
		#print(opt_mode)
	try:

		Encrypted_data = EncryptedData(file_type,input_file,8,num_round,key,output_file)

		print ('-'*100+'\n Decrypting, please wait\n' + '-'*100)

		Encrypted_data.decryption()

	except:
	
		print('[Error:] Please enter the correct input')
		exit()

	print('Decryption has finished, please check the folder')

	exit()


else:
	print('[Error:] Please select the correct operation mode using the number')
	exit()


