import sys; args = sys.argv[1:]
#Aadil Mallick pd 6
import time, random
startTime = time.process_time()
gwidth = 0
gheight = 0
posmoves3by3 = {}
posmoves4by4 = {}
solution = ''



def findSolution(pzl):
    return ''.join(sorted(pzl.replace('_' , ''))) + '_'

def randomFile3by3(file):
    f = open(file, 'w')
    for i in range(500):
        sol = [*'12345678_']
        random.shuffle(sol)
        string = ''.join(sol)
        f.write(string)
        f.write('\n')
    f.close()

def randomFile4by4(file):
    f = open(file, 'w')
    for i in range(500):
        sol = [*'ABCDEFGHIJKLMNO_']
        random.shuffle(sol)
        string = ''.join(sol)
        f.write(string)
        f.write('\n')
    f.close()

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
        dist = (gheight - 1) - rowpos
        return True if (inversionsPzl%2 == dist%2) else False
    else:
        return False



def returnSteps(seenStates , solution):
    temp = solution
    outputs = []
    while (len(temp) > 0):
        outputs.append(seenStates[temp])
        temp = seenStates[temp]
    return len(outputs) - 1

def swap( pos, pzl):
    children = []
    if len(pzl) % 2 == 1: #3by3
        moves = posmoves3by3[pos]
    else:
        moves = posmoves4by4[pos]
    for move in moves:
        lst = [*pzl]
        #swap pzl[move] with pzl[pos]
        temp = lst[move]
        lst[move] = lst[pos]
        lst[pos] = temp
        stringl = ''.join(lst)
        children.append(stringl)
    return children

def possibleMoves(pzl):
    pos = pzl.index('_')
    children = swap( pos, pzl)
    return children



def fillPosMoves(pzl):
    dicti = {}
    gwidth = int(len(pzl) ** 5)
    gheight = int(len(pzl) ** 5)
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

def solvePuzzleRandom(pzl: object)  -> object:
    if not isSolvable(pzl , findSolution(pzl)):
        return -1

    seenStates = {pzl : ''}
    workingList = [pzl]
    solution = findSolution(pzl)

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

def solveFile(f): #file f
    pzllist = open(f,'r').read().splitlines()
    stats = [0] * 4
    #stats[0] is total num of puzzles
    #stats[1] is total num of solvable puzzles
    #stats[2] is total length of solvable puzzles we want average
    #stats[3] is total time taken to process all puzzles
    counter = 0
    while time.process_time() - startTime < 90:
        gwidth = int(len(pzllist[counter]) ** 5)
        gheight = int(len(pzllist[counter]) ** 5)
        pathlen = solveManhattan(pzllist[counter] , findSolution(pzllist[counter]) , gwidth)
        if pathlen >= 0:
            stats[1] += 1
            stats[2] += pathlen
        stats[0] += 1
        counter+=1
    endTime = time.process_time() - startTime
    print('total num of puzzles:' , stats[0])
    print('total num of solvable:' , stats[1])
    print('average length of solvable puzzles:' , stats[2]/stats[1])
    print('total time:' , endTime)

#key will be puzl, value will be level
def returnDistances(goal , children , width):
    distances = {}
    for child in children:
        distances[child] = 0
        for char in solution:
            distances[child]+= abs( (child.index(char) % width) - (goal.index(char) % width) )
            distances[child] += abs((child.index(char) // width) - (goal.index(char) // width))
    return distances

def manhattanDist(root , goal, width):
    distance = 0
    for char in solution:
        distance += abs((root.index(char) % width) - (goal.index(char) % width))
        distance += abs((root.index(char) // width) - (goal.index(char) // width))
    return distance

def solveManhattan(root , goal, width):
    width = int(len(root) ** 5)
    if not isSolvable(root , goal):
        return -1
    if root == goal:
        return 0
    seenStates = {root : ''}
    priorityqueue = [(manhattanDist(root,goal,width) , root)] #queue of tuples
    count = 0
    while priorityqueue:
        mandist , parent = priorityqueue.pop(0)
        if parent == goal:
            return count
        children = possibleMoves(parent)
        count+=1
        for child in children:
            if child not in seenStates:
                seenStates[child] = parent
                mdn = manhattanDist(child , goal , width)
                priorityqueue += [ (mdn ,  child) ]
        priorityqueue.sort()



if __name__ == '__main__' :
    gwidth = 3
    gheight = 3
    posmoves3by3 = fillPosMoves('12345678_')
    gwidth = 4
    gheight = 4
    posmoves4by4 = fillPosMoves('ABCDEFGHIJKLMNO_')
    if args:
        randomFile3by3(args[0])
        solveFile(args[0])




