# POLISHING UTILITY FUNCTIONS
import os
from time import sleep

def clear_term():
    #Windows
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def black(a):
    return (f"\033[30m{a}\033[0m")
def red(a):
    return (f"\033[31m{a}\033[0m")
def green(a):
    return (f"\033[32m{a}\033[0m")
def yellow(a):
    return (f"\033[33m{a}\033[0m")
def blue(a):
    return (f"\033[34m{a}\033[0m")
def purple(a):
    return (f"\033[35m{a}\033[0m")
def azure(a):
    return (f"\033[36m{a}\033[0m")
def white(a):
    return (f"\033[37m{a}\033[0m")

def write_out(chars, timeBetweenLetters=0.01):
    for ch in chars:
        print(ch, end='', flush=True)
        sleep(timeBetweenLetters)
    print()