# Python program to check binary tree is a subtree of  
# another tree 
  
# A binary tree node 
class Node: 
  
    # Constructor to create a new node 
    def __init__(self, data): 
        self.data = data  
        self.left = None
        self.right = None
  
# A utility function to check whether trees with roots 
# as root 1 and root2 are indetical or not 
def areIdentical(root1, root2): 
      
    # Base Case 
    if root1 is None and root2 is None: 
        return True
    if root1 is None or root2 is None: 
        return False
  
    # Check if the data of both roots is same and data of 
    # left and right subtrees are also same 
    return (root1.data == root2.data and 
            areIdentical(root1.left , root2.left)and
            areIdentical(root1.right, root2.right) 
            )  
  
# This function returns True if S is a subtree of T, 
# otherwise False 
def isSubtree(T, S): 
      
    # Base Case 
    if S is None: 
        return True
  
    if T is None: 
        return False
  
    # Check the tree with root as current node 
    if (areIdentical(T, S)): 
        return True
  
    # IF the tree with root as current node doesn't match 
    # then try left and right subtreee one by one 
    return isSubtree(T.left, S) or isSubtree(T.right, S) 
  
  
# Driver program to test above function 
  
""" TREE 1 
     Construct the following tree 
              5 
            /    \ 
          3       7 
        /   \    /  \ 
      2      4  6    8 
  
    """

T = Node(5) 
T.right = Node(7) 
T.right.right  = Node(8) 
T.right.left  = Node(6) 
T.left = Node(3) 
T.left.left = Node(2) 
T.left.right = Node(4) 

""" TREE 2 
     Construct the following tree 
          5 
        /    \ 
      3       7 
    """
S = Node(5) 
S.left = Node(3) 
S.right = Node(7) 
  
if isSubtree(T, S): 
    print("Tree 2 is subtree of Tree 1")
else: 
    print("Tree 2 is not a subtree of Tree 1")
  