#import sys; args = sys.argv[1:]
#aadil mallick period 7
#myList = open(args[0],'r').read().splitlines()
import time
myList = open('myWordFile.txt', 'r').read().splitlines()

wordgraph = {}


def isLinked(word , word2):
    differences = 0
    for i in range(6):
        if word[i] != word2[i]:
            differences+=1
    return False if (differences > 1 or differences == 0) else True

def returnLinked(word , myList):
    linked = []
    for i in range(len(myList)):
        if isLinked(word , myList[i]):
            linked.append(myList[i])
    return linked

def totalEdges(graph):
    edges = 0
    #for i in range(len(graph)):
    #   edges += len(graph[i])
    for x,y in graph.items():
        edges += len(y)
    return edges

def maxEdges(graph):
    maxi = []
    for i in range(len(graph)):
        maxi[i] = len(graph[i])
    return max(maxi)



def degreeList(graph , myList):
    degrees = []
    numEdges = []
    #fill up degree with 1st degree words, and so on
    for i in range(len(graph)):
        degrees[myList[i]] = len(graph[i]) #key is word, value is edges for each word
    #find all words with degree measure i and store them
    for i in range(maxEdges(graph)+1):
        count = 0
        for x in range(myList):
            if degrees[myList[x]] == i:
                count+=1
        numEdges[i] = count
    return numEdges


start = time.time()
for i in range(len(myList)):
    wordgraph[myList[i]] = returnLinked(myList[i] , myList)
total = time.time() - start
#print("word count:" , len(myList))
#print("Edge count:" , totalEdges(wordgraph))
print(wordgraph["places"])
print(total)
