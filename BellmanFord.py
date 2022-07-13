import math

class Vertex :
    def __init__(self, name):
        self.name=name
        self.d=math.inf
        self.p=None

    def __str__(self):
        return self.name

class Edge:
    def __init__(self, src, dest, w):
        self.src=src
        self.dest=dest
        self.w=w

class Graph:
    def __init__(self, V, E):
        self.V=V
        self.E=E

    def __str__(self):
        s=''
        for e in self.E:
            s += e.src.name + '->' + e.dest.name + ', w = '+str(e.w) + '.\n'
        return s

    def shortest_path(self, nodeA, nodeB):
        self.belman_ford(nodeA)
        list=self.print_path(nodeA, nodeB, [])
        print('Shortest path:')
        for v in list:
            print (v)
        print('Duzina: ', nodeB.d)
        return None

    def print_path(self, u, v, list):
        if v is u:
            list.append(u)
        elif v.p is None:
            print('No path from', u, 'to', v)
            return None, None
        else:
            list=self.print_path(u, v.p, list)
            list.append(v)
        return list


    def belman_ford(self, s):
        self.init_single_source(s)
        for v in self.V:
            for e in self.E:
                self.relax(e.src, e.dest, self.get_weight(e.src, e.dest))
        for e in self.E:
            if e.dest.d > e.src.d + self.get_weight(e.src, e.dest):
                return False
        return True

    def get_weight(self, u, v):
        for e in self.E:
            if e.src == u  and e.dest == v:
                return e.w
        return math.inf

    def init_single_source(self, s):
        for v in self.V:
            v.d=math.inf
            v.p=None
        s.d=0

    def relax(self, u, v, w):
        if v.d>u.d+w:
            v.d=u.d+w
            v.p=u



a = Vertex('a')
b = Vertex('b')
c = Vertex('c')
d = Vertex('d')
e = Vertex('e')
f = Vertex('f')

V = [a, b, c, d, e, f]

ab = Edge(a, b, -6)
ae = Edge(a, e, 15)
ad = Edge(a, d, -4)
bc = Edge(b, c, 7)
cf = Edge(c, f, -3)
de = Edge(d, e, 11)
fe = Edge(f, e, 5)
ec = Edge(e, c, 13)

E = [ab, ae, ad, bc, cf, de, fe, ec]

G = Graph(V, E)

print(G)

G.shortest_path(a, e)


