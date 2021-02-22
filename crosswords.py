import sys; args = sys.argv[1:]

worddictionary = {}
BLOCKCHAR = '#'
OPENCHAR = '-'
rotation_lookup = {}
adjacent_lookup = {}
height = 0
width = 0
#change the board back into a string before recursion

#JUST REVERSE THE LIST!! THAT IS 180 SYMMETRY

def createRotationLookupTable():
    rotation = {}
    origboard = [x for x in range(height*width)]
    rotatedboard = origboard[:]
    rotatedboard.reverse()
    #for each position in the original board, find its rotated position
    for i in range(len(origboard)):
        pos = origboard[i]
        rotation[pos] = rotatedboard[i]
    return rotation


def handleArgs(args):
    parse1 = args[0]
    xspot = parse1.index('x')
    rows = int(parse1[:xspot])
    columns = int(parse1[xspot+1:])

    parse2 = args[1]
    numblocking = int(parse2)

    parse3 = args[2]
    file = parse3

    if len(args) > 3:
        seedstringlist = args[3:]
        return (rows , columns, numblocking, file, seedstringlist)
    else:
        return (rows , columns, numblocking, file, [])

def f():
    return [ [*range(i*width , (i+1)*width)] for i in range(height)]

def createDict(wordlist):
    # this version is word:length
    '''worddict = {}
    for word in wordlist:
        if len(word) > 3:
            if word.isalpha():
                worddict[word] = len(word)
    return worddict

    #this version is [(word , length)]
    worddict = []
    for word in wordlist:
        if len(word) > 3:
            if word.isalpha():
                worddict.append((word , len(word)))
    return worddict'''

    #this version is length: [words]
    #find max length word in list
    max = 0
    for word in wordlist:
        if len(word) > max:
            max = len(word)
    worddict = {x:[] for x in range(3,max+1)}
    for word in wordlist:
        if len(word) in worddict:
            worddict[len(word)].append(word)
    return worddict

#  H#x#chars or V#x#chars
def readInSeedString(seedstringlist): #parses the seedstring into a tuple with values
    #if chars is omitted it implies a single blocking square
    #placement starts at 0x0 whihc is the top left square with first digit being horizontal offset
    #each is either H(num)x(num)chars or V(num)x(num)chars
    tuplelist = []
    for seedstring in seedstringlist:
        orientation = seedstring[0]
        toparse = seedstring[1:]
        dim = toparse.index('x')
        V_offset = int(toparse[:dim])
        H_offset = -1
        toparse2 = toparse[dim+1:dim+1+2]
        breakpoint = None
        if toparse2.isdigit(): #2 digit number
            H_offset = int(toparse2)
            breakpoint = dim+3
        else:
            H_offset = int(toparse[dim+1:dim+2])
            breakpoint = dim+2
        if not toparse[breakpoint:] or toparse[breakpoint] == '#': #chars is omitted
            #implies single blocking square at coordiantes height,width
            tuplelist.append(('blocking' , BLOCKCHAR , V_offset, H_offset)) #false means that it is false for a normal seedstring
        else:
            tuplelist.append(('string' , toparse[breakpoint:] , V_offset, H_offset, orientation))
            #return word at coordinates(height,width) with a given orientation
    return tuplelist


def createEmptyBoard():
    string = OPENCHAR * (height*width)
    return string

def print2D(board):
    for i in range(height):
        print(board[i*width:(i+1)*width])


def translateCoordinates(V_offset , H_offset):
    #starts from index (0 , 0)
    return (V_offset * width) + H_offset
    #if given a coordinate 4x5, that is 5 down and 6 to the right, so return 29

#works for test case 1 and 2

def createInitialBoard(seedlist): #creates the initial board with seedstringlist, before any blocking square stuff
    board = [*createEmptyBoard()]
    for seed in seedlist:
        if seed[0] == 'blocking':  # is a blocking square
            pos = translateCoordinates(seed[2], seed[3])
            board[pos] = BLOCKCHAR
        else:
            state, string, Voffset, Hoffset, orientation = seed
            startpos = translateCoordinates(Voffset , Hoffset)
            if orientation == 'H':
                i = startpos
                for char in string:
                    board[i] = char
                    i += 1
            else:  # if vertical
                i = startpos
                for char in string:
                    board[i] = char
                    i += width
    return board



def createAdjacentLookup():
    origboard = [x for x in range(height * width)]
    mydict = {}
    mydict[0] = [1,width]
    mydict[width-1] = [width-2, width - 1 + width]
    mydict[height*width - 1] = [height*width - 1-width, height*width-2]
    mydict[height*width - width] = [height*width-width + 1, height*width - width -width]

    topedge = [x for x in range(1, width -1) ]
    for pos in topedge:
        mydict[pos] = [pos+1,pos-1, pos+width]

    bottomedge = [x for x in range(height*width - width + 1 , height*width - 1)]
    for pos in bottomedge:
        mydict[pos] = [pos+1,pos-1, pos-width]

    leftedge = [x for x in range(width , height*width - width, width)]
    for pos in leftedge:
        mydict[pos] = [pos+width , pos-width, pos+1]

    rightedge = [x for x in range(2*width-1 , height*width-width, width)]
    for pos in rightedge:
        mydict[pos] = [pos - width , pos + width, pos - 1]

    general = [x for x in origboard if x not in mydict]
    for pos in general:
        mydict[pos] = [pos - width, pos + width, pos - 1, pos + 1]
    return mydict
    #print(mydict)

def createFinalBoard(initboard , numblocking): #use to create Final board
    board = ''.join(initboard[:])
    if numblocking == 0:
        return board
    #while curnumblocks not equal numblocking

        #if curnumblocks == numblocking and board is valid: return board
        #place numblocks, implementing symmetry
            #place numblocks only if current space is empty
            #if rotated position is already occupied, this board is invalid
        #if board is valid, recurse --> recurse(newboard , curnumblock + 2, numblocking)
        #if board is invalid, return None
    #newboard = createFinalBoardHelper(board , )
    newboard , pos = placeInitialBlockingSquare(board , board.index(OPENCHAR))
    finalboard = createFinalBoardHelper(newboard , pos, 0 + findnumblocking(board , newboard) , numblocking)

def createFinalBoardHelper(board , initpos, curnumblocking , numblocking ):
    if curnumblocking == numblocking and isValid(board , numblocking):
        return board
    emptypos = getemptyspot(board , initpos)
    temp = placeBlockingSquare(board , emptypos)
    boardstatus = temp[0]
    if boardstatus == 'invalid':
        return None #if invalid board, dont recurse
    else:
        newboard = temp[1]
        createFinalBoardHelper(newboard , emptypos, findnumblocking(board , newboard), numblocking)

def findnumblocking(board , newboard): #finds num of blocking squares added
    return newboard.count(BLOCKCHAR) - board.count(BLOCKCHAR)

def placeInitialBlockingSquare(board , pos):
    firstelem = board[pos]
    rotatedfirstelem = board[rotation_lookup[pos]]

    while(firstelem != OPENCHAR and (rotatedfirstelem != OPENCHAR or rotatedfirstelem != BLOCKCHAR)):
        #while position is not empty and rotated position is illegal, keep traversing for legal spot
        pos = pos + 1
        firstelem = board[pos]
        rotatedfirstelem = board[rotation_lookup[pos]]

    return (modifyBoard(board , pos) , pos)



def modifyBoard(board , pos): #given a board, position, and rotated position, return a new board with blocking squares
    rotatedpos = rotation_lookup[pos]
    if pos == 0: #rotated will be last in list
        return BLOCKCHAR + board[pos+1:rotatedpos] + BLOCKCHAR
    elif rotatedpos == 0:
        return BLOCKCHAR + board[rotatedpos+1:pos] + BLOCKCHAR
    elif pos < rotatedpos:
        return board[:pos] + BLOCKCHAR + board[pos+1:rotatedpos] + BLOCKCHAR + board[rotatedpos+1:]
    elif rotatedpos < pos:
        return board[:rotatedpos] + BLOCKCHAR + board[rotatedpos+1:pos] + BLOCKCHAR + board[pos+1:]
    else:
        return None


def addAdjacent(curlist , pos):
    #adds all adjacent positions of pos to list
    adjacentlist = adjacent_lookup[pos]
    for elem in adjacentlist:
        curlist.add(elem)

def isValid(board ,  numblocking):
    emptyspots = [x for x in range(len(board)) if board[x] == OPENCHAR]
    if height*width - len(emptyspots) != numblocking:
        return False
    visited = set()
    curlist = set()
    pos = emptyspots[0]

    #append everything in getAdjacency[pos] to curlist
    addAdjacent(curlist , pos)
    visited.add(pos)

    while curlist:
        pos = curlist.pop()
        addAdjacent(curlist , pos)
        visited.add(pos)

    return len(visited) == len(emptyspots)


'''def getemptyspot(board):
    temp = {x for x in range(len(board)) if board[x] == OPENCHAR}
    return temp.pop()'''

def getemptyspot(board, pos):
    adjacent = adjacent_lookup[pos]
    emptyset = set()

    for position in adjacent: #for each position in the adjacent list, if it is empty, it is a viable candidate
        if board[position] == OPENCHAR:
            emptyset.add(position)

    if emptyset:
        return emptyset.pop()
    else:
        return board.index(OPENCHAR) #if no empty adjacents, just return

'''def placeBlockingSquare(board):
    pos = getemptyspot(board)
    newboard = [*board[:]]
    rotatedpos = rotation_lookup[pos]
    if newboard[rotatedpos] == OPENCHAR or newboard[rotatedpos] == BLOCKCHAR: #rotated spot is valid
        newboard[rotatedpos] = BLOCKCHAR
        newboard[pos] = BLOCKCHAR
        return ('valid' , ''.join(newboard))
    else: #rotated spot is occupied by letter
        return ('invalid')'''

def placeBlockingSquare(board, pos):
    rotatedpos = rotation_lookup[pos]
    if board[pos] != BLOCKCHAR and board[pos] != OPENCHAR and board[rotatedpos] != BLOCKCHAR and board[rotatedpos] != OPENCHAR:
        return ('invalid')
    else:
        return ('valid' , modifyBoard(board , pos))

    '''newboard = [*board[:]]
    newboard[rotatedpos] = BLOCKCHAR
    newboard[pos] = BLOCKCHAR
    return ('valid' , ''.join(newboard))'''





#test case: 10x10 86
if __name__ == '__main__':
    if not args:
        print('put in args bro')
        '''temp = '15x15 39 xwords.txt H0x0Mute V0x0mule V10x13Where H7x5# V3x4# H6x7# V11x3#'.split(' ')
        height,width, numblocking, file, seedlist = handleArgs(temp)
        newseedlist = readInSeedString(seedlist)
        init = createInitialBoard(height , width, newseedlist)
        print2D(init , height, width)'''
        height, width = 10,10
        rotation_lookup = createRotationLookupTable()
        adjacent_lookup = createAdjacentLookup()
        #print(createAdjacentLookup(10,10))
        #print([print(x) for x in f(10,10)])
        board = createEmptyBoard()
        board = modifyBoard(board , 99)
        print2D(board )
    else:
         rows, columns, numblocking, file , seedstringlist = handleArgs(args)
         height = rows
         width = columns
         newseedlist = readInSeedString(seedstringlist)
         initboard = createInitialBoard( newseedlist)
         print2D(initboard)
         rotation_lookup = createRotationLookupTable()
         adjacent_lookup = createAdjacentLookup()
         #print(rotation_lookup)
