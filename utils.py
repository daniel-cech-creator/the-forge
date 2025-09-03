# POLISHING UTILITY FUNCTIONS
import os
from time import sleep


def clear_term():
    if os.name == 'nt': #Windows
        os.system('cls')
    else:
        os.system('clear')

def black(text):
    return (f"\033[30m{text}\033[0m")
def red(text):
    return (f"\033[31m{text}\033[0m")
def green(text):
    return (f"\033[32m{text}\033[0m")
def yellow(text):
    return (f"\033[33m{text}\033[0m")
def blue(text):
    return (f"\033[34m{text}\033[0m")
def purple(text):
    return (f"\033[35m{text}\033[0m")
def azure(text):
    return (f"\033[36m{text}\033[0m")
def white(text):
    return (f"\033[37m{text}\033[0m")
def rainbow(text):
    colors = [
        "\033[31m",  # Red
        "\033[33m",  # Yellow
        "\033[32m",  # Green
        "\033[36m",  # Azure
        "\033[34m",  # Blue
        "\033[35m",  # Purple
    ]
    reset = "\033[0m"

    result = ""
    for i, char in enumerate(text):
        color = colors[i % len(colors)]
        result += f"{color}{char}"
    result += reset
    return result