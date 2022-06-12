import RSA_encrypt
import RSA_decrypt
import RSA_keys
from os.path import exists
from base64 import b64decode, b64encode

if (__name__ == '__main__'):
    print('Starting RSA...')
    keysG = False
    while(True):
        match(input('Select an option: g-generate keys, e-encrypt, d-decrypt, q-quit ').strip()):
            case 'g':
                prime = input('Input a number to which generate primes: ').strip()
                if (not prime.isnumeric()):
                    print('Input is not numeric. Returning...')
                    continue
                pubk, prvk = RSA_keys.generateKeys(int(prime))
                accPubKey = str(pubk[0]) + ' ' + str(pubk[1])
                accPrvKey = str(prvk[0]) + ' ' + str(prvk[1])
                accPubKey = b64encode(str(accPubKey).encode('ascii')).decode('ascii')
                accPrvKey = b64encode(str(accPrvKey).encode('ascii')).decode('ascii')    
                print('Generated public pair: {}'.format(pubk))
                print(f'Public key: {accPubKey}')
                print('Generated private pair: {}'.format(prvk))
                print(f'Private key: {accPrvKey}')
                keysG = True
            case 'e':
                br = False
                if (not keysG):
                    print('No key was generated this session.')
                    while (not br):
                        match(input('Input own key? [y/n] ').strip().lower()):
                            case 'y':
                                pubk = tuple(b64decode((input('Input public key: ').strip()).encode('ascii')).decode('ascii').split())
                                pubk = (int(pubk[0]), int(pubk[1]))
                                break
                            case 'n':
                                br = True
                            case _:
                                print('Unknown option')
                if (br):
                    continue
                file = input('File to encrypt: ').strip()
                if not(exists(file)):
                    print('File not found. Returning...')
                    continue
                RSA_encrypt.encrypt(file, pubk)
            case 'd':
                br = False
                if (not keysG):
                    print('No key was generated this session.')
                    while (not br):
                        match input('Input own key? [y/n] ').strip().lower():
                            case 'y':
                                prvk = tuple(b64decode((input('Input private key: ').strip()).encode('ascii')).decode('ascii').split())
                                prvk = (int(prvk[0]), int(prvk[1]))
                                break
                            case 'n':
                                br = True
                            case _:
                                print('Unknown option')
                if (br):
                    continue
                file = input('File to decrypt: ').strip()
                if not(exists(file)):
                    print('File not found. Returning...')
                    continue
                RSA_decrypt.decrypt(file, prvk)
            case 'q':
                exit()
            case _:
                print('Unknown option')
    