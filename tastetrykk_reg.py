# registering keystrokes, saving the count to a textfile txt

import time
import keyboard

path = 'C:\\Python\\keystrokes.txt'

keystrokes = 0

def les_fil():
    global keystrokes
    with open(path, 'r') as fil:
        tastetrykk_lest = fil.read()
    keystrokes = int(keystrokes_read)
    fil.close()
    return keystrokes


def keystrokes_reg(e):
    global keystrokes
    keystrokes += 1
    
    skriv_antall()
    

def lagre():
    global keystrokes
    with open(path, 'w') as fil:
        fil.write(str(keystrokes))
        fil.close()
        
    nå=time.ctime()
    print (f'lagret {nå}')
    print (f'number of keystrokes: {keystrokes}')
    
        
def skriv_antall():
    global keystrokes
    print (keystrokes)


les_fil()
    
keyboard.on_press(keystrokes_reg)

while True:
    time.sleep(60)
    lagre()

