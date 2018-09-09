import numpy 
import Graph
import MarkovCluster
        
f = open("../input_graph.txt","r")

grafo = Graph.Graph()
for line in f:
    edges = line.split()
    grafo.addNode(edges[0], edges[0])
    grafo.addNode(edges[1], edges[1])
    grafo.addEdge(edges[0], edges[1])

print "Reprezentacija preko liste: \n",grafo    

matrix, mapBackToKeys = grafo.getGraphMatrix()
numpymat = numpy.array(matrix)
print "Reprezentacija preko matrice: \n",numpymat
print "\nMapiranje indeksa matrice: ", mapBackToKeys

alg = MarkovCluster.MarkovClustering(matrix,e=2,r=2)
clusters = alg.computeClusters(T=40)

print "\nKlasteri nakon primene algoritma: "
for cluster in clusters:
    print [mapBackToKeys[x] for x in cluster]
