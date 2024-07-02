import networkx as nx
import matplotlib.pyplot as plt # type: ignore
import random
class Graph:
    def __init__(self):
        self.adj_list = {}  # adjacency list to store the graph

    def add_edge(self, start, end, weight):
        if start not in self.adj_list:
            self.adj_list[start] = []
        self.adj_list[start].append((end, weight))
        if end not in self.adj_list:
            self.adj_list[end] = []  # Ensure the end node is in the adjacency list

    def remove_edge(self, start, end):
        if start in self.adj_list:
            self.adj_list[start] = [(e, w) for e, w in self.adj_list[start] if e != end]

    def get_neighbors(self, node):
        return self.adj_list.get(node, [])

    def get_all_edges(self):
        edges = []
        for start in self.adj_list:
            for end, weight in self.adj_list[start]:
                edges.append((start, end, weight))
        return edges

    def get_all_vertices(self):
        return list(self.adj_list.keys())

    def visualize(self):
        G = nx.DiGraph()  # Create a directed graph

        for start in self.adj_list:
            for end, weight in self.adj_list[start]:
                G.add_edge(start, end, weight=weight)

        pos = nx.spring_layout(G)  # Position nodes using Fruchterman-Reingold force-directed algorithm

        plt.figure(figsize=(10, 7))
        nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, edge_color='black', linewidths=1, font_size=15, font_color='black', font_weight='bold', arrows=True)
        
        edge_labels = {(start, end): f"{weight}" for start, end, weight in self.get_all_edges()}
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

        plt.title('Graph Visualization')
        plt.show()

# Example usage
g = Graph()

# Adding edges to create a graph with 7 vertices and 20 edges
edges = [
    ('A', 'B', 5), ('A', 'C', 6), ('B', 'E', 3),
    ('B', 'F', 4), ('C', 'G', 5), ('C', 'E', 2), ('D', 'F', 8),
    ('D', 'G', 9), ('E', 'A', 1), ('E', 'C', 4), ('F', 'B', 2),
    ('F', 'D', 6), ('G', 'A', 7), ('G', 'B', 3), ('A', 'F', 5),
     ('C', 'D', 4), ('D', 'E', 3), ('E', 'F', 8)
]

for start, end, weight in edges:
    g.add_edge(start, end, weight)

class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.entry_finder = {}
        self.REMOVED = '<removed-task>'
        self.counter = 0

    def push(self, task, priority):
        if task in self.entry_finder:
            self.remove_task(task)
        entry = [priority, self.counter, task]
        self.entry_finder[task] = entry
        self.heap.append(entry)
        self._sift_up(len(self.heap) - 1)
        self.counter += 1

    def _sift_up(self, idx):
        while idx > 0:
            parent_idx = (idx - 1) // 2
            if self.heap[idx][0] < self.heap[parent_idx][0]:
                self.heap[idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx]
                idx = parent_idx
            else:
                break

    def remove_task(self, task):
        entry = self.entry_finder.pop(task)
        entry[-1] = self.REMOVED

    def decrease_key(self, task, new_priority):
        if task in self.entry_finder:
            entry = self.entry_finder[task]
            if new_priority < entry[0]:
                entry[0] = new_priority
                self._sift_up(self.heap.index(entry))

    def extract_minimum(self):
        while self.heap:
            priority, _, task = self.heap[0]
            if task is not self.REMOVED:
                del self.entry_finder[task]
                last_entry = self.heap.pop()
                if self.heap:
                    self.heap[0] = last_entry
                    self._sift_down(0)
                return task
            else:
                self.heap.pop(0)
        raise KeyError('pop from an empty priority queue')

    def _sift_down(self, idx):
        end = len(self.heap)
        while True:
            left_child_idx = 2 * idx + 1
            right_child_idx = 2 * idx + 2
            smallest = idx
            if left_child_idx < end and self.heap[left_child_idx][0] < self.heap[smallest][0]:
                smallest = left_child_idx
            if right_child_idx < end and self.heap[right_child_idx][0] < self.heap[smallest][0]:
                smallest = right_child_idx
            if smallest != idx:
                self.heap[idx], self.heap[smallest] = self.heap[smallest], self.heap[idx]
                idx = smallest
            else:
                break

    def is_empty(self):
        return len(self.entry_finder) == 0
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("dequeue from empty queue")

    def is_empty(self):
        return len(self.items) == 0
    def first(self):
        if self.size() <= 0:
            return None
        else :
            return self.items[0]
    def size(self):
        return len(self.items)
class DisjointSet:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def make_set(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0

    def find_set(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find_set(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find_set(x)
        root_y = self.find_set(y)

        if root_x != root_y:
            # Union by rank
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1
def depth_first_search(graph:Graph,start):
    stack = []
    all_vertices = graph.get_all_vertices()
    stack.append(start)
    marked =[start[0]]
    print(marked[0][0])
    while len(stack) !=0:
        u = stack[-1]
        print(u)
        z =  graph.get_neighbors(u)
        unmarked = []
        for r in z:
            if r[0] not in marked:
                unmarked.append(r)
        if len(unmarked) != 0 :
            v = unmarked[0]
            marked.append(v[0])
            stack.append(v[0])
        else :
            stack.pop()
    return marked
def breadth_first_search(graph:Graph,start):
    q = Queue ()
    q.enqueue(start)
    marked =[start[0]]
    while q.size() !=0:
        u = q.first()
        print(u)
        z =  graph.get_neighbors(u)
        unmarked = []
        for r in z:
            if r[0] not in marked:
                unmarked.append(r)
        if len(unmarked) != 0 :
            v = unmarked[0]
            marked.append(v[0])
            q.enqueue(v[0])
        else :
            q.dequeue()
    return marked
def kruskal(graph:Graph):
    a = []
    d = DisjointSet()
    for v in graph.get_all_vertices():
        d.make_set(v)
    edges = graph.get_all_edges()
    edges.sort(key= lambda x:x[2])
    for i in edges:
        if d.find_set(i[0]) !=d.find_set(i[1]):
            a.append({i[0],i[1]})
            d.union(i[0],i[1])
    return a   
# def prim(graph:Graph):
#     a =[]
# def djikstra(graph:Graph):
#     for i in graph.get_all_vertices():
#         i.pi = None
#         i.key = 12312312
#     start.key  = 123123
#     while Q.isnotEmpty():
#         u = extract_min()
#         if d(v) + w(u,v) < d(u):
#             d(u) -= mathi ko 
            


if __name__=="__main__":
    print(kruskal(g))
    g.visualize()