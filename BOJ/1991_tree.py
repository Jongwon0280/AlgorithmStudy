import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())

tree = {}

for i in range(n):
    node, start, end=map(str,input().split())

    

    tree[node]=[start,end]


def preorder(n):
    global tree
    if n == '.':
        return 

    print(n,end="")
    preorder(tree[n][0])
    preorder(tree[n][1])
    
def inorder(n):
    global tree
    if n == '.':
        return 

    
    inorder(tree[n][0])
    print(n,end="")
    inorder(tree[n][1])
    
def postorder(n):
    global tree
    if n == '.':
        return 

    
    postorder(tree[n][0])
    
    postorder(tree[n][1])
    print(n,end="")
    

preorder('A')
print()
inorder('A')
print()
postorder('A')
