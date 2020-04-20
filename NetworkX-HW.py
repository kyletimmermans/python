'''
Kyle Timmermans
Dr. Zhang
CISC 4080
Lab 4 - Graph Class

run with python3 lab5.py
'''

import networkx as nx
from networkx.algorithms import *
from networkx.exception import *

# Variables
file = input("Please input the path of the test-case file you would like to use e.g. /Desktop/School/test.txt: ")  # Get file input
directed = 0
response = False
items = []

def lineCheck(file, string):
    global response
    try:
        with open(file, 'r') as fileObj: #Open file in read-only
            for line in fileObj:  # Check every line
                if string in line:  # If in the line, return True, else False
                    response = True  # Must go here or returns to early
                    return True
        response = True  # Must go here or returns too early
        return False
    except FileNotFoundError:
        print("File not found, please try again")

lineCheck(file, "true")
while response is not True:
    file = input("Please input the path of the test-case file you would like to use e.g. /Desktop/School/test.txt: ")  # Get file input
    lineCheck(file, "true")

if lineCheck(file, "true"):
    directed = 1
else:
    directed = 0

with open(file, 'r') as fileObj:  # Open file in read-only
    for line in fileObj:
        items.append(line)

for elem in range(2, len(items), 1):  # Start into actual nodes and edges
    items[elem] = items[elem].replace(' ', '').replace('-', ' ').replace('>', '').strip("\n")  # Hyphen can have space, every list has at least a hyphen
    items[elem] = items[elem].split()  # Join up everything to be iterable

count = len(open(file).readlines())
if count < 20:
    items = items[2:]  # Remove early items
else:
    items = items[4:-2]  # Adds extra 2 empty lists, fixed here

if directed == 1:
    G = nx.DiGraph()
    for i in range(len(items)):
        G.add_edge((items[i][0]), (items[i][1]))  # Directed
else:
    G = nx.Graph()
    for i in range(len(items)):  # Add items
        G.add_edge(items[i][0], items[i][1])  # Undirected

# Possible path
print("")
possiblePath = input("Enter first and second node to check whether they have a path between them (e.g. shirt tie) (e.g. A B): ")
print("")
possiblePath = possiblePath.split()
if has_path(G, possiblePath[0], possiblePath[1]):
    print("There is a possible path from "+str(possiblePath[0]+" to "+str(possiblePath[1])))
else:
    print("There is not a possible path from " + str(possiblePath[0] + " to " + str(possiblePath[1])))

# BFS Tree
print("")
bfsTree = input("Enter a source node for a BFS Tree to be constructed from (e.g. tie) (e.g. B): ")
print("")
print("The BFS Tree from source "+str(bfsTree)+" is ", end='')
B = nx.bfs_tree(G, source=bfsTree, depth_limit=99)  # Print as deep as possible for case tests
print(list(B.edges))

# BFS Shortest Hops
print("")
bfsShortHop = input("Enter two nodes to get the shortest hop path using BFS (e.g. shirt tie) (e.g. A B): ")
print("")
bfsShortHop = bfsShortHop.split()
try:
    x = bidirectional_shortest_path(G, bfsShortHop[0], bfsShortHop[1])
    print("The shortest hop path from " + str(bfsShortHop[0]) + " to " + str(bfsShortHop[1])+" is ", end='')
    print(x)
except NetworkXNoPath:
    print("The is no possible path from "+str(bfsShortHop[0])+" to "+str(bfsShortHop[1]))

# DFS Tree
print("")
dfsTree = input("Enter a source node for a DFS Tree (e.g. A) (e.g. shirt): ")
print("The DFS Tree is: ", end='')
T = nx.dfs_tree(G, source=dfsTree, depth_limit=99)  # Print as deep as possible for case tests
print(list(T.edges))
print("")


# DFS Topological Sort
choice = input("Would you like to see a topological sort tree of the graph? (Y/n): ")
if choice == 'Y' or 'y':
    print("")
    print("The Topological sort based off of this graph is:")
    try:
        print(list(nx.topological_sort(G)))
    except NetworkXError:
        print("Error: Can't do Topological sort on undirected graphs")
    except NetworkXUnfeasable:
        print("Error: Can't get topological sort of a graph w/ a cycle changed during iteration")
else:
    print("Have a great day!")

