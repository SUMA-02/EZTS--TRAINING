#right view
class node:
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None
def rightview(root):
    q=[root]
    q.append(None)
    #print(root.value)
    while len(q)>0:
        curr=q.pop(0)
        if curr==None:
            if len(q)==0:
                break
            else:
                #print(q[0].value)
                q.append(None)
        else:
            if q[0]==None:
                print(curr.value)
            if curr.left!=None:
                q.append(curr.left)
            if curr.right!=None:
                q.append(curr.right)
if __name__=="__main__":         
    root=node(1)
    root.left=node(2)
    root.right=node(5)
    root.left.left=node(3)
    root.left.right=node(4)
    root.left.right.left=node(9)
    root.left.right.left.right=node(10)
    root.left.right.left.right.left=node(14)
    root.right.right=node(6)
    root.right.right.left=node(7)
    root.right.right.right=node(8)
    root.right.right.left.right=node(11)
    root.right.right.left.right.left=node(12)
    root.right.right.left.right.left.right=node(13) 
    rightview(root)
    #right view
class node:
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None
def rightview(root):
    q=[root]
    q.append(None)
    #print(root.value)
    while len(q)>0:
        curr=q.pop(0)
        if curr==None:
            if len(q)==0:
                break
            else:
                #print(q[0].value)
                q.append(None)
        else:
            if q[0]==None:
                print(curr.value)
            if curr.left!=None:
                q.append(curr.left)
            if curr.right!=None:
                q.append(curr.right)
if __name__=="__main__":         
    root=node(1)
    root.left=node(2)
    root.right=node(5)
    root.left.left=node(3)
    root.left.right=node(4)
    root.left.right.left=node(9)
    root.left.right.left.right=node(10)
    root.left.right.left.right.left=node(14)
    root.right.right=node(6)
    root.right.right.left=node(7)
    root.right.right.right=node(8)
    root.right.right.left.right=node(11)
    root.right.right.left.right.left=node(12)
    root.right.right.left.right.left.right=node(13) 
    rightview(root)
    