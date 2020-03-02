from random import random

drone = {
        "color":None,
        "weight":None,
        "size":None,
        "number of propellers":None,
        "speed":None,
        "battery type":None,
}

if __name__ == "__main__":
        for key in drone.keys():
                drone[key] = input("{}: ".format(key))
        print(drone)