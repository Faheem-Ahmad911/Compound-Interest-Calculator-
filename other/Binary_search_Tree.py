# One of the version of the Binary search Tree.
class Node:  # class Node for the creation of the Tree.
    def __init__(self,value) -> None:
        self.left=None
        self.value=value
        self.right=None
class Tree:
    def create_node(self,value):
        return Node(value) #Creating the Node in the main Tree by caling the Node class.
    def add_object(self,node,value):
        if node is None:
            return self.create_node(value)
        else:
            if value < node.data :                   # Node enters data in such a way left side is smaller than middle and right side is bigger than middle.                      
                node.left =self.insert(node.left,value) 
            else:
                node.right=self.insert(node.right,value)

        return node
    

