from hashlib import sha3_256
from string import ascii_letters
from tkinter import filedialog
from turtle import width
from Cryptodome.Hash import MD5, SHA1, SHA224, SHA256, SHA384, SHA512, SHA3_224, SHA3_256, SHA3_384, SHA3_512, TupleHash128, TupleHash256
from time import time
from tkinter import *

def select_file():
    ftype = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )
    filename = filedialog.askopenfilename(filetypes=ftype)
    file = open(filename, encoding='utf-8')
    if(text.get('1.0', 'end-1c')):
        text.delete('1.0', 'end-1c')
    text.insert('1.0', file.read())

def select_hash():
    match var.get():
        case '0':
            dropdown_opt = ['MD-5']
        case '1':
            dropdown_opt = ['SHA-1']
        case '2':
            dropdown_opt = ['SHA-224', 'SHA-256', 'SHA-384', 'SHA-512']
        case '3':
            dropdown_opt = ['SHA3-224', 'SHA3-256', 'SHA3-384', 'SHA3-512', 'TupleHash128', 'TupleHash256']
    clicked.set(dropdown_opt[0])
    #drop.grid_remove()
    drop = OptionMenu(m, clicked, *dropdown_opt)
    drop.grid(row=4, column=1, padx=5)

def start_hash():
    hashtype = clicked.get()
    match hashtype:
        case 'MD-5':
            hash = MD5.new()
            SAChash = MD5.new()
        case 'SHA-1':
            hash = SHA1.new()
            SAChash = SHA1.new()
        case 'SHA-224':
            hash = SHA224.new()
            SAChash = SHA224.new()
        case 'SHA-256':
            hash = SHA256.new()
            SAChash = SHA256.new()
        case 'SHA-384':
            hash = SHA384.new()
            SAChash = SHA384.new()
        case 'SHA-512':
            hash = SHA512.new()
            SAChash = SHA512.new()
        case 'SHA3-224':
            hash = SHA3_224.new()
            SAChash = SHA3_224.new()
        case 'SHA3-256':
            hash = SHA3_256.new()
            SAChash = SHA3_256.new()
        case 'SHA3-384':
            hash = SHA3_384.new()
            SAChash = SHA3_384.new()
        case 'SHA3-512':
            hash = SHA3_512.new()
            SAChash = SHA3_512.new()
        case 'TupleHash128':
            hash = TupleHash128.new()
            SAChash = TupleHash128.new()
        case 'TupleHash256':
            hash = TupleHash256.new()
            SAChash = TupleHash256.new()
    if(hash_text.get('1.0', 'end-1c')):
        hash_text.delete('1.0', 'end-1c')
    new_str = bytearray(text.get('1.0', 'end-1c'), 'utf-8')
    new_str[-1] = new_str[-1] ^ 1
    new_str = bytes(new_str).decode('utf-8')
    if (hashtype == 'TupleHash128' or hashtype == 'TupleHash256'):
        toHash = text.get('1.0', 'end-1c').split()
        toHashSAC = new_str.split()
        tstart = time()
        for word in toHash[:-1]:
            hash.update(bytes(word, 'utf-8'))
            hash.update(b' ')
        tfinal = time() - tstart
        for word in toHashSAC[:-1]:
            SAChash.update(bytes(word, 'utf-8'))
            SAChash.update(b' ')
        hash.update(bytes(toHash[-1], 'utf-8'))
    else:
        tstart = time()
        hash.update(bytes(text.get('1.0', 'end-1c'), 'utf-8'))
        tfinal = time() - tstart
        SAChash.update(bytes(new_str, 'utf-8'))
    hash_text.insert('1.0', hash.hexdigest())
    if(time_text.get('1.0', 'end-1c')):
        time_text.delete('1.0', 'end-1c')
    time_text.insert('1.0', str(tfinal) + ' seconds')
    cnt = 0
    n = int(hash.hexdigest(), 16) ^ int(SAChash.hexdigest(), 16)
    while n:
        n &= n - 1
        cnt += 1
    #print(cnt)
    #print(len(hash.hexdigest()), len(SAChash.hexdigest()))
    #print(len(hash.hexdigest())*4)
    print(new_str, SAChash.hexdigest())
    print(hashtype, len(hash.hexdigest())*4, cnt)
    print('SAC: ', len(hash.hexdigest())*2 == cnt)
    print('Avalanche: ', len(hash.hexdigest())*2 < cnt)
    #find_collision()
    print('----------------------')
    
    
def find_collision():
    text = b'1'
    hash = MD5.new()
    hash.update(text)
    dig = hash.hexdigest()[:3]
    i = 2
    while(True):
        hash = MD5.new()
        hash.update(bytes(str(i), 'utf-8'))
        if (dig == hash.hexdigest()[:3]):
            print(f'1 and {i} collide')
            break
        i += 1

if (__name__ == '__main__'):
    m = Tk()
    m.title('Hashing')
    m.resizable(False, False)
    #m.geometry('300x150')
    open_button = Button(
        m,
        text='Open File',
        command=select_file
    )
    open_button.grid(row=0, columnspan=2, pady=5)
    text = Text(m, height=12)
    text.grid(row=1, column=0, columnspan=2, padx=5)
    hashing = {
        'MD-5' : '0',
        'SHA-1' : '1',
        'SHA-2' : '2',
        'SHA-3' : '3'
    }
    var = StringVar(m, '0')
    i = 3
    for (t, v) in hashing.items():
        Radiobutton(m, text=t, variable=var, value=v, command=select_hash).grid(row=i, column=0)
        i += 1
    hash_button = Button(m, text='Hash', command=start_hash)
    hash_button.grid(row=7, columnspan=2, pady=5)
    clicked = StringVar()
    hash_text = Text(m, height=12)
    hash_text.grid(row=8, column=0, columnspan=2, padx=5)
    time_lab = Label(m, text='Time: ')
    time_lab.grid(row=9, column=0, pady=5)
    time_text = Text(m, height=1, width=70)
    time_text.grid(row=9, column=1, pady=5)
    clicked.set('MD-5')
    drop = OptionMenu(m, clicked, 'MD-5')
    drop.grid(row=4, column=1, padx=5)
    m.mainloop()
     