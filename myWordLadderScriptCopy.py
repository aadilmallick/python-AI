import sys; args = sys.argv[1:]
#aadil mallick period 7
myList = open(args[0],'r').read().splitlines()
import time
myList = set(myList)
#myList = set(open('myWordFile.txt', 'r').read().splitlines())
wordgraph = {}
degreeList = {} #key is num of edges value is list of all words with that num of edges
ccvisited = []

def isLinked(word , word2):
    differences = 0
    for i in range(6):
        if word[i] != word2[i]:
            differences+=1
    return False if (differences > 1 or differences == 0) else True


def returnLinked(word):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    linked = set()
    for i in range(len(word)):
        wordaslist = list(word)
        for j in alphabet:
            wordaslist[i] = j
            newword = ''.join(wordaslist)
            if(newword in myList):
                linked.add(newword)
    linked.remove(word)
    return linked




def totalEdges(graph):
    edges = 0
    #for i in range(len(graph)):
    #   edges += len(graph[i])
    for x,y in graph.items():
        edges += len(y)
    return edges//2






def printWordDegree(degree, degreeList):
    for x,y in degreeList.items():
        if x == degree:
            print('Second degree word:' ,y[0])
    return 'no word in list has such degree'


def outputDegrees(degreeList):
    string = 'Degree List: '
    keys = sorted(degreeList.keys())
    for x in keys:
        #string += 'degree ' + str(x) + ': ' + str(len(degreeList[x])) + '  '
        string += str(len(degreeList[x])) + '  '
    print(string)

def shortestPath(root, goal):
    seen = {root: ''}
    working = [root]
    while len(working) > 0:
        parent = working.pop()
        if parent == goal:
            return pathFromRootToGoal(seen , goal)
        children = list(returnLinked(parent))
        for child in children:
            if child not in seen:
                working.append(child)
                seen[child] = parent





def pathFromRootToGoal(seen , goal):
    temp = goal
    outputs = []
    while(temp != ''):
        outputs.append(temp)
        temp = seen[temp]
    return outputs[::-1]





def getFarthestWord(root): #find all veritces than can be reached from one word
    visited = {root : ('' , 0)} #start at root
    queue = [root]
    while len(queue) > 0:
        parent = queue.pop()
        children = list(returnLinked(parent))
        for child in children:
            if child not in visited:
                queue.append(child)
                visited[child] = (parent , visited[parent][1] + 1)
    component = {}
    for x in visited:
        distance = visited[x][1]
        if distance in component:
            component[distance].append(x)
        else:
            component[distance] = []
            component[distance].append(x)
    return component[max(component.keys())][-1]

def getConnectedComponents(root): #find all veritces than can be reached from one word
    visited = {root : ''} #start at root
    queue = [root]
    while len(queue) > 0:
        parent = queue.pop()
        children = list(returnLinked(parent))
        for child in children:
            if child not in visited:
                queue.append(child)
                visited[child] = parent
                ccvisited.append(child)
    return visited


def numK2():
    count = 0
    for diction in components:
        if len(diction) == 2:
            count+=1
    return count

def numK3():
    count = 0
    #allK3 = []
    for diction in components:
        if len(diction) == 3:
            keys = []
            for i in diction.keys():
                keys.append(i)
            if isLinked(keys[0] , keys[1]) and isLinked(keys[0] , keys[2]) and isLinked(keys[1] , keys[2]):
                count+=1
                #allK3.append(diction)
            else:
                count+=0
    #print('these are all the k3 components:' , allK3)
    return count

def numK4():
    count = 0
    #key is word value is parent: diction
    for diction in components:
        if len(diction) == 4:
            keys = []
            for i in diction.keys():
                keys.append(i)
            if isLinked(keys[0], keys[1]) and isLinked(keys[0], keys[2]) and isLinked(keys[1], keys[2]) and isLinked(keys[0] , keys[3]) and isLinked(keys[1] , keys[3]) and isLinked(keys[2] , keys[3]):
                count += 1
            else:
                count += 0
    return count








def neighbors(root):
    return wordgraph[root]




start = time.time()
for i in myList:
    wordgraph[i] = returnLinked(i)
    if len(wordgraph[i]) in degreeList:
        degreeList[len(wordgraph[i])].append(i)
    else:
        degreeList[len(wordgraph[i])] = []
        degreeList[len(wordgraph[i])].append(i)


print('Word count:' , len(myList))
print('Edge count:' , totalEdges(wordgraph))
outputDegrees(degreeList)
total = time.time() - start
print( 'Construction time:' , ('%.03f' % (total)) + 's')
keys = sorted(degreeList.keys())
printWordDegree(keys[-2] , degreeList)


components = []
for word in myList:
    if word not in ccvisited:
        components.append(getConnectedComponents(word))
#print([str(len(x)) + ' ' for x in components])
#put len into set adn thats number 6
diff = set([len(x) for x in components])
print('Connected component size count:' , len(diff))
#get max of len and that number 7
maxi = max([len(x) for x in components])
print('Largest component size:' , maxi)

print('K2 count:' , numK2())
print('K3 count:' , numK3())
print('K4 count:' , numK4())
try:
    n = args[1]
    print('Neighbors:' , neighbors(n))
    print()
    print('Farthest:' , getFarthestWord(n))
    #print('Path:' , ['step ' + str(x) + ': ' + y for x,y in enumerate(shortestPath(n, args[2]))])
    print('Path:' , [x for x in shortestPath(n , args[2])])
except:
    print('not enough arguments inputed for numbers 10-13')







total = time.time() - start
print('%.03f' % (total))
