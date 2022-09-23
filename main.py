
import math
import requests
from requests.exceptions import Timeout
from gdrive import Create_Service
import pandas as pd


def download_from_google_drive(id, destination):

    return


def list_googledrive_files():
    CLIENT_SECRET_FILE = 'client_secret.json'
    API_NAME = 'drive'
    API_VERSION = 'v3'
    SCOPES = ['https://www.googleapis.com/auth/drive']

    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
    folder_id = "1L_HnNULhHSuDabD036H94pGdD-XbKhLy"
    query = f"parents = '{folder_id}'"

    response = service.files().list(q=query).execute()
    # print(response)
    files = response.get('files')
    nextPageToken = response.get('nextPageToken')
    # print(nextPageToken)

    while nextPageToken:
        response = service.files().list(q=query, pageToken=nextPageToken).execute()
        # print(response.get('files'))
        files.extend(response.get('files'))
        nextPageToken = response.get('nextPageToken')
        # print(nextPageToken)

    df = pd.DataFrame(files)
    df = df[df["name"].str.contains("Pi")]
    # .sort_values(by=['name'], ascending=True)
    return df
    # vai baixar um arquivo com 78gb e ler por partes
    # cada arquivo tem 200 bilhoes de digitos


def getPi(start):
    start = start % 200000000000
    files_df = list_googledrive_files()
    print(files_df)
    arq_name = f'arquivo Pi - Dec - Chudnovsky - {start}.ycd'
    print(f'baixando o {arq_name}')
    return


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


def findPiNumbers(verification_length, start):
    #start = 0
    '''length = 1000
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
        i += 1'''
    getPi(start)
    return


if __name__ == "__main__":
    findPiNumbers(21, 0)
