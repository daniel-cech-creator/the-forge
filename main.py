import time, os, random

import weapons

def clear_terminal():
    #Windows
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# ==============
# START PROGRAM
# =============
clear_terminal()

#Title
print(r"""
 _____                    
|  ___|__  _ __ __ _  ___ 
| |_ / _ \| '__/ _` |/ _ \
|  _| (_) | | | (_| |  __/
|_|  \___/|_|  \__, |\___|
               |___/      """)
input()
clear_terminal()