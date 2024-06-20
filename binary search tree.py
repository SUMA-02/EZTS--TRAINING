#binary search tree
class node:
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None
       
def BST(root,value):
    if root==None:
        return node(value)
    if value<root.value:
        root.left=BST(root.left,value)
    if value>root.value:
        root.right=BST(root.right,value)
    return root    
def inorder(root):
    if root:
        inorder(root.left)
        print(root.value)
        inorder(root.right)         
list=[4,6,7,3,8,2,5,9,1]
root=node(list.pop(0))
#root=node(4)
for i in list:
    BST(root,i)
inorder(root)    
