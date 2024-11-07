# 트리 순회
# https://www.acmicpc.net/problem/1991

"""
    전위 순회한 결과 : ABDCEFG // (루트) (왼쪽 자식) (오른쪽 자식)
    중위 순회한 결과 : DBAECFG // (왼쪽 자식) (루트) (오른쪽 자식)
    후위 순회한 결과 : DBEGFCA // (왼쪽 자식) (오른쪽 자식) (루트)

    이진 트리의 노드의 개수 N(1 ≤ N ≤ 26)
    노드의 이름은 A부터 차례대로 알파벳 대문자로 매겨진다.
    항상 A가 루트 노드가 된다.
    자식 노드가 없는 경우에는 .으로 표현한다.
"""
import sys
class Node():
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

class Tree():
    def __init__(self, root):
        self.value = root

    # 전위 순회 VLR
    def preOrder(self, root : Node):
        if root is not None:
            print(f"{root.value}", end='')
            if root.left != '.':
                self.preOrder(nodeDict[root.left])
            if root.right != '.':
                self.preOrder(nodeDict[root.right])
        return

    # 중위순회 LVR
    def inOrder(self, root : Node):
        if root is not None:
            if root.left != '.':
                self.inOrder(nodeDict[root.left])
            print(f"{root.value}", end='')
            if root.right != '.':
                self.inOrder(nodeDict[root.right])
        return

    # 후위 순회 LRV
    def postOrder(self, root : Node):
        if root is not None:
            if root.left != '.':
                self.postOrder(nodeDict[root.left])
            if root.right != '.':
                self.postOrder(nodeDict[root.right])
            print(f"{root.value}", end='')
        return


nodeDict = {}
# 노드의 개수 N(1 ≤ N ≤ 26)
N = int(sys.stdin.readline())

for i in range(N):
    P, left, right = sys.stdin.readline().split()
    nodeDict[P] = Node(P, left, right)

root = nodeDict['A']
tree = Tree(root)
tree.preOrder(root)
print('')
tree.inOrder(root)
print('')
tree.postOrder(root)
