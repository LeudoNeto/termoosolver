import random
import time
import pyautogui as pyag
import pyperclip
from PIL import ImageGrab
import unicodedata

def checarcores(f):
    i = 0
    if xum == verde:
        letrascertas.append(f[0])
        while i < len(listadepossiveis):
            if f[0] != listadepossiveis[i][0]:
                listadepossiveis.remove(listadepossiveis[i])
            else:
                i = i + 1

    elif xum == amarelo:
        letrascertas.append(f[0])
        while i < len(listadepossiveis):
            if f[0] not in listadepossiveis[i]:
                listadepossiveis.remove(listadepossiveis[i])
            else:
                i = i + 1

    elif xum == preto and f[0] not in letrascertas:
        while i < len(listadepossiveis):
            if f[0] in listadepossiveis[i]:
                listadepossiveis.remove(listadepossiveis[i])
            else:
                i = i + 1

    i = 0
    if xdois == verde:
        letrascertas.append(f[1])
        while i < len(listadepossiveis):
            if f[1] != listadepossiveis[i][1]:
                listadepossiveis.remove(listadepossiveis[i])
            else:
                i = i + 1


    elif xdois == amarelo:
        letrascertas.append(f[1])
        while i < len(listadepossiveis):
            if f[1] not in listadepossiveis[i]:
                listadepossiveis.remove(listadepossiveis[i])
            else:
                i = i + 1

    elif xdois == preto and f[1] not in letrascertas:
        while i < len(listadepossiveis):
            if f[1] in listadepossiveis[i]:
                listadepossiveis.remove(listadepossiveis[i])
            else:
                i = i + 1

    i = 0
    if xtres == verde:
        letrascertas.append(f[2])
        while i < len(listadepossiveis):
            if f[2] != listadepossiveis[i][2]:
                listadepossiveis.remove(listadepossiveis[i])
            else:
                i = i + 1

    elif xtres == amarelo:
        letrascertas.append(f[2])
        while i < len(listadepossiveis):
            if f[2] not in listadepossiveis[i]:
                listadepossiveis.remove(listadepossiveis[i])
            else:
                i = i + 1

    elif xtres == preto and f[2] not in letrascertas:
        while i < len(listadepossiveis):
            if f[2] in listadepossiveis[i]:
                listadepossiveis.remove(listadepossiveis[i])
            else:
                i = i + 1

    i = 0
    if xquatro == verde:
        letrascertas.append(f[3])
        while i < len(listadepossiveis):
            if f[3] != listadepossiveis[i][3]:
                listadepossiveis.remove(listadepossiveis[i])
            else:
                i = i + 1

    elif xquatro == amarelo:
        letrascertas.append(f[3])
        while i < len(listadepossiveis):
            if f[3] not in listadepossiveis[i]:
                listadepossiveis.remove(listadepossiveis[i])
            else:
                i = i + 1

    elif xquatro == preto and f[3] not in letrascertas:
        while i < len(listadepossiveis):
            if f[3] in listadepossiveis[i]:
                listadepossiveis.remove(listadepossiveis[i])
            else:
                i = i + 1

    i = 0
    if xcinco == verde:
        letrascertas.append(f[4])
        while i < len(listadepossiveis):
            if f[4] != listadepossiveis[i][4]:
                listadepossiveis.remove(listadepossiveis[i])
            else:
                i = i + 1

    elif xcinco == amarelo:
        letrascertas.append(f[4])
        while i < len(listadepossiveis):
            if f[4] not in listadepossiveis[i]:
                listadepossiveis.remove(listadepossiveis[i])
            else:
                i = i + 1

    elif xcinco == preto and f[4] not in letrascertas:
        while i < len(listadepossiveis):
            if f[4] in listadepossiveis[i]:
                listadepossiveis.remove(listadepossiveis[i])
            else:
                i = i + 1

#pegar palavras disponíveis com 5 letras
with open('dicionarioptbr.txt', encoding = 'utf8') as f:
    dicionario = f.readlines()
    f.close()

palavrasdotermooo3 = []
dccopia = dicionario.copy()
for x in dccopia:
    if len(x) == 6:
        palavrasdotermooo3.append(x)
        if '-' in x:
            palavrasdotermooo3.remove(x)
        if '.' in x:
            palavrasdotermooo3.remove(x)
        if "'" in x:
            palavrasdotermooo3.remove(x)

#tirar o \n do final
palavrasdotermooo = []
for x in palavrasdotermooo3:
    y = x[0:5]
    palavrasdotermooo.append(y)

#tirar acentos e maiusculas
listadepossiveis2 = []

for x in palavrasdotermooo:
    palavrasdotermooo2 = unicodedata.normalize('NFD', x)
    palavrasdotermooo2 = palavrasdotermooo2.encode('ascii','ignore')
    palavrasdotermooo2 = palavrasdotermooo2.decode('utf-8')
    listadepossiveis2.append(palavrasdotermooo2)

listadepossiveis = []
for x in listadepossiveis2:
    y = x.lower()
    listadepossiveis.append(y)

#cores
preto = (49, 42, 44)
verde = (58, 163, 148)
amarelo = (211, 173, 105)
azul = (0, 154, 253)

#bug de letras repetidas
letrascertas = []

#bot
pyag.PAUSE = 0.1

time.sleep(1)

pyag.hotkey('alt','tab')
time.sleep(1)

palavra1 = random.choice(listadepossiveis)
print(palavra1)
listadepossiveis.remove(palavra1)
pyag.write(palavra1)
pyag.press('enter')

time.sleep(0.3)

avisoerro = ImageGrab.grab().load()[560, 160]

if avisoerro == azul:
    while True:
        pyag.press('backspace')
        pyag.press('backspace')
        pyag.press('backspace')
        pyag.press('backspace')
        pyag.press('backspace')
        palavra1 = random.choice(listadepossiveis)
        listadepossiveis.remove(palavra1)
        print(palavra1)
        pyag.write(palavra1)
        pyag.press('enter')
        time.sleep(0.3)
        avisoerro = ImageGrab.grab().load()[560, 160]
        if avisoerro != azul:
            break

time.sleep(2)

xum = ImageGrab.grab().load()[575,215]
xdois = ImageGrab.grab().load()[627,215]
xtres = ImageGrab.grab().load()[674,215]
xquatro = ImageGrab.grab().load()[731,215]
xcinco = ImageGrab.grab().load()[783,215]

print(len(listadepossiveis))

checarcores(palavra1)

print(len(listadepossiveis))
palavra2 = random.choice(listadepossiveis)
print(palavra2)
pyag.write(palavra2)
pyag.press('enter')

time.sleep(0.3)

avisoerro = ImageGrab.grab().load()[560, 160]

if avisoerro == azul:
    print('reconheceu')
    while True:
        pyag.press('backspace')
        pyag.press('backspace')
        pyag.press('backspace')
        pyag.press('backspace')
        pyag.press('backspace')
        palavra2 = random.choice(listadepossiveis)
        listadepossiveis.remove(palavra2)
        print(palavra2)
        pyag.write(palavra2)
        pyag.press('enter')
        time.sleep(0.3)
        avisoerro = ImageGrab.grab().load()[560, 160]
        if avisoerro != azul:
            break

time.sleep(2)

xum = ImageGrab.grab().load()[575,270]
xdois = ImageGrab.grab().load()[627,270]
xtres = ImageGrab.grab().load()[674,270]
xquatro = ImageGrab.grab().load()[731,270]
xcinco = ImageGrab.grab().load()[783,270]

checarcores(palavra2)

print(len(listadepossiveis))
palavra3 = random.choice(listadepossiveis)
print(palavra3)
pyag.write(palavra3)
pyag.press('enter')
listadepossiveis.remove(palavra3)

time.sleep(0.3)

avisoerro = ImageGrab.grab().load()[560, 160]

if avisoerro == azul:
    print('reconheceu')
    while True:
        pyag.press('backspace')
        pyag.press('backspace')
        pyag.press('backspace')
        pyag.press('backspace')
        pyag.press('backspace')
        palavra3 = random.choice(listadepossiveis)
        listadepossiveis.remove(palavra3)
        print(palavra3)
        pyag.write(palavra3)
        pyag.press('enter')
        time.sleep(0.3)
        avisoerro = ImageGrab.grab().load()[560, 160]
        if avisoerro != azul:
            break

time.sleep(2)

xum = ImageGrab.grab().load()[575,325]
xdois = ImageGrab.grab().load()[627,325]
xtres = ImageGrab.grab().load()[674,325]
xquatro = ImageGrab.grab().load()[731,325]
xcinco = ImageGrab.grab().load()[783,325]

checarcores(palavra3)

print(len(listadepossiveis))
palavra4 = random.choice(listadepossiveis)
print(palavra4)
pyag.write(palavra4)
pyag.press('enter')
listadepossiveis.remove(palavra4)

time.sleep(0.3)

avisoerro = ImageGrab.grab().load()[560, 160]

if avisoerro == azul:
    print('reconheceu')
    while True:
        pyag.press('backspace')
        pyag.press('backspace')
        pyag.press('backspace')
        pyag.press('backspace')
        pyag.press('backspace')
        palavra4 = random.choice(listadepossiveis)
        listadepossiveis.remove(palavra4)
        print(palavra4)
        pyag.write(palavra4)
        pyag.press('enter')
        time.sleep(0.3)
        avisoerro = ImageGrab.grab().load()[560, 160]
        if avisoerro != azul:
            break

time.sleep(2)

xum = ImageGrab.grab().load()[575,382]
xdois = ImageGrab.grab().load()[627,382]
xtres = ImageGrab.grab().load()[674,382]
xquatro = ImageGrab.grab().load()[731,382]
xcinco = ImageGrab.grab().load()[783,382]

checarcores(palavra4)

print(len(listadepossiveis))
palavra5 = random.choice(listadepossiveis)
print(palavra5)
pyag.write(palavra5)
pyag.press('enter')
listadepossiveis.remove(palavra5)

time.sleep(0.3)

avisoerro = ImageGrab.grab().load()[560, 160]

if avisoerro == azul:
    print('reconheceu')
    while True:
        pyag.press('backspace')
        pyag.press('backspace')
        pyag.press('backspace')
        pyag.press('backspace')
        pyag.press('backspace')
        palavra5 = random.choice(listadepossiveis)
        listadepossiveis.remove(palavra5)
        print(palavra5)
        pyag.write(palavra5)
        pyag.press('enter')
        time.sleep(0.3)
        avisoerro = ImageGrab.grab().load()[560, 160]
        if avisoerro != azul:
            break

time.sleep(2)

doisxum = ImageGrab.grab().load()[575,438]
doisxdois = ImageGrab.grab().load()[627,438]
doisxtres = ImageGrab.grab().load()[674,438]
doisxquatro = ImageGrab.grab().load()[731,438]
doisxcinco = ImageGrab.grab().load()[783,438]

checarcores(palavra5)

print(len(listadepossiveis))
palavra6 = random.choice(listadepossiveis)
print(palavra6)
pyag.write(palavra6)
pyag.press('enter')

time.sleep(0.3)

avisoerro = ImageGrab.grab().load()[560, 160]

if avisoerro == azul:
    print('reconheceu')
    while True:
        pyag.press('backspace')
        pyag.press('backspace')
        pyag.press('backspace')
        pyag.press('backspace')
        pyag.press('backspace')
        palavra6 = random.choice(listadepossiveis)
        listadepossiveis.remove(palavra6)
        print(palavra6)
        pyag.write(palavra6)
        pyag.press('enter')
        time.sleep(0.3)
        avisoerro = ImageGrab.grab().load()[560, 160]
        if avisoerro != azul:
            break
