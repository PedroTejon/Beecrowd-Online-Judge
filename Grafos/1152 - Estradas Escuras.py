class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
 
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])
 
    def find(self, parent, i):
        if parent[i - 1] == i:
            return i
        return self.find(parent, parent[i - 1])
 
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
 
        if rank[xroot - 1] < rank[yroot - 1]:
            parent[xroot - 1] = yroot
        elif rank[xroot - 1] > rank[yroot - 1]:
            parent[yroot - 1] = xroot
        else:
            parent[yroot - 1] = xroot
            rank[xroot - 1] += 1
 
    def KruskalMST(self):
        result = []
         
        i = 0
        
        e = 0
        
        self.graph = sorted(self.graph, key=lambda item: item[2])
        graph2 = self.graph.copy()
        parent = [node for node in range(1, self.V + 1)]
        rank = [0 for _ in range(self.V)]
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
 
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
                graph2.remove([u, v, w])

        return sum([x[2] for x in graph2])


resultado = []
while True:
    qntdVertices, qntdEdges = map(int, input().split())
    if qntdVertices == 0 and qntdEdges == 0:
        break
    
    g = Graph(qntdVertices)

    for _ in range(qntdEdges):
        a, b, p = map(int, input().split())
        g.addEdge(a, b, p)

    resultado.append(g.KruskalMST())

[print(result) for result in resultado]