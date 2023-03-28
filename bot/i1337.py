import random

numbers = '1337'
base_text = 'хакерская минута'
hacker_emoji = '😎💻🔓🖥💰🎉'

leet = {'х':'x', 'а':'4', 'к':'k', 'е':'3', 'р':'p', 'с': 'c', 'я':'я', 'м':'m', 'и':'u', 'н':'n', 'у':'y', 'т':'7', ' ':' ', 'a':'4', 't':'7', 'g':'9', 'i':'1', 'e':'3', 's':'5', 'o':'0'}

def rand_case(text):
    for i in range(len(text)):
        text = text[:i] + random.choice([text[i].lower(), text[i].upper()]) + text[i+1:]
    return text

def to_leet(text):
    for i in range(len(text)):
        if text[i].lower() in leet:
            text = text[:i] + leet[text[i].lower()] + text[i+1:]
    return text

def rand_emoji(text):
    left = random.choice(list(hacker_emoji) + [''])
    right = random.choice(list(hacker_emoji) + [''])
    if left:
        left += ' '
    if right:
        right = ' ' + right
    return f"{left}{text}{right}"

def get_text():
    return rand_emoji(rand_case(to_leet(base_text)))
