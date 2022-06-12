import RSA_keys as keys
import argparse as argp
from os.path import exists
from base64 import b64encode

def encrypt(filename, pubk):
    with open(filename) as file, open('encrypted.txt', 'w') as ciph:
        number_text = ''
        for char in file.read():
            number_text += str(ord(char))
        print('Encrypting...')
        enc_text = ''
        indicies = [i for i in range(0, len(number_text)-1)]
        indicies = indicies[slice(0, len(number_text)-1, 3)]
        for i in indicies:
            if (i+3 > len(number_text)-1):
                enc_text += str(pow(int(number_text[i:]), pubk[0], pubk[1])) + ' ' 
            else:
                enc_text += str(pow(int(number_text[i:i+3]), pubk[0], pubk[1])) + ' '
        enc_text = enc_text[:-1].encode('ascii')
        enc_text = b64encode(enc_text)
        ciph.write(enc_text.decode('ascii'))
        print('Encryption complete')
        

if(__name__=='__main__'):
    parser = argp.ArgumentParser(description='Encrypt a message using RSA')
    parser.add_argument('prime', metavar='prime', type=int, help='Number to which generate primes')
    parser.add_argument('text', metavar='file', type=str, help='File to encrypt')

    args = parser.parse_args()
    if not(exists(args.text)):
        print('File {} does not exist'.format(args.text))
        exit()
    encrypt(args.text, args.prime)