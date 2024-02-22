# registrere tastetrykk og lagre med tekstfil

import time
import keyboard

path = 'C:\\Python\\tekstfiler\\tastetrykk.txt'

tastetrykk = 0

def les_fil():
    global tastetrykk
    with open(path, 'r') as fil:
        tastetrykk_lest = fil.read()
    tastetrykk = int(tastetrykk_lest)
    fil.close()
    return tastetrykk


def tastetrykk_reg(e):
    global tastetrykk
    tastetrykk += 1
    
    skriv_antall()
    

def lagre():
    global tastetrykk
    with open(path, 'w') as fil:
        fil.write(str(tastetrykk))
        fil.close()
        
    nå=time.ctime()
    print (f'lagret {nå}')
    print (f'tastetrykk siden 22.02.2024: {tastetrykk}')
    
        
def skriv_antall():
    global tastetrykk
    print (tastetrykk)


les_fil()
    
keyboard.on_press(tastetrykk_reg)

while True:
    time.sleep(60)
    lagre()

