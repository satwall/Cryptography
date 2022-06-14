import os
import random
import string
import binascii

def main():
    plainText = ""
    while True:
        cipherL = input("Please input 'file' if it's a file or 'input' if it's an input? ")
        if cipherL == "file":
            plain = input("Please enter the file name: ")
            plainText += open(plain, 'r').read()
            break
        elif cipherL == "input":
            plainText = input("Please enter the text: ")
            break
        else:
            print("Your response was invalid, please enter 'file' or 'input'")


    key2 = createK(len(plainText))
    print("Key:", key2)

    cipherText = xorCompare2(plainText, key2)
    print("Ciphertext:", cipherText)

    print("------")

    verify2 = input("Do you want to decrypt using the above ciphertext (Y/N)? ")
    if verify2 == "Y":
        cipher22 = input("Please enter the ciphertext: ")
        key22 = input("Please enter the key: ")
        print("This is the decryption of the ciphertext and key entered: ", xorCompare2(cipher22, key22))
    print("------")
    save2 = input("Do you want to save the ciphertext (Y/N)? ")
    if save2 == "Y":
        fileName = input("Please enter the name of the file: ")
        outputfile = open(fileName, "w")
        outputfile.write(cipherText)
        outputfile.close()
    else:
        print("Shutting Down.")


#def xorCompare(b1, b2):
    #return '{0:0{1}b}'.format(int(b1,2) ^ int(b2, 2), len(b1))

def xorCompare2(plainText, key2):
    return "".join(chr(ord(a) ^ ord(b)) for a,b in zip(plainText, key2))

def createK(cipherLen):
    allchars = string.ascii_letters + string.punctuation + string.digits
    return "".join(random.choice(allchars) for x in range(cipherLen))


if __name__ == "__main__":
    main()
