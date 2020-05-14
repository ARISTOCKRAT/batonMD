import numpy as np
import json

with open("out_data/fuzzy_logic.json") as file:
    t = json.load(file)

print(t.keys())
print(t["0"]["intervals"])