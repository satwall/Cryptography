def read_file(file_name):

	file1 = open(file_name,'rb')

	data = file1.read()

	file1.close()

	bin_array = []

	for b in data:
		#bin_array[n] = format(b,'08b')
		bin_array.append(format(b,'08b'))

	#return bin_array

	bin_string = ''

	bin_string = ''.join(bin_array)

	return (bin_string)

def save_file(file_bin_string,file_name):


	n = 8

	byte_array = []

	file_bin_array = []

	file_bin_array = [file_bin_string[i:i+n] for i in range(0,len(file_bin_string),n)]


	for b in file_bin_array:
		byte_array.append(int(b,2))

	byte_array = bytearray(byte_array)

	file2 = open(file_name,'wb')
	file2.write(byte_array)
	file2.close()

	#print (byte_array)






if __name__ == '__main__':

	#file_bin_array = read_file('003.3.jpg')
	#save_file(file_bin_array,'output.jpg')

	file_bin_string = read_file('LAND2.BMP')

	#print(file_bin_string)

	print(len(file_bin_string))

	save_file(file_bin_string,'output.bmp')

