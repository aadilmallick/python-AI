import sys; args = sys.argv[1:]

def possibleMoves(pzl):
    pos = pzl.index('_')

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

def solvePuzzle(pzl)  -> object:
    seenStates = {pzl : ''}
    workingList = [pzl]
    pzlcountAtStep = {}
    count = 0
    while len(workingList) > 0: #make workinglist into dictionary
        parent = workingList.pop(0) #pop the one with shortest distance
        '''if parent == solution:
            pzlcountAtStep[count] = len(possibleMoves(parent))
            return pzlcountAtStep'''
        children = possibleMoves(parent)
        pzlcountAtStep[count] = len(children) + 1
        count+=1
        #print('children' , children)
        for child in children:
            if child not in seenStates:
                workingList.append(child) #workinglist[child] = getDistance[child]
                seenStates[child] = parent #save parent as previous step from child
    return pzlcountAtStep

def swap(moves , pos, pzl):
    children = []
    for move in moves:
        lst = [*pzl]
        #swap pzl[move] with pzl[pos]
        temp = lst[move]
        lst[move] = lst[pos]
        lst[pos] = temp
        stringl = ''.join(lst)
        children.append(stringl)
    return children

#Time for 500 random puzzles (s)


#Ave. time for impossible (s)


#Impossible count


#Average depth for the possible puzzles


#Ave time for possible (s)



dicc = solvePuzzle('12345678_')
sett = set()
for x,y in dicc.items():
        sett.add(y)
#if len(sys.argv) == 2:
print('Degree List:' , sett)

