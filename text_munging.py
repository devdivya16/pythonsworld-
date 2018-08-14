import random

import re

def replace(t):
    inner_word = list(t.group(2))
    random.shuffle(inner_word)
    return t.group(1) + "".join(inner_word) + t.group(3)
text = "Hello, You should reach the finish line."
print( re.sub(r"(\w)(\w+)(\w)", replace, text))
print (re.sub(r"(\w)(\w+)(\w)", replace, text))