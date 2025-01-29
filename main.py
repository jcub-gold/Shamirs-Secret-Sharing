import os
from dotenv import load_dotenv
import random
import json

load_dotenv()

p = 2 ** int(os.getenv("MARSENNE_EXPONENT")) - 1
n = 8054 # population of Stanford undergraduates
k = 2 # number of people required to decode the key

def choose_indistinct_large(k, p):
    chosen = []
    while len(chosen) < k:
        chosen.append(random.randint(1, p - 1))
    return chosen

x = range(1, n + 1)
a = choose_indistinct_large(k, p)

y = []
for _x in x:
    y.append(a[0] + a[1] * _x)
K = a[0]

data = {"K": K, "y": y}

with open('secrect_info.json', "w") as json_file:
    json.dump(data, json_file, indent=4)

print('done')