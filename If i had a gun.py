import sys
import time
from time import sleep

def print_lirik(): 
    baris = [
        ("Let me fly you to the moon", 0.11),
        ("My eyes have always followed you around the room", 0.11),
        ("'Cause you're the only", 0.08),
        ("God that i will ever need", 0.11),
        ("I'm holding on and waiting for the moment to find me", 0.10),
    ]

    jeda = [1.1, 1.1, 0.5, 0.6, 0.5] 

    for i, (line, char_jeda) in enumerate(baris): 
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_jeda)  
        print('')
        sleep(jeda[i]) 

print_lirik() 