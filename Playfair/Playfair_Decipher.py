import argparse as argp
import string
from os.path import exists
from sys import exit as sys_exit

def generateAlphabet(key):
    key = key.upper()
    alphabet = [[] for _ in range(5)]
    letter = 0
    standard_letter = 0
    standard_alph = string.ascii_uppercase
    key = key.replace('J', "I")
    for row in alphabet:
        i = 0
        while (letter < len(key)):
            if not(key[letter].isalpha()):
                print('Non letter character in key omitted')
                letter += 1
                continue
            if (any(key[letter] in r for r in alphabet)):
                letter += 1
                continue
            row.append(key[letter])
            i += 1
            letter += 1
            if (i == 5):
                break
        if (letter == len(key)):
            while (standard_letter < len(standard_alph)):
                if (standard_alph[standard_letter] == 'J' or any(standard_alph[standard_letter] in r for r in alphabet)):
                    standard_letter += 1
                    continue
                row.append(standard_alph[standard_letter])
                standard_letter += 1
                i += 1
                if (i == 5):
                    break
    return alphabet

def playfair(filename, alphabet):
    if (filename == -1):
        print('Enter cipher:')
        cipher = input().strip()
    else:
        file = open(filename, encoding="utf-8")
        cipher = file.read()
        file.close()
    cipher = cipher.upper()
    '''regex = re.compile('[^A-Z]')
    cipher = regex.sub('', cipher)
    cipher = list(map(''.join, zip(*[iter(cipher)]*2)))'''
    text = ''
    j = 0
    while (j < len(cipher)):
        tmp = ''
        if not (cipher[j].isalpha()):
            text += cipher[j]
            j += 1
            if (j == len(cipher)):
                break
            continue
        lett1 = cipher[j]
        j += 1
        try:
            while not (cipher[j].isalpha()):
                tmp += cipher[j]
                j += 1
                if (j == len(cipher)):
                    break
            lett2 = cipher[j]
        except IndexError:
            print('File contains uneven number of letters!')
            print('Check if cipher is correct')
            sys_exit()
        j += 1
        for i in range(5):
            if (lett1 in alphabet[i]):
                i0 = i
                j0 = alphabet[i].index(lett1)
            if (lett2 in alphabet[i]):
                i1 = i
                j1 = alphabet[i].index(lett2)
        if (i0 == i1):
            text += alphabet[i0][(j0-1)%5] + tmp + alphabet[i1][(j1-1)%5]
        elif (j0 == j1):
            text += alphabet[(i0-1)%5][j0] + tmp + alphabet[(i1-1)%5][j1]
        else:
            text += alphabet[i0][j1] + tmp + alphabet[i1][j0]
    if (filename == -1):
        print(text)
    else:
        filename = filename.split('.')
        file = open(filename[0]+'_deciphered.'+filename[1], 'w', encoding='utf-8')
        file.write(text)
        file.close()
        print('File deciphered')
    return

if __name__ == '__main__':
    parser = argp.ArgumentParser(description='Decipher text using playfair cipher')
    parser.add_argument('key', metavar='key', type=str, help='key word to be used')
    parser.add_argument('-f', '--file', type=str, help='[optional] file containing text to be deciphered')

    args = parser.parse_args()
    
    if (args.file):
        if not(exists(args.file)):
            print('Cipher file does not exist')
        else:
            playfair(args.file, generateAlphabet(args.key))
    else:
        playfair(-1, generateAlphabet(args.key))

    #playfair("Sample_ciphered.txt", generateAlphabet("prejudice"))