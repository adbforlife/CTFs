#!/usr/bin/env python3
from binascii import hexlify
from binascii import unhexlify
from operator import attrgetter

ME_FLAGE = '<censored>'

#SoUp = input
#soUP = hex
#sOUp = print
#sOuP = ord
SOuP = open

def palindrome(sOUP):
    soup = 0
    while sOUP != 0:
        soup = (soup * 10) + (sOUP % 10)
        sOUP //= 10
    return soup

def SOup(sOUP):
    soup = 0
    for soUp in sOUP:
        soup *= 10
        soup += ord(soUp) - ord('0')
    return soup


possibles = [u'\u096D',u'\u00B3',u'\u2070',u'\u2081',u'\u2094',u'\u2075',u'\u2076',u'\u2077',u'\u2078',u'\u2079']
for i in possibles:
    print(i.isdigit())
    print(ord(i) - ord('0'))

print(u'\u096D')
print(SOup(u'\u096D552391'))
#print(s.isdigit())
#print(hex(2365552391))
#print(palindrome(2365552391))

#print(palindrome(int(hexlify('s0up'), 16)))

def SOUP(number):
    #Soup = input()[:7]
    #print(Soup)
    #if not Soup.isdigit():
    #    print("that's not a number lol")
    #    return
    Soup = number
    soup = palindrome(Soup)
    SouP = hex(soup)[2:].zfill(8)[-8:]
    #if unhexlify(SouP) == 's0up'.encode():
    #    print("oh yay it's a flag!", ME_FLAGE)
    #else:
    #    print('oh noes rip u')

if __name__ == '__main__':
    SOUP(2365552391)
