import sys; args = sys.argv[1:]
#Aadil Mallick pd 6
import time, random
startTime = time.process_time()
gwidth = 3
gheight = 3
posmoves = {}
posmoves[0] = [1 , 3]
posmoves[1] = [0,2,4]
posmoves[2] = [1 , 5]
posmoves[3] = [0, 4, 6]
posmoves[4] = [1 , 3,5,7]
posmoves[5] = [2,4,8]
posmoves[6] = [3,7]
posmoves[7] = [4,6,8]
posmoves[8] = [5,7]


def printPuzzle(pzl):
    size = int(len(pzl) ** .5)
    strarr = []
    for i in range(size):
        strarr.append(pzl[ i*size : (i+1) * size])
    for e in strarr:
        print(e)

def createRandomPuzzle3by3():
    choose = '12345678_'
    newpzl = ''
    count = 0
    while len(newpzl) < 9:
        index = random.randint(0 , 8)
        if choose[index] not in newpzl:
            newpzl += choose[index]
            count+=1
    return newpzl





def findSolution(pzl):
    tempstring = pzl.replace('_' , '')
    tempstring = sorted(tempstring)
    tempstring.append('_')
    return ''.join(tempstring)

def printPuzzleBands(arr):
    #print out multiline strings on same line
    if len(arr) <= 5:
        strarr = []
        #fill up strarr with empty strings
        for i in range(gheight):
            strarr.append('')
        for i in range(gheight):
            for elem in arr:
                strarr[i] += (elem[i*gwidth : (i+1)*gwidth] + '  ')
        for e in strarr:
            print(e)
        return

    lowerbound = 0
    upperbound = 5
    finalband = len(arr) % 5
    while upperbound <= len(arr) - finalband:
        strarr = []
        for i in range(gheight):
            strarr.append('')
        for i in range(gheight):
            for elem in arr[lowerbound : upperbound]:
                strarr[i] += (elem[i*gwidth : (i+1)*gwidth] + '  ')
        for e in strarr:
            print(e)
        print()
        lowerbound+=5
        upperbound+=5

    strarr = []
    for i in range(gheight):
        strarr.append('')
    for i in range(gheight):
        for elem in arr[(len(arr) - finalband) : ] :
            strarr[i] += (elem[i * gwidth: (i + 1) * gwidth] + '  ')
    for e in strarr:
        print(e)
    print()



def determineDimensions(pzl):
    square = False
    if len(pzl) ** .5 == int(len(pzl) ** .5):
        square = True
    if(square == True):
        return int(len(pzl) ** .5) , int(len(pzl) ** .5)
    else:
       return 1,1





#teacher want us to print in bands
def process(seenStates , solution) :
    temp = solution
    outputs = []
    while(len(temp) > 0):
        outputs.append(seenStates[temp])
        temp = seenStates[temp]
    #[(printPuzzle(x) , print()) for x in outputs[::-1]]
    pzllist = outputs[::-1]
    pzllist.append(solution)
    pzllist.pop(0)
    printPuzzleBands(pzllist)
    #printPuzzle(solution)
    print()
    print('Steps:' , len(outputs)-1 )



def fillPosMoves(pzl):
    dicti = {}
    for index in range(len(pzl)):
        cur = []
        if canMoveUp(pzl , index):
            cur.append(moveUp(pzl , index))
        if canMoveDown(pzl, index):
            cur.append(moveDown(pzl, index))
        if canMoveRight(pzl, index):
            cur.append(moveRight(pzl, index))
        if canMoveLeft(pzl, index):
            cur.append(moveLeft(pzl, index))
        dicti[index] = cur
    return dicti


'''0123
   4567
   89ab
   cde_'''
def possibleMoves(pzl):
    pos = pzl.index('_')
    children = swap( pos, pzl)
    return children

def canMoveUp(pzl , pos):
    return pos - gwidth >= 0

def canMoveDown(pzl , pos):
    return pos + gwidth < len(pzl)

def canMoveLeft(pzl , pos):
    return (pos % gwidth) - 1 >= 0

def canMoveRight(pzl , pos):
    return (pos % gwidth) + 1 < gwidth

def moveUp(pzl , pos):
    return pos - gwidth

def moveDown(pzl , pos):
    return pos + gwidth

def moveRight(pzl , pos):
    return pos + 1

def moveLeft(pzl , pos):
    return pos - 1







def swap( pos, pzl):
    children = []
    moves = posmoves[pos]
    for move in moves:
        lst = [*pzl]
        #swap pzl[move] with pzl[pos]
        temp = lst[move]
        lst[move] = lst[pos]
        lst[pos] = temp
        stringl = ''.join(lst)
        children.append(stringl)
    return children





def isSolvable(pzl , goal):
#Recap:for an odd width slider puzzle, the parity of the inversion counts must match for the puzzle and goal to be solvable.
#For an even width slider puzzle, the parity of(the inversion count + rowNumberOfTheEmptyTile)
# must match for the puzzle and goal.
    #1. find inversions of pzl and goal
    inversionsPzl = 0
    inversionsGoal = 0
    under = pzl.index('_')
    rowpos = under//gwidth
    lst = [x for x in pzl if x != '_']
    pzlcopy = pzl.replace('_', '')
    goalcopy = goal.replace('_' , '')
    for i in range(0, len(pzlcopy) - 1):
            for y in range(i+1, len(pzlcopy)):
                if pzlcopy[i] > pzlcopy[y] and i < y:
                    inversionsPzl+=1
    for i in range(0, len(goalcopy) - 1):
            for y in range(i+1, len(goalcopy)):
                if goalcopy[i] > goalcopy[y] and i < y:
                    inversionsGoal+=1
    #2.find paritys of pzl and goal inversions
    parityPzl = inversionsPzl % 2
    parityGoal = inversionsGoal % 2
    #3.separate cases into even and odd width
    if(len(pzl) % 2 == 1): #odd width
        return True if (parityPzl == parityGoal) else False
    if(len(pzl) % 2 == 0): #even width
        parityPzl = (inversionsPzl + rowpos) % 2
        parityGoal = inversionsGoal % 2
        return True if (parityPzl == parityGoal) else False
    else:
        return False


def solvePuzzle(pzl: object)  -> object:
    if not isSolvable(pzl , '12345678_'):
        printPuzzle(pzl)
        print()
        print('Steps: -1')
        return

    seenStates = {pzl : ''}
    workingList = [pzl]
    #solution = findSolution(pzl)
    solution = '12345678_'

    if pzl == solution:
        printPuzzle(pzl)
        print()
        print('Steps: 0')
        return

    while len(workingList) > 0: #make workinglist into dictionary
        #print(workingList)
       # print(workingList)
        parent = workingList.pop(0) #pop the one with shortest distance
        if parent == solution:
            process(seenStates , solution)
            return
        children = possibleMoves(parent)
        #print('children' , children)
        for child in children:
            if child not in seenStates:
                workingList.append(child) #workinglist[child] = getDistance[child]
                seenStates[child] = parent #save parent as previous step from child
    printPuzzle(pzl)
    print()
    print('Steps: -1')

def solvePuzzle2param(pzl , solution) :

    if pzl == solution:
        printPuzzle(pzl)
        print()
        print('Steps: 0')
        return

    if not isSolvable(pzl , solution):
        printPuzzle(pzl)
        print()
        print('Steps: -1')
        return

    seenStates = {pzl : ''}
    workingList = [pzl]


    while len(workingList) > 0: #make workinglist into dictionary
        #print(workingList)
        parent = workingList.pop(0) #pop the one with shortest distance
        if parent == solution:
            process(seenStates , solution)
            return
        children = possibleMoves(parent)
        #print('children' , children)
        for child in children:
            if child not in seenStates:
                workingList.append(child) #workinglist[child] = getDistance[child]
                seenStates[child] = parent #save parent as previous step from child
    printPuzzle(pzl)
    print()
    print('Steps: -1')

def returnSteps(seenStates , solution):
    temp = solution
    outputs = []
    while (len(temp) > 0):
        outputs.append(seenStates[temp])
        temp = seenStates[temp]
    return len(outputs) - 1

def solvePuzzleRandom(pzl: object)  -> object:
    if not isSolvable(pzl , '12345678_'):
        return -1

    seenStates = {pzl : ''}
    workingList = [pzl]
    #solution = findSolution(pzl)
    solution = '12345678_'

    if pzl == solution:
        return 0

    while len(workingList) > 0: #make workinglist into dictionary
        #print(workingList)
       # print(workingList)
        parent = workingList.pop(0) #pop the one with shortest distance
        if parent == solution:
            return returnSteps(seenStates , solution)
        children = possibleMoves(parent)
        #print('children' , children)
        for child in children:
            if child not in seenStates:
                workingList.append(child) #workinglist[child] = getDistance[child]
                seenStates[child] = parent #save parent as previous step from child



def main():
    if args:
        if len(sys.argv) == 2:
            gwidth, gheight = determineDimensions(args[0])
            posmoves = fillPosMoves(args[0])
            solvePuzzle(args[0])
        if len(sys.argv) == 3:
            gwidth, gheight = determineDimensions(args[0])
            posmoves = fillPosMoves(args[0])
            solvePuzzle2param(args[0], args[1])
    else:
        puzzlesToSolve = 500
        stats = [0] * 5
        #index 0 is impossible count
        #index 1 is possible count
        #index 2 is total time of impossible cases
        #index 3 is total time of possible cases
        #index 4 is sum of path lengths
        for i in range(puzzlesToSolve):
            cur = createRandomPuzzle3by3()
            mytime = time.time()
            pathlen = solvePuzzleRandom(cur)
            if pathlen == -1: #impossible cases
                stats[0] += 1
                stats[2] += (time.time() - mytime)
            if pathlen >= 0:
                stats[1] += 1
                stats[3] += (time.time() - mytime)
                stats[4] += pathlen

        endTime = time.process_time() - startTime
        print('Total time:' , endTime)
        print('Average time for an impossible puzzle:' , ('%.03fs' % (stats[2]/stats[0])))
        print('Average time for a possible puzzle:', ('%.03fs' %  (stats[3] / stats[1])))
        print('Average path length for a possible puzzle:' , (stats[4]/stats[1]))
        print('num of impossible:' , stats[0])

if __name__ == '__main__' : main()


