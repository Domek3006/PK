from base64 import b64decode

def decrypt(filename, prvk):
    with open(filename) as file, open('decrypted.txt', 'w', encoding='utf-8') as ciph:
        enc_text = file.read().encode('ascii')
        enc_text = b64decode(enc_text)
        enc_text = enc_text.decode('ascii')
        number_text = enc_text.split(' ')
        print('Decrypting...')
        dec_text = ''
        for num in number_text:
            next = str(pow(int(num), prvk[0], prvk[1]))
            while (len(next) < 3):
                next = '0' + next
            dec_text += next
        text = ''
        i = 0
        while (i < len(dec_text)-1):
            if (dec_text[i] == '1'):
                text += chr(int(dec_text[i:i+3]))
                i += 3
            else:
                text += chr(int(dec_text[i:i+2]))
                i += 2
        ciph.write(text)
        print('Decryption complete')