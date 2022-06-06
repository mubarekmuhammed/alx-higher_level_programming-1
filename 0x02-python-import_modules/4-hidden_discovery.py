#!/usr/bin/python3

if __name__ == "__main__":
    """Prints all the names defined by the compiled module hidden_4.pyc"""
    import hidden_4

    i = 0

    mylist = dir(hidden_4)
    newlist = sorted(mylist)
    while i < len(newlist):
        if newlist[i][0] != '_':
            print(newlist[i])
        i += 1
