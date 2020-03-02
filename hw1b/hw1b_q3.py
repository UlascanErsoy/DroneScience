
if __name__ == "__main__":
    for n in range(0,50):
        r = ""
        if not n%3:
            r+="fizz"
        if not n%5:
            r+="buzz"
        if len(r) != 0:
            print(r)
        else:
            print(n)