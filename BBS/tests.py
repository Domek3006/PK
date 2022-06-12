from os import stat


def singleBits(key):
    count = 0
    for bit in key:
        if (bit == '1'):
            count += 1
    if (count > 9725 and count < 10275):
        print('Single bit test: passed')
    else:
        print('Single bit test: failed (bit count = {})'.format(count))
        
def series(key, curr):
    seriesLen = { '1':0, '2':0, '3':0, '4':0, '5':0, '6':0 }
    count = 0
    for bit in key:
        if (bit == curr):
            count += 1
        else:
            if (count == 0):
                continue
            if (count > 6):
                count = 6
            seriesLen[str(count)] += 1
            count = 0
    status = True
    if (seriesLen['1'] < 2315 or seriesLen['1'] > 2685):
        status = False
        print('Fail: Series 1 = {}'.format(seriesLen['1']))
    if (seriesLen['2'] < 1114 or seriesLen['2'] > 1386):
        status = False
        print('Fail: Series 2 = {}'.format(seriesLen['2']))
    if (seriesLen['3'] < 527 or seriesLen['3'] > 723):
        status = False
        print('Fail: Series 3 = {}'.format(seriesLen['3']))
    if (seriesLen['4'] < 240 or seriesLen['4'] > 384):
        status = False
        print('Fail: Series 4 = {}'.format(seriesLen['4']))
    if (seriesLen['5'] < 103 or seriesLen['5'] > 209):
        status = False
        print('Fail: Series 5 = {}'.format(seriesLen['5']))
    if (seriesLen['6'] < 103 or seriesLen['6'] > 209):
        status = False
        print('Fail: Series 6+ = {}'.format(seriesLen['6']))
    
    if (status):
        print('Series test for {}: passed'.format(curr))
    else:
        print('Series test for {}: failed'.format(curr))
    
def seriesLong(key):
    curr = key[0]
    count = 0
    status = True
    for bit in key:
        if (bit == curr):
            count += 1
        else:
            if (count > 25):
                status = False
                break
            curr = bit
            count = 1
    if (count > 25):
            status = False
    if (status):
        print('Long series test: passed')
    else:
        print('Long series test: failed')
        
def poker(key):
    sums = [0 for _ in range(16)]
    for i in range(0, len(key), 4):
        sums[int(key[i:i+4], 2)] += 1
    x = 0
    for count in sums:
        x += count**2
    x *= 16./5000.
    x -= 5000
    if (x > 2.16 and x < 46.17):
        print('Poker test: passed')
    else:
        print('Poker test: failed (x = {})'.format(x))
            
    
if (__name__ == '__main__'):
    with open('key.txt', encoding='utf-8') as key_file:
        key = key_file.read()
        singleBits(key)
        series(key, '0')
        series(key, '1')
        seriesLong(key)
        poker(key)