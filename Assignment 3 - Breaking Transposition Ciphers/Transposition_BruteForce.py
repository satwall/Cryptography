import sys, math
from ProvidedScripts import detectEnglish ##Imports detectEnglish script from the folder ProvidedScripts

def decryptMessage(k, m):
        #nR = math.ceil((
        nC = math.ceil(len(m)/k)
        nR = k
        nUnused = (nC * nR) - len(m)
        plainText =[''] * nC
        #print(plainText)
        row = col = 0
        for symbol in m: 
                plainText[col] += symbol
                col += 1

                if (col == nC) or (col == nC - 1 and row >= nR - nUnused):
                        col = 0
                        row += 1
       # return
        return ''.join(plainText)

###Using command line to enter prompt (-c)
#def main(argv):
    #message = ""
    #if len (sys.argv[1:]) < 2:
        #print ('Usage: ./Transposition_BruteForce.py -c <Input Ciphertext Message>')
    #parser = argparse.ArgumentParser()


def main():
        #cipherText = input("Input the cipher text: ")
        #print(cipherText)
        cipherText = ""
        while True:
                cipherW = input("Please input 'file' if it's a file or 'input' if it's an input? ")
                #print(cipherW)
                if cipherW == "file":
                        cipher = input("Please enter the name of the file: ")
                        cipherText += open(cipher, 'r').read()
                        print(cipherText)
                        break #Added break otherwise it would infinite loop 
                elif cipherW == "input":
                        cipher = input("Please enter the cipher text: ")
                        cipherText = cipher
                        print(cipherText)
                        break #Added break otherwise it would infinite loop
                else:
                        print("Your response was invalid, please enter 'file' or 'input'")


        for k in range(len(cipherText) - 1):
                print("Testing Key... %d" % (k + 1))
                #print("Testing Plaintext....%s" % plainText)
                plainText = decryptMessage(k + 1, cipherText.strip('\n'))
                if detectEnglish.FindEnglish(plainText):
                        print('Potential Key is: %d' % (k + 1))
                        print('POtential Plaintext is: %s' % plainText)
                        check=input("Do you want to continue checking? ('Y' for yes, 'N' for no) ")
                        if check == "N":
                                print('The Key is: %d' % (k + 1))
                                print('The Plaintext is: %s' % plainText)
                                sys.exit()
                        else:
                                print('Continuing')
        
if __name__=="__main__":
        main()
