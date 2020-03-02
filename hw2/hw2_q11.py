from random import random

def randPair(d):
        pairs = list(zip(d.keys(),d.values()))
        rand  = int(random() * len(pairs)) - 1
        print(pairs[rand])

if __name__ == "__main__":
        car = {
        "brand": "Tesla",
        "model": "S",
        "year": 2019}
        car["year"] = 2020
        car["mode"] = "ludicrous"
        for a in range(100):
                randPair(car)