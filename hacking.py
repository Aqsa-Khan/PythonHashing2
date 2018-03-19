from StolenInfo import loginDict
from hashlib import *
import string
loginDict = {'Gerald': '4d416525fcdbdd87be5b3cda134e806dfa6613c682fb8b749ea552adeffab251'}
hash=loginDict["Gerald"]
rainbow = {}
letters = list(string.ascii_uppercase)

for first in letters:
    for second in letters:
        for third in letters:
            curPass=first+second+third
            hashPass=sha256(curPass.encode('utf-8')).hexdigest()
            rainbow[hashPass]=curPass


print(rainbow[hash])
