
if __name__ == "__main__":
    group = input("Enter a group seperated by commas:").split(",")
    query = input("Enter a member to search for: ")
    print("\033[32m{}\033[m is in the group".format(query) if query in group else "\033[31m{}\033[m is not in the group".format(query))

