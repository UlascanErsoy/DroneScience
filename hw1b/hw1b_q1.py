
if __name__ == "__main__":
    for i in range(2):
        for j in range(5):
            if i == 0:
                print("*"*(j+1))
            else:
                print("*"*(4-j))