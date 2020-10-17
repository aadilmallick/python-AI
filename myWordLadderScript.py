#import sys; args = sys.argv[1:]
#aadil mallick period 7
#myList = open(args[0],'r').read().splitlines()
import time
#myList = set(myList)
myList = set(open('myWordFile.txt', 'r').read().splitlines())
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
            print('example of a word with second highest degree:' ,y[0])
    return 'no word in list has such degree'


def outputDegrees(degreeList):
    string = ''
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




'''def largestConnectedComponentSize():
    components = set()
    for word in myList:
        components.add(len(createConnectedComponent(word)))
    return max(components)'''



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

def createComponentDistanceV(root): #find all veritces than can be reached from one word
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
    return component


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
    all3 = []
    allk3 = {}
    for diction in components:
        if len(diction) == 3:
            all3.append(diction)
            keys = []
            for i in diction.keys():
                keys.append(i)
            if isLinked(keys[0] , keys[1]) and isLinked(keys[0] , keys[2]) and isLinked(keys[1] , keys[2]):
                count+=1
                allk3[count] = keys
            else:
                count+=0
    print('these are all the len 3 components:' , all3)
    print('these are all the k3 components:', allk3)

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


print('word count:' , len(myList))
print('Edge count:' , totalEdges(wordgraph))
outputDegrees(degreeList)
keys = sorted(degreeList.keys())
printWordDegree(keys[-2] , degreeList)
'''lengths = []
for elem in wordgraph:
    if len(elem) not in lengths:
        lengths.append(len(elem))
print('example of a word with second highest degree:', lengths[-2])'''
print()

components = []
for word in myList:
    if word not in ccvisited:
        components.append(getConnectedComponents(word))
print([str(len(x)) + ' ' for x in components])
#put len into set adn thats number 6
diff = set([len(x) for x in components])
print('number of different component sizes' , len(diff))
#get max of len and that number 7
maxi = max([len(x) for x in components])
print('largest component size' , maxi)

print('num of k2' , numK2())
print('num of k3' , numK3())
print('num of k4' , numK4())

print(['step ' + str(x) + ': ' + y for x,y in enumerate(shortestPath('faring' , 'coated'))])

print(createComponentDistanceV('abater'))
print(returnLinked('amuser'))
print('farthest word' , getFarthestWord('faring'))


#print(getFarthestWord('abater'))
#print(largestConnectedComponentSize())
#print('k2:' , exampleComponent(2))
#print('k3:', exampleComponent(3))
#print('k4:', exampleComponent(4))
#k2 is a connected component with 2 vertices

print(wordgraph['coated'])
total = time.time() - start
print('%.03f' % (total))
