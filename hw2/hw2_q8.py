
if __name__ == "__main__":
    print("You should get 1.")
    a = {(1,2):1,(2,3):2}
    assert(a[1,2]==1)
    print(a[1,2])
