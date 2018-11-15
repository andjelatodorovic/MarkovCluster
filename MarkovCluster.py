
import numpy

class MarkovClustering(object):

    def __init__(self, matrix, e, r):

        self.matrix = numpy.array(matrix,dtype=numpy.float64)
        self.e = e
        self.r = r
        
    def computeClusters(self, T = 100):
 
        self.addSelfLoops()
        self.normalizeColumns()
        
        t = 0
        while(t<T):
            lastMatrix = numpy.copy(self.matrix)
            self.powerStep()
            self.inflationStep()
            if self.steadyState(lastMatrix)==True:
                break
            t += 1

        return self.interpretClusters()
        
        
    def addSelfLoops(self):
      
        for i in range(self.matrix.shape[0]):
            self.matrix[i][i] = 1
            
    def normalizeColumns(self):

        s = self.matrix.sum(axis=0)
        for (x,y), _ in numpy.ndenumerate(self.matrix):
            if s[y] != 0:
                self.matrix[x][y] /= float(s[y])
        
    def powerStep(self): 
        temp = self.matrix
        for _ in range(self.e-1):
            temp = temp.dot(self.matrix) 
        self.matrix = temp
            
    def inflationStep(self):
        self.matrix **= self.r 
        self.normalizeColumns();
    
    def steadyState(self, lastMatrix):
        for (x,y), _ in numpy.ndenumerate(self.matrix):
            if self.matrix[x][y]-lastMatrix[x][y] != 0:
                return False
        return True
        
    def interpretClusters(self):
        res = []
        for i in range(self.matrix.shape[0]):
            cluster = []
            flag = 0
            for z in range(self.matrix.shape[0]):
                if self.matrix[i][z] > 0:
                    cluster.append(z)
                    flag = 1
            if flag==1:
                res.append(cluster)
        return res
