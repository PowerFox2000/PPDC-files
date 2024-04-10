import os, time
print('Project is owned by Matheo Genre')
def decode(number):
    decoder = {
    #         j     p        y 
        '··--': ' ', '·-': 'a', '-···': 'b', '-·-·': 'c', '-··': 'd', '·': 'e', '··-·': 'f', '--·': 'g', '····': 'h', '··': 'i', '·---': 'j', '-·-': 'k', '·-··': 'l', '--': 'm', '-·': 'n', 
        '---': 'o', '·--·': 'p', '--·-': 'q', '·-·': 'r', '···': 's', '-': 't', '··-': 'u', '···-': 'v', '·--': 'w', '-··-': 'x', '-·--': 'y', '--··': 'z',
        '·----': '1', '··---': '2', '···--': '3', '····-': '4', '·····': '5', '-····': '6',  '--···': '7', '---··': '8', '----·': '9', '-----': '0', '·-·-·-': '.','--··--': ',', 
    }
    return decoder.get(number, '')
def code(number):
    coder = {
        ' ': '··--', 'a': '·-', 'b': '-···', 'c': '-·-·', 'd': '-··', 'e': '·', 'f': '··-·', 'g': '--·', 'h': '····', 'i': '··', 'j': '·---', 'k': '-·-', 'l': '·-··',
        'm': '--', 'n': '-·', 'o': '---', 'p': '·--·', 'q': '--·-', 'r': '·-·', 's': '···', 't': '-', 'u': '··-', 'v': '···-', 'w': '·--', 'x': '-··-',
        'y': '-·--', 'z': '--··', '1': '·----', '2': '··---', '3': '···--', '4': '·····', '5': '-····', '6': '--···',
        '7': '---··', '8': '----·', '9': '-----', '0': '·-·-·-','.': '·-·-·-', ',': '--··--',
    }
    return coder.get(number, '')
cord = input('Hi, do you want to code(c) or decode(d) ?\n')
if cord == 'd':
    decoder = 1
    os.system('cls')
    decoder = input('Hi, what do you want to decode ?\n')
    print('Here is your message :')
    v = ''
    if decoder[-1] ==";":
        decoder = decoder[0:-1]
    msg = decoder.split(' ')
    for i in msg :
        v = v + (decode(str(i))) 
    print(v)
elif cord == 'c':
    coder = 1
    os.system('cls')
    coder = input('Hi, what do you want to code ?\n')
    print('Here is your code')
    v = ''
    for i in coder :
        v = v + (code(i)) + ' '
    print(v)
else: 
    print('Unknow command')