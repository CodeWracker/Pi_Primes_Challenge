
import chunk
import math
from queue import PriorityQueue
from turtle import position
import requests
from requests.exceptions import Timeout
import pandas as pd
#import tqdm


def download_file(url, save_path):
    file_name = url.split("=")[-1]
    print(f'baixando arquivo {file_name}')
    local_filename = f'{save_path}/{file_name}'
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        # with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=8192):
            yield (str(chunk))
            # If you have chunk encoded response uncomment if
            # and set chunk_size parameter to None.
            # if chunk:
            # f.write(chunk)
    return local_filename


def getPi(start):
    # vai baixar um arquivo com 43gb e ler por partes
    # cada arquivo tem 100 bilhoes de digitos
    start = str(int((start / (100000000000+1))) + 1)
    if (len(start) < 2):
        start = '0' + start

    url = f'https://ia801605.us.archive.org/view_archive.php?archive=/17/items/pi_dec_1t/pi_dec_1t_{start}.zip&file=pi_dec_1t_{start}.txt'
    save_path = "D:\Projetos\Pessoal\DesafioPI"
    for chunk in download_file(url, save_path):
        yield (chunk)
    return


def checkPalindrome(num):
    for i in range(int(len(num)/2)):
        # print(len(num), i)
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


def findPiNumbers(verification_length, start, chunk_start):
    # segundo parametro é o inicio da analise, caso tenha sido interrompida em algum momento e queira continuar
    # o terceito é o chunk que parou, None se não quiser dizer p ele começar de um ponto especifico

    # start = 0
    '''length = 1000
    i = 0
    break_loop = False
    while (1):
        pi = getPi(start, length)
        print(f'Analise de pi {start} ate {start+length}')
        # print(pi)
        for j in range(0, len(pi) - verification_length + 1):
            ev_pi = pi[j:j+verification_length]
            # print(f'{start+j}: ev_pi: {ev_pi}')
            if (checkPalindrome(str(ev_pi))):

                print(f'Palindromo encontrado em: ', start + j)
                if (isPrime(int(ev_pi))):
                    print(f'Palindromo {ev_pi} e primo')
                    break_loop = True
                    break

        if (break_loop):
            break

        start += length - (verification_length-1)
        i += 1'''
    start = start - verification_length
    if (start < 0):
        start = 0
    first_chunk = True
    try:
        while (1):
            prev_chunk = ""
            chunk_count = 0
            if (first_chunk):
                print(f'Indo até o chunck {chunk_start}')
                while (chunk_count < chunk_start - 1):
                    getPi(start)
                    chunk_count += 1

            first_chunk = False
            position = start
            print(f'Analise de pi {start} ate {start+100000000000}')
            for chunk in getPi(start):
                chunk = chunk.replace('.', '').replace(
                    '\n', '').replace('b', '').replace("'", '')

                if (chunk_count == 0):
                    print(chunk[0:20])

                chunk = prev_chunk[len(prev_chunk) -
                                   ((verification_length-1)):-1] + chunk
                position = position + len(prev_chunk)
                for j in range(0, len(chunk) - verification_length + 1):
                    ev_pi = chunk[j:j+(verification_length)]
                    # print(f'{start+j}: ev_pi: {ev_pi}')
                    if (checkPalindrome(str(ev_pi))):
                        print(
                            f'Palindromo {ev_pi} encontrado - Analise de pi em {position+j} | tamanho do chunk {chunk_count}: {len(chunk)}')
                        if (isPrime(int(ev_pi))):
                            print(
                                f'Palindromo {ev_pi} e primo na posicao {position+j}')
                            return
                chunk_count += 1
                prev_chunk = chunk
            print(f'nada encontrado entre {start} e {position}')
            start += 100000000000
    except KeyboardInterrupt:
        print(
            f'Analise de pi {start} ate {position} | tamanho do chunk {chunk_count}: {len(chunk)} interrompida pelo usuário')

    return


# 43 372 464
if __name__ == "__main__":

    findPiNumbers(21, 100907050064, 56893)
