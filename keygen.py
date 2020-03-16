#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import operator

magicNumber=0x1acb0aad
secondMagicNumber=0x4c7

def validateKey(number):
    ecx = number
    imuled = operator.imul(ecx, magicNumber)

    edx = int(hex(imuled)[:-8], 16)

    edx >>= 0x7
    eax = ecx

    eax >>= 0x1f
    edx -= eax
    eax = edx

    eax = operator.imul(eax, secondMagicNumber)
    ecx -= eax
    eax = ecx

    return eax

def main():
    valid = False

    while not valid:
        randomNumber = random.randrange(11111, 99999)
        keyNumber = validateKey(randomNumber)

        if(keyNumber == 0):
            valid = True
            print(randomNumber)

main()
