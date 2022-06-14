from hashlib import sha256
import pandas as pd

#input_=input('Enter Something: ')
#print(sha256(input_.encode('utf-8')).hexdigest())

#a, b, c, d = [input("Enter the first word: ").split()]

a=input('Enter the first word: ')
b=input('Enter the second word: ')
#c=input('Enter the third word: ')
#d=input('Enter the fourth word: ')

A=(sha256(a.encode('utf-8')).hexdigest())
B=(sha256(b.encode('utf-8')).hexdigest())
#C=(sha256(c.encode('utf-8')).hexdigest())
#D=(sha256(d.encode('utf-8')).hexdigest())

print(A)
print(B)
#print(C)
#print(D)
#test = {'User Input':[a,b,c,d], 'sha256 Output':[A,B,C,D]}

def countBits(x):
    count=0
    while x>0:
        count += x & 1
        #x <<= 1
        x >>= 1
    return count

def compareHash(A,B):
    hashA=''.join('{0:08b}'.format(ord(x), 'b') for x in a)
    hashB=''.join('{0:08b}'.format(ord(x), 'b') for x in b)
    print (hashA)
    print (hashB)
    cH='{0:b}'.format(int(hashA,2) ^ int(hashB,2))
    cH=int(str(cH),2)
    cH=countBits(cH)
    return cH

print(compareHash(A,B))

hashA=''.join('{0:08b}'.format(ord(x), 'b') for x in a)
hashB=''.join('{0:08b}'.format(ord(x), 'b') for x in b)


test = {'User Input':[a,b], 'sha256 Output':[A,B], 'Binary Format':[hashA,hashB]}

df = pd.DataFrame(test, columns=['User Input','sha256 Output','Binary Format'])

df.to_csv(r'sha256_export.csv')
