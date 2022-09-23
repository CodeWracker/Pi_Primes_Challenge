
import math

import requests

from requests.exceptions import Timeout


def getPi(start, length):
    req = {}
    try:
        req = requests.get(
            f'https://api.pi.delivery/v1/pi?start={start}&numberOfDigits={length}')
    except:
        print("Erro, tentando de novo")
        req = getPi(start, length)
        return req

    return ((req.json()['content']))


def checkPalindrome(num):
    for i in range(int(len(num)/2)):
        #print(len(num), i)
        if (num[i] != num[len(num) - (i+1)]):
            return False

    return True


def isPrime(num):
    if (num == 1):
        return False
    if (num == 2):
        return True
    for i in range(2, int(math.sqrt(num))+1):
        if (num % i == 0):
            return False
    return True

# travou em um momento então coloquei um parametro para iniciar de 55269060


def generatePiNumbers(verification_length, start):
    #start = 0
    length = 1000
    i = 0
    break_loop = False
    while (1):
        pi = getPi(start, length)
        print(f'Analise de pi {start} ate {start+length}')
        # print(pi)
        for j in range(0, len(pi) - verification_length + 1):
            ev_pi = pi[j:j+verification_length]
            #print(f'{start+j}: ev_pi: {ev_pi}')
            if (checkPalindrome(str(ev_pi))):

                print(f'Palindromo encontrado em: ', start + j)
                if (isPrime(int(ev_pi))):
                    print(f'Palindromo {ev_pi} e primo')
                    break_loop = True
                    break

        if (break_loop):
            break

        start += length - (verification_length-1)
        i += 1
    return


if __name__ == "__main__":
    generatePiNumbers(21, 55269060)
