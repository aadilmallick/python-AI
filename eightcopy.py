import sys

def printPuzzle(pzl):
    str1 = pzl[:3]
    str2 = pzl[3:6]
    str3 = pzl[6:]
    print(str1)
    print(str2)
    print(str3)

def isSolvable(pzl):
    #If the grid width is odd, then the number of inversions in a solvable situation is even.
    under = pzl.index("_")
    pzlcopy = [x for x in pzl if x != "_"]
    inversions = 0
    for i in range(0 , len(pzl)):
        for y in range(1 , len(pzl)):
            if pzl.index(i) == "_" or pzl.index(y) == "_": #dont count underscore
                continue
            else:
                if pzlcopy.index(i) > pzlcopy.index(y):
                    inversions+=1
    return True if(inversions % 2 == 0) else False






def process(seenStates , solution) :
    temp = solution
    outputs = []
    while(len(temp) > 0):
        outputs.append(seenStates[temp])
        temp = seenStates[temp]
    [(printPuzzle(x) , print()) for x in outputs[::-1]]
    printPuzzle(solution)
    print(len(outputs) + 1 , "steps")

def findSolution(pzl):
    tempstring = pzl.replace('_' , '')
    '''temp = [int(x) for x in pzl]
    temp.sort()
    solution = ''.join([str(x) for x in temp])
    solution += '_'
    return solution'''
    #sol = ''.join(sorted(tempstring)) + '_'
    temp = [int(x) for x in tempstring]
    temp.sort()
    sol = ''.join([str(x) for x in temp])
    sol += '_'
    return sol


#012
#345
#678
def possibleMoves(pzl):
    pos = pzl.index("_")

    #pos is 0
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
    children = swap(posmoves[pos], pos, pzl)
    return children




def swap(children, pos, pzl):
    stringList =  []
    for elem in children:
        pzlcopy = pzl[:]

        smaller = min(pos , elem)
        larger = max(pos , elem)
        if larger <= 8:
            newpzl = pzlcopy[:smaller] + pzlcopy[larger] + pzlcopy[smaller+1:larger] + pzlcopy[smaller] + pzlcopy[larger+1:]
        else:
            newpzl = pzlcopy[:smaller] + pzlcopy[larger] + pzlcopy[smaller + 1:larger] + pzlcopy[smaller] + pzlcopy[
                                                                                                            larger:]
        stringList.append(newpzl)

    return stringList

def shortestDistance(workingList , solution):
    distances = []
    for elem in workingList:
        distances.append(getDistance(elem , solution))
    smallest = min(distances)

def getDistance(child , solution):
    #distance between 1 of child and 1 of solution etc between 8 of child and 8 of solution
    childpos = []
    for i in range(0,9):
        if i == 8:
            childpos[i] = child.index("_")
        childpos[i] = child.index(str(i))
    distance = 0
    for i in range(0,9):
        distance += abs(childpos[i]-solution.index(i))
    return distance

def solvePuzzle(pzl) :
    seenStates = {pzl : ""}
    solution = "12345678_"
    workingList = {pzl : getDistance(pzl , solution)}
    #workingList = [pzl] original

    while len(workingList) > 0: #make workinglist into dictionary
        #print(workingList)
        parent = workingList.pop(0) #pop the one with shortest distance
        if parent == solution:
            process(seenStates , solution)
            return
        children = possibleMoves(parent)
        #print("children" , children)
        for child in children:
            if child not in seenStates:
                workingList[child] = getDistance[child] #workinglist[child] = getDistance[child]
                seenStates[child] = parent #save parent as previous step from child

if __name__ == "__main__" :

    #solvePuzzle("38524_176")
    print(isSolvable("38524_176"))
