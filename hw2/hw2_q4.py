
def foo(list1,list2):
    if type(list1) != list or type(list2) != list:
        print("I was promised lists!")
        raise TypeError
    if len(set(list1) & set(list2)) > 0:
        print("Common Member!")

if __name__ == "__main__":
    list1 = input("Enter the first list(,):").split(",")
    list2 = input("Enter the second list(,):").split(",")
    foo(list1,list2)