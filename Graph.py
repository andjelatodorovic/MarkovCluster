
"""
@author: kobrica@pmf
"""

class Node(object):
    
    def __init__(self, value):
        self.value = value
        self.neighbors = {}
        self.inDegree = 0
        self.outDegree = 0
    
    def updateEdgeWeight(self, key):
        pass
        
    def getEdgeWeight(self, key):
        if self.isConnectedTo(key):
            return self.neighbors[key]
        return None
    
    def connectTo(self, key, weight):
        self.neighbors[key] = weight

    def isConnectedTo(self, key):
        return key in self.neighbors
        
class Graph(object):
    def __init__(self, directedGraph=False):
        
        self.directedGraph = directedGraph
        self.nodes = {}
        self.nodesCount = 0
        self.edgeCount = 0
        
    #Modifikacije/iso34
    def addNode(self, key, value):
        
        if not self.hasNode(key):
            self.nodes[key] = Node(value)
            self.nodesCount += 1         
            
    def addEdge(self, key1, key2, weight=1): 
    
        if not self.hasNode(key1) or not self.hasNode(key2):
            return None
        if not self.hasEdge(key1, key2):
            self.nodes[key1].connectTo(key2, weight)
            self.edgeCount += 1
        
        if not self.directedGraph:
            if not self.hasEdge(key2, key1):
                self.nodes[key2].connectTo(key1, weight)
 
    def updateNodeValue(self, key):
        pass
    def updateEdge(self, key1, key2, newWeight):
        pass
    def removeNode(self, key):       
        pass
    def removeEdge(self,node1,node2):
        pass

    
    def getNodeValue(self, key):
   
        if (self.hasNode(key)):
            return self.nodes[key].value 
        return None
    
    def getEdgeWeight(self, key1, key2):
  
        if self.hasNode(key1):
            return self.nodes[key1].getEdgeWeight(key2)
        return None
    
    def getAllNodes(self):
    
        res = []
        for k in self.nodes:
            res.append((k,self.getNodeValue(k)))            
        return res
    
    def getAllEdges(self):
        res = []
        for k in self.nodes:
            for k1 in self.nodes[k].neighbors:
                if self.directedGraph: 
                    res.append((k,k1))
                else:
                    if (k1, k) not in res:
                        res.append((k, k1))
        return res
        
    def getNeighbours(self, key):
        
        if self.hasNode(key):
            return [(x, self.getNodeValue(x)) for x in self.nodes[key].neighbors]
        return None
    
    def hasNode(self, key):
    
        return key in self.nodes
        
    def hasEdge(self, key1, key2):
        
        if self.hasNode(key1):
            return self.nodes[key1].isConnectedTo(key2)
        return False
    
    def nodesCount(self):
        return self.nodesCount
        
    def inDegree(self, key):
        pass
    def outDegree(self, key):
        pass


    # Algoritmi
        
    def DepthFirstSearch(self, key1, key2):

        pass 
    
    def Dijkstra(self, key1):
 
        pass
        
    def Kruskal(self):

        pass
    
    def degreeCentrality(self, key):   

        pass
        
    def UnionFind(self):
 
        pass

    def getGraphMatrix(self):
        mapKeysToIndexes = {}
        mapIndexesToKeys = [None] * self.nodesCount
        c = 0
        for k in self.nodes:
            mapKeysToIndexes[k] = c 
            mapIndexesToKeys[c] = k
            c += 1
        
        matrix = [[0 for _ in range(self.nodesCount)] 
                for _ in range(self.nodesCount)]
        for k in self.nodes:
            for k1 in self.nodes[k].neighbors:
                matrix[mapKeysToIndexes[k]][mapKeysToIndexes[k1]] = \
                        self.nodes[k].neighbors[k1]
         
        return (matrix, mapIndexesToKeys)
        
        s = ""
        for n1 in self.nodes:
            s += str(n1) + ": "
            for n2 in self.nodes[n1].neighbors:
                s+= str(n2) + "->"
            s += "\n"
        return s
