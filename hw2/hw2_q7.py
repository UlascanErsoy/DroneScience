
if __name__ == "__main__":
    d = {"Key%d"%(a):"Value%d"%(a) for a in range(1,4)}
    e = {"Key%d"%(a):"Value%d"%(a) for a in range(4,7)}
    d.update(e)
    print(d)