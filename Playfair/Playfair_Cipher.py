import argparse as argp
import string
from os.path import exists

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
        print('Enter plaintext:')
        text = input().strip()
    else:
        file = open(filename, encoding="utf-8")
        text = file.read()
        file.close()
    text = text.upper()
    '''regex = re.compile('[^A-Z]')
    text = regex.sub('', text)'''
    #if (len(text) % 2 == 1):
     #   text += 'X'
    #text = list(map(''.join, zip(*[iter(text)]*2)))
    text = text.replace('J', 'I')
    cipher = ''
    j = 0
    while (j < len(text)):
        tmp = ''
        if not (text[j].isalpha()):
            cipher += text[j]
            j += 1
            if (j == len(text)):
                break
            continue
        lett1 = text[j]
        j += 1
        if (j < len(text)):    
            while not (text[j].isalpha()):
                tmp += text[j]
                j += 1
                if (j == len(text)):
                    break
        if (j == len(text)):
            if(lett1 == 'X'):
                lett2 = 'Q'
            else:
                lett2 = 'X'
        else:
            lett2 = text[j]
        if (lett1 == lett2):
            if(lett1 == 'X'):
                lett2 = 'Q'
            else:
                lett2 = 'X'
        j += 1
        for i in range(5):
            if (lett1 in alphabet[i]):
                i0 = i
                j0 = alphabet[i].index(lett1)
            if (lett2 in alphabet[i]):
                i1 = i
                j1 = alphabet[i].index(lett2)
        if (i0 == i1):
            cipher += alphabet[i0][(j0+1)%5] + tmp + alphabet[i1][(j1+1)%5]
        elif (j0 == j1):
            cipher += alphabet[(i0+1)%5][j0] + tmp + alphabet[(i1+1)%5][j1]
        else:
            cipher += alphabet[i0][j1] + tmp + alphabet[i1][j0]
    if ( filename == -1):
        print(cipher)
    else:    
        filename = filename.split('.')
        file = open(filename[0]+'_ciphered.'+filename[1], 'w', encoding='utf-8')
        file.write(cipher)
        file.close()
        print('File ciphered')
    return

if __name__ == '__main__':
    parser = argp.ArgumentParser(description='Cipher text using playfair cipher')
    parser.add_argument('key', metavar='key', type=str, help='key word to be used')
    parser.add_argument('-f', '--file', type=str, help='[optional] file containing text to be ciphered')

    args = parser.parse_args()
    
    if (args.file):    
        if not(exists(args.file)):
            print('Plaintext file does not exist')
        else:
            playfair(args.file, generateAlphabet(args.key))
    else:
        playfair(-1, generateAlphabet(args.key))
        
    #playfair('in', generateAlphabet('nonsense'))
