# registering keystrokes, saving the count to a textfile txt

import time
import keyboard

path = 'C:\\Python\\keystrokes.txt'

keystrokes = 0

def read_file():
    global keystrokes
    with open(path, 'r') as file:
        keystrokes_lest = file.read()
    keystrokes = int(keystrokes_read)
    file.close()
    return keystrokes


def keystrokes_reg(e):
    global keystrokes
    keystrokes += 1
    
    write_number()
    

def save():
    global keystrokes
    with open(path, 'w') as file:
        file.write(str(keystrokes))
        file.close()
        
    now=time.ctime()
    print (f'saved {now}')
    print (f'number of keystrokes: {keystrokes}')
    
        
def write_number():
    global keystrokes
    print (keystrokes)


read_file()
    
keyboard.on_press(keystrokes_reg)

while True:
    time.sleep(60)
    save()

