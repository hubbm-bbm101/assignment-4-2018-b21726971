import sys
myFile = open(sys.argv[1], "r")
myFile = myFile.readlines()
myDict = {}
counter = 1
mylist = []
mylist2 = []
final_list = []
for poland in myFile:
    another_one = []
    for prussia in poland:
        try:
            another_one.append(int(prussia))
        except ValueError:
            pass
    myDict[counter] = another_one
    counter += 1


def printer(x):
    global row
    global column
    deleter()
    destroyer()
    if x != 1:
        for turkey in range(1, len(myDict)+1):
            str1 = " ".join(str(e) for e in myDict[turkey])
            print(str1)
        if len(mylist) == 0 or len(mylist) == 1:
            print("Your score is 0")
        if len(mylist) > 1:
            final = fibonacci(mylist[-1]-mylist[-2])*mylist2[-1]
            final_list.append(final)
            print("Your score is {}".format(sum(final_list)))
    if endgame():
        print("Game Over")
        sys.exit()
    answer = input("Please enter a row and column number : ")
    answer = answer.split(" ")
    row, column = int(answer[0]), (int(answer[1])-1)
    if row > len(myDict) or column > len(myDict[1])-1:
        print("Please enter a correct size")
        printer(1)
    elif myDict[row][column] == " ":
        print("Please enter a correct size")
        printer(1)
    else:
        mylist2.append(myDict[row][column])
        first_checker(row, column)
        calculator()


def checker(x, y):
    global old_value
    old_value = myDict[row][column]
    a, b, c, d = 0, 0, 0, 0
    if x <= len(myDict) and y <= len(myDict[1])-1:
        if y+1 <= len(myDict[1])-1:
            if myDict[x][y] == myDict[x][y+1] and myDict[x][y] != " ":
                a += 1
        if y-1 >= 0:
            if myDict[x][y] == myDict[x][y-1] and myDict[x][y] != " ":
                b += 1
        if x+1 <= len(myDict):
            if myDict[x][y] == myDict[x+1][y] and myDict[x][y] != " ":
                c += 1
        if x-1 >= 1:
            if myDict[x][y] == myDict[x-1][y] and myDict[x][y] != " ":
                d += 1
        myDict[x][y] = " "
        if a == 1:
            checker(x, y+1)
        if b == 1:
            checker(x, y-1)
        if c == 1:
            checker(x+1, y)
        if d == 1:
            checker(x-1, y)


def calculator():
    change = 0
    for ulm in range(1, len(myDict)+1):
        for bavaria in range(len(myDict[1])):
            if myDict[ulm][bavaria] == " ":
                change += 1
    mylist.append(change)
    printer(0)


def first_checker(x, y):
    a, b, c, d = 0, 0, 0, 0
    if x <= len(myDict) and y <= len(myDict[1])-1:
        if y+1 <= len(myDict[1])-1:
            if myDict[x][y] == myDict[x][y+1] and myDict[x][y] != " ":
                a += 1
        if y-1 >= 0:
            if myDict[x][y] == myDict[x][y-1] and myDict[x][y] != " ":
                b += 1
        if x+1 <= len(myDict):
            if myDict[x][y] == myDict[x+1][y] and myDict[x][y] != " ":
                c += 1
        if x-1 >= 1:
            if myDict[x][y] == myDict[x-1][y] and myDict[x][y] != " ":
                d += 1
    if (a or b or c or d) == 0:
        pass
    else:
        checker(x, y)


def deleter():
    for patch in range(len(myDict)):
        for york in range(len(myDict[1])):
            for wessex in range(1, len(myDict)):
                if myDict[wessex+1][york] == " ":
                    myDict[wessex+1][york] = myDict[wessex][york]
                    myDict[wessex][york] = " "


def destroyer():
    for york in range(len(myDict[1])-1):
        dest = 0
        for wessex in range(1, len(myDict)+1):
            if myDict[wessex][york] == " ":
                dest += 1
        if dest == len(myDict):
            for wessex in range(1, len(myDict)+1):
                myDict[wessex][york] = myDict[wessex][york+1]
                myDict[wessex][york+1] = " "
    gs = 0
    for monster in range(len(myDict[1])):
        if myDict[1][monster] == " ":
            gs += 1
    if gs == len(myDict[1]):
        a = myDict[1]
        for j in range(1, len(myDict)):
            myDict[j] = myDict.pop(j+1)
        myDict[len(myDict)+1] = a


def fibonacci(x):
    x = int(x)
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return fibonacci(x-1) + fibonacci(x-2)


def endgame():
    crom = 0
    for d in range(1, len(myDict)+1):
        for f in range(len(myDict[1])-1):
            if myDict[d][f] == myDict[d][f+1] and myDict[d][f] != " ":
                crom += 1
    for i in range(len(myDict[1])):
        for r in range(1, len(myDict)):
            if myDict[r][i] == myDict[r+1][i] and myDict[r][i] != " ":
                crom += 1
    if crom >= 1:
        return False
    else:
        return True


calculator()
