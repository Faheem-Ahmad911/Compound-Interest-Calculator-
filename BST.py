class Node:
    def __init__(self,value):
        self.left=None
        self.value=value
        self.right=None
class BST:
    def __init__(self) -> None:
        self.root=None
        #Make insert function in recursive mode.
    def insert(self,value): 
        self.root =self.rinsert(self.root,value)
    def rinsert(self,root,value):
        if root is None:
            return Node(value)
        if value < root.value:
            root.left=self.rinsert(root.left,value)
        elif value > root.value:
            root.right=self.rinsert(root.right,value)
        return root
    def search(self,data):
        return self.rsearch(self.root,data)

    def rsearch(self,root,data):
        if data is None or root.value==data:
            return root
        if data < root.value :
            return self.rsearch(root.left,data)
        else:
            return self.rsearch(root.right,data)
    def inorder(self):
        list=[]
        self.rinorder(self.root,list)
        return list
    def rinorder(self,root,list):
        if root:
            self.rinorder(root.left,list)
            list.append(root.value)
            self.rinorder(root.right,list)
    def preorder(self):
        list=[]
        self.rpreorder(self.root,list)
        return list
    def rpreorder(self,root,list):
        if root:
            list.append(root.value)
            self.rpreorder(root.left,list)
            self.rpreorder(root.right,list)
    def postorder(self):
        list=[]
        self.rpostorder(self.root,list)
        return list
    def rpostorder(self,root,list):
        self.rpreorder(root.left,list)
        self.rpreorder(root.right,list)
        list.append(root.value)
    def min_value(self,root):
        current=root
        while current.left is not None:
            current=current.left
        return current.value
    def max_value(self,root):
        current=root
        while current.right is not None:
            current=current.right
        return current.value
    def Delete(self,data):
        self.root=self.rdelete(self.root,data)
    def rdelete(self,root,data):
        if root is None:
            return None
        if data < root.left:
            root.left=self.rdelete(root.left,data)
        elif  data > root.right:
            root.right=self.rdelete(root.right,data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                root.item=self.min_value(root.right)
                self.rdelete(root.right,root.item)
            return root










        
        

        


    


            
        

        
    