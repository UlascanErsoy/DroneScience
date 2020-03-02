
def map4DigitBinary(x):
    if len(x) == 4:
        return int(x,2)
    else:
        print("The number {} is supposed to have 4 digits!".format(x))

if __name__ == "__main__":
    seq = [*map(map4DigitBinary,input("Enter a sequence of 4 digit binary numbers: ").split(","))]
    for n in seq:
        if n%5 == 0:
            print("{:b}".format(n),end=" ")
    print("")