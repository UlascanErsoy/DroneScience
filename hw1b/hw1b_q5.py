
if __name__ == "__main__":
    seq = [*map(int,input("Enter 4 numbers seperated by a comma:").split(","))]
    if seq[1:] == seq[:-1]:
        print(sum(seq)*4)
    else:
        print(sum(seq))
